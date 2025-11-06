# simulador/partido.py
from models.equipo import Equipo
from models.jugadores import Jugador
from models.atributos import AtributosJugador
from models.partido import Partido
from models.estadisticas_jugador import EstadisticasJugador
from models.estadisticas_partido import EstadisticasPartido
from models.clasificacion import Clasificacion
import random

def jugar_partido(equipo_local_id, equipo_visitante_id, fecha, liga_id):
    """
    Simula un partido entre dos equipos, genera resultados y estadísticas.
    """
    # 1️⃣ Obtener jugadores y atributos
    jugadores_local = Jugador().obtener_por_equipo(equipo_local_id)
    jugadores_visitante = Jugador().obtener_por_equipo(equipo_visitante_id)

    # 2️⃣ Calcular goles y estadísticas (muy básico por ejemplo)
    goles_local = random.randint(0,5)
    goles_visitante = random.randint(0,5)

    # 3️⃣ Crear el partido
    partido = Partido(fecha=fecha, equipo_local_id=equipo_local_id,
                      equipo_visitante_id=equipo_visitante_id,
                      goles_local=goles_local, goles_visitante=goles_visitante,
                      liga_id=liga_id, jugado=True)
    partido.crear_partido()

    # 4️⃣ Crear estadísticas de jugadores (ejemplo simplificado)
    for jugador in jugadores_local:
        stats = EstadisticasJugador(
            partido_id=partido.id,
            jugador_id=jugador[0],  # id del jugador
            goles=random.randint(0, goles_local),
            asistencias=random.randint(0, goles_local)
        )
        stats.crear_estadistica()

    for jugador in jugadores_visitante:
        stats = EstadisticasJugador(
            partido_id=partido.id,
            jugador_id=jugador[0],
            goles=random.randint(0, goles_visitante),
            asistencias=random.randint(0, goles_visitante)
        )
        stats.crear_estadistica()

    # 5️⃣ Estadísticas globales del partido
    estad_partido = EstadisticasPartido(
        partido_id=partido.id,
        posesion_local=random.randint(40,60),
        posesion_visitante=random.randint(40,60),
        tiros_local=random.randint(5,20),
        tiros_visitante=random.randint(5,20)
    )
    estad_partido.crear_estadistica()

    # 6️⃣ Actualizar clasificación
    # Aquí podrías llamar a una función que recalcule puntos y posiciones
