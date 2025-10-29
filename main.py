# =========================
#   FOOTMANAGER v0.1
# =========================
from ui.interfaz_console import Interfaz
from models.jugador import Jugador
from models.partido import Partido
from models.equipo import Equipo
from bd.repositorio import inicializar_bd
from bd.repositorio import inicializar_bd, guardar_equipo, obtener_equipos, guardar_jugador, obtener_jugadores

# === Ejemplo de uso ===
if __name__ == "__main__":
    #Instancia interfaz
    # interfaz = Interfaz()
    # interfaz.menu()
    # Creamos jugadores
    j1 = Jugador("Luis", "DC", 75)
    j2 = Jugador("Carlos", "MC", 68)
    j3 = Jugador("Andrés", "PT", 70)
    j4 = Jugador("Felipe", "DF", 72)

    # Creamos equipo y agregamos jugadores
    equipo1 = Equipo("Club Atlético Python")
    equipo1.agregar_jugador(j1)
    equipo1.agregar_jugador(j2)
    equipo1.agregar_jugador(j3)
    equipo1.agregar_jugador(j4)

    # Mostramos plantilla


 # Creamos jugadores
    j5 = Jugador("Adrían", "DC", 75)
    j6 = Jugador("Enrique", "MC", 68)
    j7 = Jugador("Juan", "PT", 70)
    j8 = Jugador("David", "DF", 72)

    # Creamos equipo y agregamos jugadores
    equipo2 = Equipo("Club Atlético JS")
    equipo2.agregar_jugador(j5)
    equipo2.agregar_jugador(j6)
    equipo2.agregar_jugador(j7)
    equipo2.agregar_jugador(j8)

    # Mostramos plantilla
    # equipo2.mostrar_plantilla()

    # partido = Partido(equipo1=equipo1,equipo2=equipo2)
    # partido.simular_partido()
    inicializar_bd()

    guardar_equipo("Club Python")
    equipos = obtener_equipos()
    print("Equipos:", equipos)

    primer_equipo_id = equipos[0][0]
    guardar_jugador("Luis", "DC", 80, primer_equipo_id)

    jugadores = obtener_jugadores(primer_equipo_id)
    print("Jugadores:", jugadores)

    juego = Interfaz()
    juego.equipos.append(equipo1)
    juego.equipos.append(equipo2)
    juego.menu()
