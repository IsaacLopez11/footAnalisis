# models/equipo.py
from models.base_model import BaseModel as BM

class Equipo(BM):
    tabla = "equipos"

    def __init__(self,  nombre=None, ciudad=None, estadio=None, capacidad_estadio=None, liga_id=None):
        super().__init__()  # nombre de la tabla
        self.id= None
        self.nombre = nombre
        self.ciudad = ciudad
        self.estadio = estadio
        self.capacidad_estadio = capacidad_estadio
        self.liga_id = liga_id

    def listar_equipos(self):
        equipos = BM.obtener_todos(self.tabla)
        return equipos

    def crear_equipo(self):
        BM.crear(self.tabla,self.__dict__)
    
    def eliminar_equipo(self, id_equipo):
        BM.eliminar(id_equipo)

    def editar_equipo(self, id_equipo):
        BM.actualizar(id_equipo, self.__dict__)

    def obtener_equipo_por_id(self, id):
        return BM.obtener_por_id(self.tabla, id)

    def listar_jugadores(self):
        return 0
    

