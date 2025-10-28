# =========================
#   FOOTMANAGER v0.1
# =========================
import random

class Jugador:
    def __init__(self, nombre, posicion, habilidad):
        self.nombre = nombre
        self.posicion = posicion
        self.habilidad = habilidad

    def editar_jugador(self, nombre=None, posicion=None, habilidad=None):
        if nombre:
            self.nombre = nombre
        if posicion:
            self.posicion = posicion
        if habilidad:
            self.habilidad = habilidad


    def __str__(self):
        return f"{self.nombre} - {self.posicion} - {self.habilidad}"


class Equipo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.jugadores = []

    def agregar_jugador(self, jugador):
        self.jugadores.append(jugador)

    def eliminar_jugador(self, jugador):
        if jugador in self.jugadores:
            self.jugadores.remove(jugador)
        else:
            print(f"⚠️ El jugador {jugador.nombre} no está en {self.nombre}.")
            

    def mostrar_plantilla(self):
        print(f"\n=== Plantilla de {self.nombre} ===")
        print(f"{'Nombre':<15} {'Posición':<10} {'Habilidad':<10}")
        print("-" * 35)
        for j in self.jugadores:
            print(f"{j.nombre:<15} {j.posicion:<10} {j.habilidad:<10}")

class Partido:

    def __init__(self, equipo1, equipo2):
        self.equipo1 = equipo1
        self.equipo2 = equipo2


    def simular_partido(self):
        habilidad_a = sum(j.habilidad for j in self.equipo1.jugadores) / len(self.equipo1.jugadores)
        habilidad_b = sum(j.habilidad for j in self.equipo2.jugadores) / len(self.equipo2.jugadores)

        goles_a = random.randint(0, int(habilidad_a // 25))
        goles_b = random.randint(0, int(habilidad_b // 25))

        print(f"\n{self.equipo1.nombre} {goles_a} - {goles_b} {self.equipo2.nombre}")
        if goles_a > goles_b:
            print(f"🏆 ¡{self.equipo1.nombre} gana el partido!")
        elif goles_a < goles_b:
            print(f"🏆 ¡{self.equipo2.nombre} gana el partido!")
        else:
            print("🤝 Empate")


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
            equipo.mostrar_plantilla()

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
    juego = Interfaz()
    juego.equipos.append(equipo1)
    juego.equipos.append(equipo2)
    juego.menu()
