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


# class Interfaz:
#     def menu(self):
#         while keyDown != "C":

#             print("Hola desde la interfaz")

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
    equipo1.mostrar_plantilla()


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
    equipo2.mostrar_plantilla()

    partido = Partido(equipo1=equipo1,equipo2=equipo2)
    partido.simular_partido()

