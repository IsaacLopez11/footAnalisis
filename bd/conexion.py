import sqlite3

DB_PATH = "data/footmanager.db"

def obtener_conexion():
    conn = sqlite3.connect(DB_PATH)
    return conn
