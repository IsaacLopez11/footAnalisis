from models.jugador import Jugador
from models.partido import Partido
from models.equipo import Equipo


class Interfaz:
    def __init__(self):
        self.equipos = []

    def menu(self):
        while True:
            print("\n=== ⚽ FOOTMANAGER v0.2 ===")
            print("1. Crear equipo")
            print("2. Agregar jugador a un equipo")
            print("3. Eliminar jugador de un equipo")
            print("4. Editar jugador de un equipo")
            print("5. Mostrar plantillas")
            print("6. Simular partido")
            print("7. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.crear_equipo()
            elif opcion == "2":
                self.agregar_jugador()
            elif opcion == "3":
                self.eliminar_jugador()
            elif opcion == "4":
                self.editar_jugador()
            elif opcion == "5":
                self.mostrar_plantillas()
            elif opcion == "6":
                self.simular_partido()
            elif opcion == "7":
                print("👋 Saliendo del juego...")
                break
            else:
                print("⚠️ Opción no válida, intente de nuevo.")

    def crear_equipo(self):
        nombre = input("Nombre del nuevo equipo: ")
        equipo = Equipo(nombre)
        self.equipos.append(equipo)
        print(f"✅ Equipo '{nombre}' creado con éxito.")

    def seleccionar_equipo(self):
        if not self.equipos:
            print("⚠️ No hay equipos creados aún.")
            return None
        print("\nEquipos disponibles:")
        for i, eq in enumerate(self.equipos, start=1):
            print(f"{i}. {eq.nombre}")
        try:
            idx = int(input("Seleccione un equipo: ")) - 1
            return self.equipos[idx]
        except (ValueError, IndexError):
            print("⚠️ Selección inválida.")
            return None
        
    def seleccionar_jugador(self, equipo):
        if not equipo.jugadores:
            print("⚠️ No hay jugadores en el equipo.")
            return None
        print("\Jugadores disponibles:")
        for i, j in enumerate(equipo.jugadores, start=1):
            print(f"{i}. {j.nombre} - {j.posicion}")
        try:
            idx = int(input("Seleccione un jugador: ")) - 1
            return equipo.jugadores[idx]
        except (ValueError, IndexError):
            print("⚠️ Selección inválida.")
            return None


    def agregar_jugador(self):
        equipo = self.seleccionar_equipo()
        if not equipo:
            return
        nombre = input("Nombre del jugador: ")
        posicion = input("Posición (PT, DF, MC, DC): ").upper()
        try:
            habilidad = int(input("Habilidad (0-100): "))
        except ValueError:
            print("⚠️ Valor de habilidad inválido.")
            return
        jugador = Jugador(nombre, posicion, habilidad)
        equipo.agregar_jugador(jugador)
        print(f"✅ Jugador {nombre} agregado a {equipo.nombre}.")

    def editar_jugador(self):
        equipo = self.seleccionar_equipo()
        jugador = self.seleccionar_jugador(equipo)
        print(f"\nEditando jugador: {jugador.nombre} ({jugador.posicion}, {jugador.habilidad})")

        nombre = input("Nuevo nombre (deja vacío para mantener el actual): ") or jugador.nombre
        posicion = input("Nueva posición (PT, DF, MC, DC o vacío para mantener): ").upper() or jugador.posicion
        try:
            habilidad_input = input("Nueva habilidad (0-100 o vacío para mantener): ")
            habilidad = int(habilidad_input) if habilidad_input else jugador.habilidad
        except ValueError:
            print("⚠️ Valor de habilidad inválido, se mantiene la actual.")
            habilidad = jugador.habilidad
        jugador.editar_jugador(nombre, posicion, habilidad)
        print(f"✅ {jugador.nombre} fue actualizado correctamente.")

    def eliminar_jugador(self):
        equipo = self.seleccionar_equipo()
        if not equipo:
            return
        nombre_jugador = input("Nombre del jugador a eliminar: ")
        equipo.eliminar_jugador(nombre_jugador)

    def mostrar_plantillas(self):
        for equipo in self.equipos:
            equipo.cargar_jugadores()

    def simular_partido(self):
        if len(self.equipos) < 2:
            print("⚠️ Debe haber al menos dos equipos para simular un partido.")
            return
        print("\nSeleccione los dos equipos:")
        e1 = self.seleccionar_equipo()
        e2 = self.seleccionar_equipo()
        if e1 and e2 and e1 != e2:
            partido = Partido(e1, e2)
            partido.simular_partido()
        else:
            print("⚠️ Selección inválida para el partido.")
