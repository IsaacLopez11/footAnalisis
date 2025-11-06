from models.base_model import BaseModel as BM

class AtributosJugador(BM):
    tabla = "atributos_jugador"

    def __init__(self, jugador_id=None,
                 desmarques=None, remate=None, tiros_lejanos=None,   # Ataque
                 tecnica=None, pase=None, tiro_lejano_medio=None,     # Medio
                 marcaje=None, entradas=None,                          # Defensa
                 colocacion=None, vision=None, agresividad=None,       # Mentales
                 agarre=None, despeje=None, mando_area=None):         # Portero

        self.jugador_id = jugador_id

        # Ataque
        self.desmarques = desmarques
        self.remate = remate
        self.tiros_lejanos = tiros_lejanos

        # Medio
        self.tecnica = tecnica
        self.pase = pase
        self.tiro_lejano_medio = tiro_lejano_medio

        # Defensa
        self.marcaje = marcaje
        self.entradas = entradas

        # Mentales
        self.colocacion = colocacion
        self.vision = vision
        self.agresividad = agresividad

        # Portero
        self.agarre = agarre
        self.despeje = despeje
        self.mando_area = mando_area

    # Crear atributos
    def crear_atributos(self):
        BM.crear(self.__dict__)

    # Listar atributos
    def listar_atributos(self):
        atributos = BM.obtener_todos(self.tabla)
        print(atributos)

    # Editar atributos
    def editar_atributos(self, id_atributos):
        BM.actualizar(id_atributos, self.__dict__)

    # Eliminar atributos
    def eliminar_atributos(self, id_atributos):
        BM.eliminar(id_atributos)


    def obtener_por_jugador(self, jugador_id):
        """Devuelve los atributos de un jugador específico."""
        conn = obtener_conexion()
        cur = conn.cursor()

        cur.execute(f"SELECT * FROM {self.tabla} WHERE jugador_id = ?", (jugador_id,))
        registro = cur.fetchone()

        conn.close()
        return registro
