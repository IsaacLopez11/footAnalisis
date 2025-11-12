# models/base_model.py
from bd.conexion import obtener_conexion

class BaseModel:
    tabla = ""
    campos = []

    def crear(cls, datos: dict):
        """Inserta un nuevo registro en la tabla."""
        conn = obtener_conexion()
        cur = conn.cursor()

        columnas = ", ".join(datos.keys())
        valores = tuple(datos.values())
        placeholders = ", ".join(["?"] * len(datos))

        query = f"INSERT INTO {cls} ({columnas}) VALUES ({placeholders})"
        cur.execute(query, valores)

        conn.commit()
        conn.close()
        print(f"Registro creado en '{cls}' correctamente.")
    
    
    def obtener_todos(cls):
        """Devuelve todos los registros de la tabla."""
        conn = obtener_conexion()
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM {cls}")
        registros = cur.fetchall()
        conn.close()
        return [dict(registro) for registro in registros]

    
    def obtener_por_id(tabla, id):
        """Devuelve un registro específico por ID."""
        conn = obtener_conexion()
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM {tabla} WHERE id = ?", (id,))
        registro = cur.fetchone()
        conn.close()
        return dict(registro) if registro else None

    
    def actualizar(cls, id, datos:dict):
        """Actualiza un registro existente."""
        conn = obtener_conexion()
        cur = conn.cursor()

        # Filtrar datos que sean None o que no existan en la tabla
        cur.execute(f"PRAGMA table_info({cls})")
        columnas_tabla = [col[1] for col in cur.fetchall()]
        datos_filtrados = {k: v for k, v in datos.items() if k in columnas_tabla}

        set_clause = ", ".join([f"{campo} = ?" for campo in datos_filtrados.keys()])
        valores = tuple(datos_filtrados.values()) + (id,)

        query = f"UPDATE {cls} SET {set_clause} WHERE id = ?"
        cur.execute(query, valores)

        conn.commit()
        conn.close()
        print(f"Registro con ID {id} actualizado en {cls}.")

        
    def eliminar(cls, id):
        """Elimina un registro por ID."""
        conn = obtener_conexion()
        cur = conn.cursor()
        cur.execute(f"DELETE FROM {cls} WHERE id = ?", (id,))
        conn.commit()
        conn.close()
        print(f"Registro con ID {id} eliminado de {cls}.")

    def consulta_general(sql):
        """Consulta general."""
        conn = obtener_conexion()
        cur = conn.cursor()
        cur.execute(sql)
        resultados = cur.fetchall()
        conn.commit()
        conn.close()
        print("Consulta realizada")
        return [dict(fila) for fila in resultados]  
