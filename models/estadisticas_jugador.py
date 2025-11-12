from models.base_model import BaseModel as BM
from bd.conexion import obtener_conexion

class EstadisticasJugador(BM):
    tabla = "estadisticas_jugador"

    def __init__(self, partido_id=None, jugador_id=None, goles=0, asistencias=0,
                 tarjetas_amarillas=0, tarjetas_rojas=0, minutos_jugados=0, calificacion=0.0):

        self.partido_id = partido_id
        self.jugador_id = jugador_id
        self.goles = goles
        self.asistencias = asistencias
        self.tarjetas_amarillas = tarjetas_amarillas
        self.tarjetas_rojas = tarjetas_rojas
        self.minutos_jugados = minutos_jugados
        self.calificacion = calificacion

    # Crear estadística
    def crear_estadistica(self):
        BM.crear("estadisticas_jugador", self.__dict__)

    # Listar todas
    def listar_estadisticas(self):
        estadisticas = BM.obtener_todos(self.tabla)
        return estadisticas

    # Editar
    def editar_estadistica(self, id_estadistica):
        BM.actualizar(id_estadistica, self.__dict__)

    # Eliminar
    def eliminar_estadistica(self, id_estadistica):
        BM.eliminar(id_estadistica)

    # Obtener estadísticas de un jugador específico
    def obtener_estadisticas_por_jugador(self, jugador_id):
        conn = obtener_conexion()
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM {self.tabla} WHERE jugador_id = ?", (jugador_id,))
        resultado = cur.fetchall()
        conn.close()
        return resultado
    
    def obtener_estadisticas_de_jugador_por_id_partido(self, id_partido, id_jugador):
        sql = "SELECT * FROM estadisticas_jugador WHERE partido_id = ? AND jugador_id = ?"
        return BM.consulta_general(sql, (id_partido, id_jugador))

    def obtener_estadisticas_de_todos_jugadores_por_id_partido(self, id_partido, id_jugador):
        sql = "SELECT * FROM estadisticas_jugador WHERE partido_id = ? AND jugador_id = ?"
        return BM.consulta_general(sql, (id_partido, id_jugador))
