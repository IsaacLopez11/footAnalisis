import sqlite3

DB_PATH = "data/footmanager.db"

def obtener_conexion():
    """Devuelve una conexión nueva a la base de datos con timeout y control de fila."""
    conn = sqlite3.connect(DB_PATH, timeout=10, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn
