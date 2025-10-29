from bd.conexion import obtener_conexion
from models.jugador import Jugador

class Equipo:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre
        self.jugadores = self.cargar_jugadores()

    def cargar_jugadores(self):
        conn = obtener_conexion()
        cursor = conn.cursor()
        cursor.execute("SELECT id, nombre, posicion, habilidad FROM jugadores WHERE equipo_id = ?", (self.id,))
        jugadores = [Jugador(id=j[0], nombre=j[1], posicion=j[2], habilidad=j[3]) for j in cursor.fetchall()]
        conn.close()
        return jugadores

    def __str__(self):
        return f"{self.nombre} ({len(self.jugadores)} jugadores)"
