from models.base_model import BaseModel as BM

class Liga(BM):
    tabla = "ligas"

    def __init__(self, nombre=None, temporada_actual=None):
        self.nombre = nombre
        self.temporada_actual = temporada_actual

    # Crear liga
    def crear_liga(self):
        BM.crear(self.tabla, self.__dict__)

    # Listar todas las ligas
    def listar_ligas(self):
        ligas = BM.obtener_todos(self.tabla)
        return ligas

    # Editar liga por ID
    def editar_liga(self, id_liga):
        BM.actualizar(self.tabla,id_liga, self.__dict__)

    # Eliminar liga por ID
    def eliminar_liga(self, id_liga):
        BM.eliminar(self.tabla,id_liga)

    def listar_equipos_por_liga(self, liga_id):
        sql = "SELECT * FROM equipos WHERE liga_id = ?"
        return BM.consulta_general(sql, (liga_id,))

    
    def obtener_liga_por_id(self, id_liga):
        sql = "SELECT * FROM ligas WHERE liga_id = ?"
        return BM.consulta_general(sql, (id_liga,))

