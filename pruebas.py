from models.equipo import Equipo
from models.jugadores import Jugador
from models.estadisticas_jugador import EstadisticasJugador

def pruebas():
    print("=== 🔹 PRUEBA EQUIPO ===")
    equipo = Equipo()
    equipo_data = equipo.obtener_equipo_por_id(3)
    print("Equipo por ID:", equipo_data)

    print("\n=== 🔹 PRUEBA LISTAR EQUIPOS ===")
    equipos_liga = equipo.listar_equipos()
    print(equipos_liga)

    print("\n=== 🔹 PRUEBA JUGADOR ===")
    jugador = Jugador()
    jugador_data = jugador.obtener_jugador_por_id(1)
    print("Jugador por ID:", jugador_data)

    print("\n=== 🔹 PRUEBA LISTAR JUGADORES POR EQUIPO ===")
    jugadores_equipo = jugador.listar_por_equipo(3)
    print(jugadores_equipo)

    print("\n=== 🔹 PRUEBA ESTADÍSTICAS ===")
    estad = EstadisticasJugador()
    estad_jugador = estad.obtener_estadisticas_de_jugador_por_id_partido(1, 1)
    print("Estadísticas jugador-partido:", estad_jugador)

    estad_equipo = estad.obtener_estadisticas_de_todos_jugadores_por_id_partido(1, 3)
    print("Estadísticas de jugadores del equipo en partido:", estad_equipo)

    estad_partido = estad.obtener_estadisticas_por_jugador(2)
    print("Estadísticas del partido:", estad_partido)


if __name__ == "__main__":
    pruebas()
