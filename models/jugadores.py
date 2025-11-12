from models.base_model import BaseModel as BM

class Jugador(BM):
    tabla = "jugadores"

    def __init__(self, nombre=None, edad=None, posicion=None, equipo_id=None):
        self.nombre = nombre
        self.edad = edad
        self.posicion = posicion
        self.equipo_id = equipo_id

    # Crear jugador
    def crear_jugador(self):
        BM.crear(self.tabla,self.__dict__)

    # Listar todos los jugadores
    def listar_jugadores(self):
        jugadores = BM.obtener_todos(self.tabla)
        return jugadores

    # Eliminar jugador por ID
    def eliminar_jugador(self, id_jugador):
        BM.eliminar(self.tabla,id_jugador)

    # Editar jugador por ID
    def editar_jugador(self, id_jugador):
        BM.actualizar(self.tabla,id_jugador, self.__dict__)
