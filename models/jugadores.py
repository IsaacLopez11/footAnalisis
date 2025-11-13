from models.base_model import BaseModel as BM

class Jugador(BM):
    tabla = "jugadores"

    def __init__(self,id=None, nombre=None, edad=None, posicion=None, equipo_id=None):
        self.id = id
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

    def obtener_jugador_por_id(self, id):
        return BM.obtener_por_id(self.tabla, id)


    def listar_por_equipo(self, id_equipo):
        sql = "SELECT * FROM jugadores WHERE equipo_id = ?"
        return BM.consulta_general(sql, (id_equipo,))

    def obtener_atributos(self, id_jugador):
        sql = "SELECT * FROM atributos_jugador WHERE jugador_id = ?"
        return BM.consulta_general(sql, (id_jugador,))

    def obtener_estadisticas(self, id_jugador):
        sql = "SELECT * FROM estadisticas_jugador WHERE jugador_id = ?"
        return BM.consulta_general(sql, (id_jugador,))

    def get_nombre(self, jugador_id):
            # Aquí recuperas el nombre desde la base de datos
            jugador = self.obtener_por_id(jugador_id)
            return jugador["nombre"] if jugador else f"Jugador {jugador_id}"
    
    