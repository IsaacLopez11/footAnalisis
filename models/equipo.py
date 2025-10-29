
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
