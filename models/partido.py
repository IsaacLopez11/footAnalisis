import random


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

