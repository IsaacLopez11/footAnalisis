import random
import math
from datetime import date

from models.base_model import BaseModel as BM
from models.partido import Partido
from models.estadisticas_jugador import EstadisticasJugador
from models.estadisticas_partido import EstadisticasPartido
from models.jugadores import Jugador


def jugar_partido(equipo_local_id, equipo_visitante_id, fecha=None, liga_id=None):
    fecha = fecha or date.today().isoformat()

    # 1️⃣ Obtener jugadores
    jugadores_local = BM.consulta_general("SELECT * FROM jugadores WHERE equipo_id = ?", (equipo_local_id,))
    jugadores_visitante = BM.consulta_general("SELECT * FROM jugadores WHERE equipo_id = ?", (equipo_visitante_id,))

    if not jugadores_local or not jugadores_visitante:
        return {"error": "Uno de los equipos no tiene jugadores."}

    # 2️⃣ Obtener atributos de cada jugador
    atributos_map = {}
    for j in jugadores_local + jugadores_visitante:
        attrs = BM.consulta_general("SELECT * FROM atributos_jugador WHERE jugador_id = ?", (j["id"],))
        atributos_map[j["id"]] = attrs[0] if attrs else {}

    # 3️⃣ Calcular fuerza del equipo
    def fuerza_equipo(atributos_lista):
        """Calcula fuerza simplificada: ataque y defensa de un equipo."""
        atributos_lista = [d for d in atributos_lista if d]
        if not atributos_lista:
            return {"ataque": 0.0, "defensa": 0.0}

        avg = {k: sum(d.get(k, 0) or 0 for d in atributos_lista) / len(atributos_lista)
               for k in atributos_lista[0]}

        ataque = (avg.get("remate", 0) * 0.4 +
                  avg.get("desmarques", 0) * 0.25 +
                  avg.get("tecnica", 0) * 0.2 +
                  avg.get("pase", 0) * 0.15)

        defensa = (avg.get("marcaje", 0) * 0.5 +
                   avg.get("entradas", 0) * 0.3 +
                   avg.get("colocacion", 0) * 0.2)

        ataque /= 100.0
        defensa /= 100.0
        return {"ataque": ataque, "defensa": defensa}

    fuerza_local = fuerza_equipo([atributos_map[j["id"]] for j in jugadores_local])
    fuerza_visitante = fuerza_equipo([atributos_map[j["id"]] for j in jugadores_visitante])

    # 4️⃣ Simular goles basados en fuerza
    def simular_goles(fuerza_ataque, fuerza_defensa_rival):
        base = 1.5 + (fuerza_ataque * 2.5) - (fuerza_defensa_rival * 1.5)
        base = max(0.2, base)
        goles = max(0, int(round(random.gauss(base, 1))))
        return goles

    goles_local = simular_goles(fuerza_local["ataque"], fuerza_visitante["defensa"])
    goles_visit = simular_goles(fuerza_visitante["ataque"], fuerza_local["defensa"])

    print(f"⚽ Resultado simulado: Local {goles_local} - Visitante {goles_visit}")

    # 5️⃣ Inicializar estadísticas por jugador
    stats_por_jugador = {
        j["id"]: {
            "jugador_id": j["id"],
            "goles": 0,
            "asistencias": 0,
            "tarjetas_amarillas": 0,
            "tarjetas_rojas": 0,
            "minutos_jugados": random.randint(70, 95),
            "calificacion": 6.0 + random.random() * 3.0
        }
        for j in jugadores_local + jugadores_visitante
    }

    # 🔹 Elegir jugadores que marcan y asisten
    def elegir_jugador_para_gol(jugadores, atributos_map):
        weights = []
        for j in jugadores:
            a = atributos_map.get(j["id"], {})
            w = (a.get("remate", 0) * 1.2 +
                 a.get("tiros_lejanos", 0) * 0.6 +
                 a.get("desmarques", 0) * 0.8)
            if j.get("posicion", "").lower().startswith("del"):
                w *= 1.2
            weights.append(max(w, 0.1))
        total = sum(weights)
        r = random.random() * total
        acum = 0
        for i, w in enumerate(weights):
            acum += w
            if r <= acum:
                return jugadores[i]
        return jugadores[-1]

    def elegir_asistente(jugadores, excluido_id, atributos_map):
        candidates = [j for j in jugadores if j["id"] != excluido_id]
        if not candidates:
            return None
        weights = []
        for j in candidates:
            a = atributos_map.get(j["id"], {})
            w = a.get("pase", 0) * 0.7 + a.get("vision", 0) * 0.6
            weights.append(max(w, 0.1))
        total = sum(weights)
        r = random.random() * total
        acum = 0
        for i, w in enumerate(weights):
            acum += w
            if r <= acum:
                return candidates[i]
        return candidates[-1]

    # 6️⃣ Asignar goles y asistencias
    for _ in range(goles_local):
        scorer = elegir_jugador_para_gol(jugadores_local, atributos_map)
        assister = elegir_asistente(jugadores_local, scorer["id"], atributos_map)
        stats_por_jugador[scorer["id"]]["goles"] += 1
        if assister:
            stats_por_jugador[assister["id"]]["asistencias"] += 1

    for _ in range(goles_visit):
        scorer = elegir_jugador_para_gol(jugadores_visitante, atributos_map)
        assister = elegir_asistente(jugadores_visitante, scorer["id"], atributos_map)
        stats_por_jugador[scorer["id"]]["goles"] += 1
        if assister:
            stats_por_jugador[assister["id"]]["asistencias"] += 1

    # 7️⃣ Registrar partido en base de datos
    partido_obj = Partido(
        fecha=fecha,
        equipo_local_id=equipo_local_id,
        equipo_visitante_id=equipo_visitante_id,
        goles_local=goles_local,
        goles_visitante=goles_visit,
        liga_id=liga_id,
        jugado=1
    )
    partido_id = partido_obj.crear_partido()
    partido_obj.id = partido_id

    # 8️⃣ Insertar estadísticas de jugadores
    for pid, s in stats_por_jugador.items():
        s["partido_id"] = partido_id
        est_obj = EstadisticasJugador(
            partido_id=s["partido_id"],
            jugador_id=pid,
            goles=s["goles"],
            asistencias=s["asistencias"],
            tarjetas_amarillas=s["tarjetas_amarillas"],
            tarjetas_rojas=s["tarjetas_rojas"],
            minutos_jugados=s["minutos_jugados"],
            calificacion=s["calificacion"]
        )
        est_obj.crear_estadistica()

    # 9️⃣ Insertar estadísticas generales del partido
    estad_partido_obj = EstadisticasPartido(
        partido_id=partido_id,
        posesion_local=random.randint(45, 60),
        posesion_visitante=100 - random.randint(45, 60),
        tiros_local=random.randint(5, 15),
        tiros_visitante=random.randint(4, 12),
        tiros_puerta_local=random.randint(2, 8),
        tiros_puerta_visitante=random.randint(1, 6),
        faltas_local=random.randint(8, 15),
        faltas_visitante=random.randint(8, 15),
        corners_local=random.randint(2, 8),
        corners_visitante=random.randint(2, 8),
        tarjetas_local=random.randint(0, 4),
        tarjetas_visitante=random.randint(0, 4)
    )
    estad_partido_obj.crear_estadistica()

    # 🔟 Devolver resumen
    resumen = {
        "partido_id": partido_id,
        "resultado": {"local": goles_local, "visitante": goles_visit},
        "estadisticas_jugadores": list(stats_por_jugador.values()),
        "estadisticas_partido": list(stats_por_jugador.values())
    }

    return resumen
