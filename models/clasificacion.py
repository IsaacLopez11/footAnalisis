from models.base_model import BaseModel as BM

class Clasificacion(BM):
    tabla = "clasificacion"

    def __init__(self, liga_id=None, equipo_id=None, partidos_jugados=0,
                 ganados=0, empatados=0, perdidos=0,
                 goles_a_favor=0, goles_en_contra=0, puntos=0):

        self.liga_id = liga_id
        self.equipo_id = equipo_id
        self.partidos_jugados = partidos_jugados
        self.ganados = ganados
        self.empatados = empatados
        self.perdidos = perdidos
        self.goles_a_favor = goles_a_favor
        self.goles_en_contra = goles_en_contra
        self.puntos = puntos

    # CRUD
    def crear_clasificacion(self):
        BM.crear(self.__dict__)

    def listar_clasificacion(self):
        clasificacion = BM.obtener_todos(self.tabla)
        print(clasificacion)

    def editar_clasificacion(self, id_clasificacion):
        BM.actualizar(id_clasificacion, self.__dict__)

    def eliminar_clasificacion(self, id_clasificacion):
        BM.eliminar(id_clasificacion)
