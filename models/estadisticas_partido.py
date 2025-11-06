from models.base_model import BaseModel as BM

class EstadisticasPartido(BM):
    tabla = "estadisticas_partido"

    def __init__(self, partido_id=None, posesion_local=0, posesion_visitante=0,
                 tiros_local=0, tiros_visitante=0,
                 tiros_puerta_local=0, tiros_puerta_visitante=0,
                 faltas_local=0, faltas_visitante=0,
                 corners_local=0, corners_visitante=0,
                 tarjetas_local=0, tarjetas_visitante=0):

        self.partido_id = partido_id
        self.posesion_local = posesion_local
        self.posesion_visitante = posesion_visitante
        self.tiros_local = tiros_local
        self.tiros_visitante = tiros_visitante
        self.tiros_puerta_local = tiros_puerta_local
        self.tiros_puerta_visitante = tiros_puerta_visitante
        self.faltas_local = faltas_local
        self.faltas_visitante = faltas_visitante
        self.corners_local = corners_local
        self.corners_visitante = corners_visitante
        self.tarjetas_local = tarjetas_local
        self.tarjetas_visitante = tarjetas_visitante

    # CRUD
    def crear_estadistica(self):
        BM.crear(self.__dict__)

    def listar_estadisticas(self):
        estadisticas = BM.obtener_todos(self.tabla)
        print(estadisticas)

    def editar_estadistica(self, id_estadistica):
        BM.actualizar(id_estadistica, self.__dict__)

    def eliminar_estadistica(self, id_estadistica):
        BM.eliminar(id_estadistica)
