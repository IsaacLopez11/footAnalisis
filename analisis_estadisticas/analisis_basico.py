import matplotlib.pyplot as plt

def lista_goleadores(partidos):
    goles_totales = {}
    for partido in partidos:
        for estad in partido.get("estadisticas", []):
            jugador = estad["jugador_id"]
            goles_totales[jugador] = goles_totales.get(jugador, 0) + estad["goles"]
    # Orden descendente por goles
    return sorted(goles_totales.items(), key=lambda x: x[1], reverse=True)

def lista_asistencias(partidos):
    asistencias_totales = {}
    for partido in partidos:
        for estad in partido.get("estadisticas", []):
            jugador = estad["jugador_id"]
            asistencias_totales[jugador] = asistencias_totales.get(jugador, 0) + estad["asistencias"]
    return sorted(asistencias_totales.items(), key=lambda x: x[1], reverse=True)

def promedio_goles_por_partido(partidos):
    total_goles = sum(p["goles_local"] + p["goles_visitante"] for p in partidos)
    return total_goles / len(partidos) if partidos else 0

def promedio_asistencias_por_partido(partidos):
    total_asistencias = sum(
        sum(estad["asistencias"] for estad in p.get("estadisticas", []))
        for p in partidos
    )
    return total_asistencias / len(partidos) if partidos else 0




def grafico_goleadores(goleadores):
    jugadores, goles = zip(*goleadores)
    plt.figure(figsize=(10, 6))
    plt.bar(jugadores, goles, color='green')
    plt.title('Goleadores de la Temporada')
    plt.xlabel('Jugador')
    plt.ylabel('Goles')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def grafico_asistentes(asistentes):
    jugadores, asistencias = zip(*asistentes)
    plt.figure(figsize=(10, 6))
    plt.bar(jugadores, asistencias, color='blue')
    plt.title('Asistentes de la Temporada')
    plt.xlabel('Jugador')
    plt.ylabel('Asistencias')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def analisis_basico(partidos):
    goles = lista_goleadores(partidos)
    asistencias = lista_asistencias(partidos)

    # Graficar goleadores y asistentes
    grafico_goleadores(goles)
    grafico_asistentes(asistencias)

    # Promedios de goles y asistencias
    promedio_goles = promedio_goles_por_partido(partidos)
    promedio_asistencias = promedio_asistencias_por_partido(partidos)

    print(f'Promedio de goles por partido: {promedio_goles}')
    print(f'Promedio de asistencias por partido: {promedio_asistencias}')
