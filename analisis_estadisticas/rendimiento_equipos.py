import matplotlib.pyplot as plt


class RendimientoEquipo:
    def __init__(self, partidos):
        self.partidos = partidos

    def posesion_promedio_por_equipo(self, equipo_id):
        posesion_total = 0
        partidos_jugados = 0
        for p in self.partidos:
            if p["equipo_local_id"] == equipo_id or p["equipo_visitante_id"] == equipo_id:
                posesion_total += p.get("posesion_"+str(equipo_id), 0)
                partidos_jugados += 1
        return posesion_total / partidos_jugados if partidos_jugados else 0

    def tiros_por_partido(self, equipo_id):
        tiros_totales = 0
        partidos_jugados = 0
        for p in self.partidos:
            if p["equipo_local_id"] == equipo_id:
                tiros_totales += p.get("tiros_local", 0)
                partidos_jugados += 1
            elif p["equipo_visitante_id"] == equipo_id:
                tiros_totales += p.get("tiros_visitante", 0)
                partidos_jugados += 1
        return tiros_totales / partidos_jugados if partidos_jugados else 0

    def goles_por_partido(self, equipo_id):
        goles_totales = 0
        partidos_jugados = 0
        for p in self.partidos:
            if p["equipo_local_id"] == equipo_id:
                goles_totales += p.get("goles_local", 0)
                partidos_jugados += 1
            elif p["equipo_visitante_id"] == equipo_id:
                goles_totales += p.get("goles_visitante", 0)
                partidos_jugados += 1
        return goles_totales / partidos_jugados if partidos_jugados else 0

    def goles_contra_por_partido(self, equipo_id):
        goles_totales = 0
        partidos_jugados = 0
        for p in self.partidos:
            if p["equipo_local_id"] == equipo_id:
                goles_totales += p.get("goles_visitante", 0)
                partidos_jugados += 1
            elif p["equipo_visitante_id"] == equipo_id:
                goles_totales += p.get("goles_local", 0)
                partidos_jugados += 1
        return goles_totales / partidos_jugados if partidos_jugados else 0



def grafico_posesion(posesion_por_equipo):
    equipos, posesion = zip(*posesion_por_equipo)
    plt.figure(figsize=(10, 6))
    plt.bar(equipos, posesion, color='orange')
    plt.title('Posesión Promedio por Equipo')
    plt.xlabel('Equipo')
    plt.ylabel('Posesión Promedio (%)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def grafico_tiros(tiros_por_equipo):
    equipos, tiros = zip(*tiros_por_equipo)
    plt.figure(figsize=(10, 6))
    plt.bar(equipos, tiros, color='purple')
    plt.title('Tiros Promedio por Partido')
    plt.xlabel('Equipo')
    plt.ylabel('Tiros por Partido')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def rendimiento_equipos(partidos):
    rendimiento = RendimientoEquipo(partidos)
    
    # Obtener posesión promedio y tiros por equipo
    equipos = [p["equipo_local_id"] for p in partidos] + [p["equipo_visitante_id"] for p in partidos]
    equipos = list(set(equipos))  # Lista de equipos únicos

    # Estadísticas de posesión y tiros
    posesion_por_equipo = [(equipo, rendimiento.posesion_promedio_por_equipo(equipo)) for equipo in equipos]
    tiros_por_equipo = [(equipo, rendimiento.tiros_por_partido(equipo)) for equipo in equipos]

    # Graficar los equipos
    grafico_posesion(posesion_por_equipo)
    grafico_tiros(tiros_por_equipo)
