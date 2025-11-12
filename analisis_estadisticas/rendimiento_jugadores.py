

import matplotlib.pyplot as plt

class EstadisticasJugador:
    def __init__(self, partidos):
        self.partidos = partidos

    def goles_por_jugador(self, jugador_id):
        goles = sum(
            estad["goles"] for p in self.partidos for estad in p.get("estadisticas", []) if estad["jugador_id"] == jugador_id
        )
        return goles

    def asistencias_por_jugador(self, jugador_id):
        asistencias = sum(
            estad["asistencias"] for p in self.partidos for estad in p.get("estadisticas", []) if estad["jugador_id"] == jugador_id
        )
        return asistencias

    def promedio_goles_por_partido(self, jugador_id):
        partidos_jugados = sum(
            1 for p in self.partidos if any(estad["jugador_id"] == jugador_id for estad in p.get("estadisticas", []))
        )
        goles = self.goles_por_jugador(jugador_id)
        return goles / partidos_jugados if partidos_jugados else 0

    def promedio_asistencias_por_partido(self, jugador_id):
        partidos_jugados = sum(
            1 for p in self.partidos if any(estad["jugador_id"] == jugador_id for estad in p.get("estadisticas", []))
        )
        asistencias = self.asistencias_por_jugador(jugador_id)
        return asistencias / partidos_jugados if partidos_jugados else 0

    def jugadores_mas_ofensivos(self):
        ofensivos = {}
        for p in self.partidos:
            for estad in p.get("estadisticas", []):
                jid = estad["jugador_id"]
                ofensivos[jid] = ofensivos.get(jid, 0) + estad["goles"] + estad["asistencias"]
        return sorted(ofensivos.items(), key=lambda x: x[1], reverse=True)

    def jugadores_mas_defensivos(self):
        defensivos = {}
        for p in self.partidos:
            for estad in p.get("estadisticas", []):
                jid = estad["jugador_id"]
                defensivos[jid] = defensivos.get(jid, 0) + estad.get("recuperaciones", 0) + estad.get("bloqueos", 0)
        return sorted(defensivos.items(), key=lambda x: x[1], reverse=True)



def grafico_ofensivos(ofensivos):
    jugadores, puntos_ofensivos = zip(*ofensivos)
    plt.figure(figsize=(10, 6))
    plt.bar(jugadores, puntos_ofensivos, color='red')
    plt.title('Jugadores Más Ofensivos')
    plt.xlabel('Jugador')
    plt.ylabel('Puntos Ofensivos (Goles + Asistencias)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def grafico_defensivos(defensivos):
    jugadores, puntos_defensivos = zip(*defensivos)
    plt.figure(figsize=(10, 6))
    plt.bar(jugadores, puntos_defensivos, color='blue')
    plt.title('Jugadores Más Defensivos')
    plt.xlabel('Jugador')
    plt.ylabel('Puntos Defensivos (Recuperaciones + Bloqueos)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def rendimiento_jugadores(partidos, jugador_id):
    estadisticas = EstadisticasJugador(partidos)
    
    # Obtener rendimiento ofensivo y defensivo
    ofensivos = estadisticas.jugadores_mas_ofensivos()
    defensivos = estadisticas.jugadores_mas_defensivos()

    # Graficar los jugadores más ofensivos y defensivos
    grafico_ofensivos(ofensivos[:10])  # Los 10 más ofensivos
    grafico_defensivos(defensivos[:10])  # Los 10 más defensivos
