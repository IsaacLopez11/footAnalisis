from models.estadisticas_jugador import EstadisticasJugador
import matplotlib.pyplot as plt
from analisis_estadisticas.analisis_basico import lista_goleadores, grafico_goleadores



jugador = EstadisticasJugador()
estadisticas = jugador.obtener_estadisticas_por_jugador(5)

print (estadisticas)


partidos = [e['partido_id'] for e in estadisticas]
goles = [e['goles'] for e in estadisticas]
asistencias = [e['asistencias'] for e in estadisticas]
calificaciones = [e['calificacion'] for e in estadisticas]

# Gráfico de goles por partido
plt.figure(figsize=(10, 5))
plt.bar(partidos, goles, color='green')
plt.title('Goles por Partido - Jugador 5')
plt.xlabel('ID del Partido')
plt.ylabel('Goles')
plt.xticks(partidos)
plt.show()

# Gráfico de asistencias por partido
plt.figure(figsize=(10, 5))
plt.bar(partidos, asistencias, color='blue')
plt.title('Asistencias por Partido - Jugador 5')
plt.xlabel('ID del Partido')
plt.ylabel('Asistencias')
plt.xticks(partidos)
plt.show()

# Opcional: gráfico de calificaciones por partido
plt.figure(figsize=(10, 5))
plt.plot(partidos, calificaciones, marker='o', linestyle='-', color='orange')
plt.title('Calificación por Partido - Jugador 5')
plt.xlabel('ID del Partido')
plt.ylabel('Calificación')
plt.xticks(partidos)
plt.ylim(0, 10)
plt.grid(True)
plt.show()