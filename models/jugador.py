
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
