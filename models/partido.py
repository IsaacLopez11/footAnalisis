from models.base_model import BaseModel as BM

class Partido(BM):
    tabla = "partidos"

    def __init__(self, fecha=None, equipo_local_id=None, equipo_visitante_id=None,
                 goles_local=None, goles_visitante=None, liga_id=None, jugado=False):

        self.fecha = fecha
        self.equipo_local_id = equipo_local_id
        self.equipo_visitante_id = equipo_visitante_id
        self.goles_local = goles_local
        self.goles_visitante = goles_visitante
        self.liga_id = liga_id
        self.jugado = jugado

    # Crear partido
    def crear_partido(self):
        BM.crear(self.__dict__)

    # Listar partidos
    def listar_partidos(self):
        partidos = BM.obtener_todos(self.tabla)
        return partidos

    # Editar partido
    def editar_partido(self, id_partido):
        BM.actualizar(id_partido, self.__dict__)

    # Eliminar partido
    def eliminar_partido(self, id_partido):
        BM.eliminar(id_partido)

    def obtener_partido_por_id(self, id_partido):
        return BM.obtener_por_id(self.tabla, id_partido)
