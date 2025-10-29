from bd.conexion import obtener_conexion

def inicializar_bd():
    conn = obtener_conexion()
    cursor = conn.cursor()

    # Tabla equipos
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS equipos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL
        )
    """)

    # Tabla jugadores
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS jugadores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            posicion TEXT NOT NULL,
            habilidad INTEGER NOT NULL,
            equipo_id INTEGER,
            FOREIGN KEY(equipo_id) REFERENCES equipos(id)
        )
    """)

    conn.commit()
    conn.close()
def guardar_equipo(nombre):
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO equipos (nombre) VALUES (?)", (nombre,))
    conn.commit()
    conn.close()

def obtener_equipos():
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nombre FROM equipos")
    equipos = cursor.fetchall()
    conn.close()
    return equipos

def guardar_jugador(nombre, posicion, habilidad, equipo_id):
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO jugadores (nombre, posicion, habilidad, equipo_id)
        VALUES (?, ?, ?, ?)
    """, (nombre, posicion, habilidad, equipo_id))
    conn.commit()
    conn.close()

def obtener_jugadores(equipo_id):
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT id, nombre, posicion, habilidad FROM jugadores
        WHERE equipo_id = ?
    """, (equipo_id,))
    jugadores = cursor.fetchall()
    conn.close()
    return jugadores
