import sqlite3
import pandas as pd

DB_PATH = "data/futbol.db"

def calcular_rendimiento_general():
    """Calcula un índice de rendimiento por jugador combinando estadísticas y atributos."""
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query("""
        SELECT j.nombre,
               e.nombre AS equipo,
               (es.goles * 5 + es.asistencias * 3 + es.pases_completados * 0.05
                + a.tiro * 0.4 + a.velocidad * 0.3 + a.pase * 0.3) AS rendimiento
        FROM jugadores j
        JOIN equipos e ON j.equipo_id = e.id
        JOIN estadisticas_jugadores es ON j.id = es.jugador_id
        JOIN atributos_jugador a ON j.id = a.jugador_id
    """, conn)
    conn.close()

    print(df.sort_values(by="rendimiento", ascending=False))

def comparar_jugadores(jugador1, jugador2):
    """Compara dos jugadores por rendimiento."""
    conn = sqlite3.connect(DB_PATH)
    query = f"""
        SELECT j.nombre, e.nombre AS equipo,
               (es.goles * 5 + es.asistencias * 3 + a.tiro * 0.4 + a.pase * 0.3 + a.velocidad * 0.3) AS rendimiento
        FROM jugadores j
        JOIN equipos e ON j.equipo_id = e.id
        JOIN estadisticas_jugadores es ON j.id = es.jugador_id
        JOIN atributos_jugador a ON j.id = a.jugador_id
        WHERE j.nombre IN (?, ?)
    """
    df = pd.read_sql_query(query, conn, params=(jugador1, jugador2))
    conn.close()

    print(df)
