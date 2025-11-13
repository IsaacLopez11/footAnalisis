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
    return sorted(
        ((jugador, calificaciones[jugador] / contador[jugador]) for jugador in calificaciones),
        key=lambda x: x[1], reverse=True
    )

def lista_tarjetas(estadisticas):
    amarillas = {}
    rojas = {}
    minutos = {}
    for estad in estadisticas:
        jugador = estad["jugador_id"]
        minutos[jugador] = minutos.get(jugador, 0) + estad.get("minutos_jugados", 0)
        amarillas[jugador] = amarillas.get(jugador, 0) + estad.get("tarjetas_amarillas", 0)
        rojas[jugador] = rojas.get(jugador, 0) + estad.get("tarjetas_rojas", 0)
    return (
        sorted(((j, amarillas[j], minutos[j]) for j in amarillas), key=lambda x: x[1]/x[2]*90 if x[2]>0 else 0, reverse=True),
        sorted(((j, rojas[j], minutos[j]) for j in rojas), key=lambda x: x[1]/x[2]*90 if x[2]>0 else 0, reverse=True)
    )

# ------------------------
# Funciones normalizadas por 90 minutos
# ------------------------

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
# Función de gráficos
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
    # Goleadores totales
    graficar_barras(lista_goleadores(estadisticas)[:10], "Goleadores Totales", "Goles", color='green')

    # Goleadores por 90 minutos
    graficar_barras(calcular_por_90_minutos(estadisticas, "goles")[:10], "Goles por 90 minutos", "Goles / 90min", color='darkgreen')

    # Asistencias totales
    graficar_barras(lista_asistencias(estadisticas)[:10], "Asistencias Totales", "Asistencias", color='blue')

    # Asistencias por 90 minutos
    graficar_barras(calcular_por_90_minutos(estadisticas, "asistencias")[:10], "Asistencias por 90 minutos", "Asistencias / 90min", color='darkblue')

    # Minutos jugados
    graficar_barras(lista_minutos(estadisticas)[:10], "Minutos Jugados", "Minutos", color='orange')

    # Calificación media
    graficar_barras(lista_calificaciones(estadisticas)[:10], "Calificación Media", "Calificación", color='purple')

    # Tarjetas por 90 minutos
    amarillas, rojas = lista_tarjetas(estadisticas)
    graficar_barras([(j, a/ m *90 if m>0 else 0) for j,a,m in amarillas[:10]], "Tarjetas Amarillas por 90 minutos", "TA / 90min", color='yellow')
    graficar_barras([(j, r/ m *90 if m>0 else 0) for j,r,m in rojas[:10]], "Tarjetas Rojas por 90 minutos", "TR / 90min", color='red')
