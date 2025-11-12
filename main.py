# =========================
#   FOOTMANAGER v0.1
# =========================
from models.equipo import Equipo
from models.jugadores import Jugador
from models.ligas import Liga
from models.equipo import Equipo
from models.jugadores import Jugador
from models.atributos import AtributosJugador
from controladores.partido import jugar_partido
from datetime import date
from models.partido import Partido
from controladores.partido import jugar_partido
# === Ejemplo de uso ===
if __name__ == "__main__":
    
   # Crear y simular un partido
    resumen = jugar_partido(equipo_local_id=1, equipo_visitante_id=2, fecha="2025-11-12", liga_id=1)

    # Ver resultados
    print("Resultado final:", resumen["resultado"])
    print("Estadísticas jugadores:", resumen["estadisticas_jugadores"])
    print("Estadísticas del partido:", resumen["estadisticas_partido"])


    # equipo = Equipo().listar_equipos()
    # print(equipo)
    # equipo = Equipo().obtener_equipo_por_id(2)
    # print(equipo)
    # print(equipo['id'])
    # equipo_jugar = Equipo()
    # equipo_jugar.id = equipo['id']
    # print(equipo_jugar.id)
    # equipo_jugar.listar_jugadores(2)
    # print( )
    #Instancia interfaz
    # interfaz = Interfaz()
    # interfaz.menu()
    # Creamos jugadores
#     j1 = Jugador("Luis", "DC", 75)
#     j2 = Jugador("Carlos", "MC", 68)
#     j3 = Jugador("Andrés", "PT", 70)
#     j4 = Jugador("Felipe", "DF", 72)

#     # Creamos equipo y agregamos jugadores
#     equipo1 = Equipo("Club Atlético Python")
#     equipo1.agregar_jugador(j1)
#     equipo1.agregar_jugador(j2)
#     equipo1.agregar_jugador(j3)
#     equipo1.agregar_jugador(j4)

#     # Mostramos plantilla


#  # Creamos jugadores
#     j5 = Jugador("Adrían", "DC", 75)
#     j6 = Jugador("Enrique", "MC", 68)
#     j7 = Jugador("Juan", "PT", 70)
#     j8 = Jugador("David", "DF", 72)

#     # Creamos equipo y agregamos jugadores
#     equipo2 = Equipo("Club Atlético JS")
#     equipo2.agregar_jugador(j5)
#     equipo2.agregar_jugador(j6)
#     equipo2.agregar_jugador(j7)
#     equipo2.agregar_jugador(j8)

#     # Mostramos plantilla
#     # equipo2.mostrar_plantilla()

#     # partido = Partido(equipo1=equipo1,equipo2=equipo2)
#     # partido.simular_partido()
#     inicializar_bd()

#     guardar_equipo("Club Python")
#     equipos = obtener_equipos()
#     print("Equipos:", equipos)

#     primer_equipo_id = equipos[0][0]
#     guardar_jugador("Luis", "DC", 80, primer_equipo_id)

#     jugadores = obtener_jugadores(primer_equipo_id)
#     print("Jugadores:", jugadores)
#      equipo = Equipo(nombre="Brisas del Lago", ciudad="Punta Gorda", estadio="La cancha del Liceo", capacidad_estadio=1000, liga_id=1)
#      equipo = Equipo()
# #      equipo.listar_equipos()
#      equipo.obtener_equipo_por_id(1)


#      # nuevo = Jugador("Messi", 36, "Delantero", 1)
#      nuevo = Jugador("Messi", 36, "Delantero", 1)
#      # nuevo.crear_jugador()
#      actualizado = Jugador("Lionel Messi", 36, "Delantero", 1)
#      actualizado.editar_jugador(2)  # ahora debería funcionar

     # Crear una liga
     # nueva = Liga("Primera División", 2025)
     # nueva.crear_liga()

#      # Listar ligas
#      ligas = Liga()
#      ligas.listar_ligas()

#      # Editar liga
#      # actualizada = Liga("Primera División", 2026)
#      # actualizada.editar_liga(2)

#      # Eliminar liga
#      # ligas.eliminar_liga(1)


# # --- 1️⃣ Crear algunos equipos de ejemplo ---
#      equipo1 = Equipo(nombre="Brisas del Lago", ciudad="Punta Gorda",
#                          estadio="La Cancha del Liceo", capacidad_estadio=1000, liga_id=1)
#      # equipo1.crear_equipo()

#      equipo2 = Equipo(nombre="Los Halcones", ciudad="Ciudad Alta",
#                          estadio="Estadio Central", capacidad_estadio=1200, liga_id=1)
#      # equipo2.crear_equipo()

#      # --- 2️⃣ Crear jugadores para cada equipo ---
#      jugador1 = Jugador(nombre="Juan Perez", edad=22, posicion="Delantero", equipo_id=1)
#      # jugador1.crear_jugador()

#      jugador2 = Jugador(nombre="Carlos Gomez", edad=24, posicion="Mediocampo", equipo_id=2)
#      # jugador2.crear_jugador()

#      # --- 3️⃣ Crear atributos de los jugadores ---
#      atributos1 = AtributosJugador(
#           jugador_id=1,
#           desmarques=80, remate=90, tiros_lejanos=70,
#           tecnica=85, pase=80, 
#           marcaje=50, entradas=40,
#           colocacion=70, vision=75, agresividad=60,
#           agarre=0, despeje=0, mando_area=0
#      )
#      atributos1.crear_atributos()

#      atributos2 = AtributosJugador(
#           jugador_id=2,
#           desmarques=75, remate=70, tiros_lejanos=65,
#           tecnica=88, pase=85, 
#           marcaje=60, entradas=55,
#           colocacion=80, vision=82, agresividad=70,
#           agarre=0, despeje=0, mando_area=0
#      )
#      atributos2.crear_atributos()

#      # --- 4️⃣ Simular un partido ---
#      fecha_partido = date.today()
#      jugar_partido(equipo_local_id=1, equipo_visitante_id=2, fecha=fecha_partido, liga_id=1)

#      print("Partido simulado y estadísticas generadas.")