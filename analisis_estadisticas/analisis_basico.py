import matplotlib.pyplot as plt

# ------------------------
# Funciones de cálculo
# ------------------------

def lista_goleadores(estadisticas):
    goles_totales = {}
    for estad in estadisticas:
        jugador = estad["jugador_id"]
        goles_totales[jugador] = goles_totales.get(jugador, 0) + estad.get("goles", 0)
    return sorted(goles_totales.items(), key=lambda x: x[1], reverse=True)


def lista_asistencias(estadisticas):
    asistencias_totales = {}
    for estad in estadisticas:
        jugador = estad["jugador_id"]
        asistencias_totales[jugador] = asistencias_totales.get(jugador, 0) + estad.get("asistencias", 0)
    return sorted(asistencias_totales.items(), key=lambda x: x[1], reverse=True)


def lista_minutos(estadisticas):
    minutos_totales = {}
    for estad in estadisticas:
        jugador = estad["jugador_id"]
        minutos_totales[jugador] = minutos_totales.get(jugador, 0) + estad.get("minutos_jugados", 0)
    return sorted(minutos_totales.items(), key=lambda x: x[1], reverse=True)


def lista_calificaciones(estadisticas):
    calificaciones = {}
    contador = {}
    for estad in estadisticas:
        jugador = estad["jugador_id"]
        calificaciones[jugador] = calificaciones.get(jugador, 0) + estad.get("calificacion", 0)
        contador[jugador] = contador.get(jugador, 0) + 1
    # Calificación media
    return sorted(
        ((jugador, calificaciones[jugador] / contador[jugador]) for jugador in calificaciones),
        key=lambda x: x[1],
        reverse=True
    )


def lista_tarjetas(estadisticas):
    amarillas = {}
    rojas = {}
    for estad in estadisticas:
        jugador = estad["jugador_id"]
        amarillas[jugador] = amarillas.get(jugador, 0) + estad.get("tarjetas_amarillas", 0)
        rojas[jugador] = rojas.get(jugador, 0) + estad.get("tarjetas_rojas", 0)
    return (
        sorted(amarillas.items(), key=lambda x: x[1], reverse=True),
        sorted(rojas.items(), key=lambda x: x[1], reverse=True)
    )


def calcular_por_90_minutos(estadisticas, key):
    """Devuelve lista de tuplas (jugador, valor_por_90)"""
    totales = {}
    minutos = {}
    for estad in estadisticas:
        jugador = estad["jugador_id"]
        totales[jugador] = totales.get(jugador, 0) + estad.get(key, 0)
        minutos[jugador] = minutos.get(jugador, 0) + estad.get("minutos_jugados", 0)
    por_90 = []
    for jugador in totales:
        if minutos[jugador] > 0:
            por_90.append((jugador, totales[jugador] / minutos[jugador] * 90))
        else:
            por_90.append((jugador, 0))
    return sorted(por_90, key=lambda x: x[1], reverse=True)
# ------------------------
# Funciones de gráficos
# ------------------------

def graficar_barras(datos, titulo, ylabel, color='blue'):
    if not datos:
        print(f"⚠️ No hay datos para {titulo}")
        return
    jugadores, valores = zip(*datos)
    plt.figure(figsize=(10,6))
    plt.bar(jugadores, valores, color=color)
    plt.title(titulo)
    plt.xlabel("Jugador")
    plt.ylabel(ylabel)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# ------------------------
# Función principal
# ------------------------

def analisis_basico_jugadores(estadisticas):
    # Goleadores
    goleadores = lista_goleadores(estadisticas)
    graficar_barras(goleadores[:10], "Goleadores de la Temporada", "Goles", color='green')

    # Asistencias
    asistencias = lista_asistencias(estadisticas)
    graficar_barras(asistencias[:10], "Asistentes de la Temporada", "Asistencias", color='blue')

    # Minutos jugados
    minutos = lista_minutos(estadisticas)
    graficar_barras(minutos[:10], "Minutos Jugados", "Minutos", color='orange')

    # Calificación media
    calificaciones = lista_calificaciones(estadisticas)
    graficar_barras(calificaciones[:10], "Calificación Media", "Calificación", color='purple')

    # Tarjetas
    amarillas, rojas = lista_tarjetas(estadisticas)
    graficar_barras(amarillas[:10], "Tarjetas Amarillas", "Cantidad", color='yellow')
    graficar_barras(rojas[:10], "Tarjetas Rojas", "Cantidad", color='red')
