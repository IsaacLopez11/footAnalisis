import tkinter as tk
from tkinter import ttk, messagebox
from models.ligas import Liga
from models.equipo import Equipo
from models.jugadores import Jugador
from models.partido import Partido
from models.estadisticas_jugador import EstadisticasJugador
import analisis_estadisticas.analisis_basico as ab


class Interfaz:
    def __init__(self, root):
        self.root = root
        self.root.title("FootAnalisis - Sistema de Gestión y Estadísticas")
        self.root.geometry("1000x650")
        self.root.config(bg="#f9fafb")

        # --- MENÚ LATERAL ---
        self.menu_frame = tk.Frame(root, bg="#1f2937", width=220)
        self.menu_frame.pack(side="left", fill="y")

        # --- CONTENEDOR PRINCIPAL ---
        self.main_frame = tk.Frame(root, bg="#f9fafb")
        self.main_frame.pack(side="right", expand=True, fill="both")

        # --- BOTONES DEL MENÚ ---
        opciones_menu = [
            ("🏠 Menú Principal", self.mostrar_home),
            ("🏆 Ligas", self.mostrar_ligas),
            ("⚽ Equipos", self.mostrar_equipos),
            ("👟 Jugadores", self.mostrar_jugadores),
            ("📊 Análisis", self.mostrar_analisis),
        ]

        for texto, comando in opciones_menu:
            tk.Button(
                self.menu_frame, text=texto, font=("Arial", 12, "bold"),
                bg="#374151", fg="white", relief="flat", activebackground="#2563eb",
                activeforeground="white", command=comando, pady=12
            ).pack(fill="x", padx=15, pady=8)

        # Mostrar pantalla de inicio
        self.mostrar_home()

    # -------------------------------------------------------------------------
    # UTILIDADES
    # -------------------------------------------------------------------------
    def limpiar_main(self):
        """Limpia la vista principal antes de cambiar de pantalla"""
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    # -------------------------------------------------------------------------
    # PANTALLAS
    # -------------------------------------------------------------------------
    def mostrar_home(self):
        self.limpiar_main()
        tk.Label(
            self.main_frame,
            text="🏟️ Bienvenido a FootAnalisis",
            font=("Arial", 22, "bold"),
            bg="#f9fafb",
            fg="#111827"
        ).pack(pady=40)

        tk.Label(
            self.main_frame,
            text="Sistema de gestión y análisis futbolístico",
            font=("Arial", 14),
            bg="#f9fafb"
        ).pack(pady=10)

    # -------------------------------------------------------------------------
    def mostrar_ligas(self):
        self.limpiar_main()
        tk.Label(self.main_frame, text="🏆 Ligas Registradas", font=("Arial", 18, "bold"), bg="#f9fafb").pack(pady=15)

        tree = ttk.Treeview(self.main_frame, columns=("id", "nombre", "temporada"), show="headings", height=20)
        tree.heading("id", text="ID")
        tree.heading("nombre", text="Nombre")
        tree.heading("temporada", text="Temporada Actual")

        tree.pack(expand=True, fill="both", padx=20, pady=10)

        try:
            ligas = Liga().listar_ligas()
            for l in ligas:
                tree.insert("", "end", values=(l["id"], l["nombre"], l["temporada_actual"]))
        except Exception as e:
            messagebox.showerror("Error", f"No se pudieron cargar las ligas.\n{e}")

    # -------------------------------------------------------------------------
    def mostrar_equipos(self):
        self.limpiar_main()
        tk.Label(self.main_frame, text="⚽ Equipos", font=("Arial", 18, "bold"), bg="#f9fafb").pack(pady=15)

        tree = ttk.Treeview(self.main_frame, columns=("id", "nombre", "liga"), show="headings", height=20)
        tree.heading("id", text="ID")
        tree.heading("nombre", text="Nombre")
        tree.heading("liga", text="Liga ID")
        tree.pack(expand=True, fill="both", padx=20, pady=10)

        try:
            equipos = Equipo().listar_equipos()
            for eq in equipos:
                tree.insert("", "end", values=(eq["id"], eq["nombre"], eq["liga_id"]))
        except Exception as e:
            messagebox.showerror("Error", f"No se pudieron cargar los equipos.\n{e}")

    # -------------------------------------------------------------------------
    def mostrar_jugadores(self):
        self.limpiar_main()
        tk.Label(self.main_frame, text="👟 Jugadores", font=("Arial", 18, "bold"), bg="#f9fafb").pack(pady=15)

        tree = ttk.Treeview(self.main_frame, columns=("id", "nombre", "posicion", "equipo"), show="headings", height=20)
        tree.heading("id", text="ID")
        tree.heading("nombre", text="Nombre")
        tree.heading("posicion", text="Posición")
        tree.heading("equipo", text="Equipo ID")
        tree.pack(expand=True, fill="both", padx=20, pady=10)

        try:
            jugadores = Jugador().listar_jugadores()
            for j in jugadores:
                tree.insert("", "end", values=(j["id"], j["nombre"], j["posicion"], j["equipo_id"]))
        except Exception as e:
            messagebox.showerror("Error", f"No se pudieron cargar los jugadores.\n{e}")

    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------
    # ------------------------
# INTERFAZ
# ------------------------
    def mostrar_analisis(self):
        self.limpiar_main()
        
        tk.Label(
            self.main_frame,
            text="📊 Análisis de Rendimiento de Jugadores",
            font=("Arial", 18, "bold"),
            bg="#f9fafb"
        ).pack(pady=25)

        descripcion = (
            "En esta sección podrás analizar los datos básicos y por 90 minutos de los jugadores:\n"
            "- Goleadores\n"
            "- Asistencias\n"
            "- Minutos Jugados\n"
            "- Calificación\n"
            "- Tarjetas Amarillas y Rojas\n"
            "Haz clic en el botón correspondiente para generar el gráfico."
        )
        tk.Label(self.main_frame, text=descripcion, font=("Arial", 12), bg="#f9fafb").pack(pady=10)

        # ------------------------
        # BOTONES ESTADÍSTICAS TOTALES
        # ------------------------
        tk.Button(
            self.main_frame,
            text="Goleadores Totales",
            bg="#2563eb", fg="white", font=("Arial", 13, "bold"),
            relief="flat", padx=15, pady=8,
            command=self.ejecutar_analisis_goleadores
        ).pack(pady=5)

        tk.Button(
            self.main_frame,
            text="Asistencias Totales",
            bg="#10b981", fg="white", font=("Arial", 13, "bold"),
            relief="flat", padx=15, pady=8,
            command=self.ejecutar_analisis_asistencias
        ).pack(pady=5)

        tk.Button(
            self.main_frame,
            text="Minutos Jugados Totales",
            bg="#f59e0b", fg="white", font=("Arial", 13, "bold"),
            relief="flat", padx=15, pady=8,
            command=self.ejecutar_analisis_minutos
        ).pack(pady=5)

        tk.Button(
            self.main_frame,
            text="Calificación Media / Tarjetas",
            bg="#ef4444", fg="white", font=("Arial", 13, "bold"),
            relief="flat", padx=15, pady=8,
            command=self.ejecutar_analisis_calificacion
        ).pack(pady=5)

        # ------------------------
        # BOTONES ESTADÍSTICAS POR 90 MINUTOS
        # ------------------------
        tk.Label(self.main_frame, text="--- Estadísticas por 90 Minutos ---", font=("Arial", 12, "bold"), bg="#f9fafb").pack(pady=15)

        tk.Button(
            self.main_frame,
            text="Goleadores /90 Minutos",
            bg="#1d4ed8", fg="white", font=("Arial", 12, "bold"),
            relief="flat", padx=15, pady=6,
            command=self.ejecutar_analisis_goleadores_90
        ).pack(pady=5)

        tk.Button(
            self.main_frame,
            text="Asistencias /90 Minutos",
            bg="#059669", fg="white", font=("Arial", 12, "bold"),
            relief="flat", padx=15, pady=6,
            command=self.ejecutar_analisis_asistencias_90
        ).pack(pady=5)

        tk.Button(
            self.main_frame,
            text="Tarjetas Amarillas /90 Minutos",
            bg="#b45309", fg="white", font=("Arial", 12, "bold"),
            relief="flat", padx=15, pady=6,
            command=self.ejecutar_analisis_tarjetas_amarillas_90
        ).pack(pady=5)

        tk.Button(
            self.main_frame,
            text="Tarjetas Rojas /90 Minutos",
            bg="#b91c1c", fg="white", font=("Arial", 12, "bold"),
            relief="flat", padx=15, pady=6,
            command=self.ejecutar_analisis_tarjetas_rojas_90
        ).pack(pady=5)


    # ------------------------
    # FUNCIONES ESTADÍSTICAS TOTALES
    # ------------------------
    def ejecutar_analisis_goleadores(self):
        jugadores = Jugador().listar_jugadores()
        jugadores_dict = {j['id']: j['nombre'] for j in jugadores}
        estadisticas = EstadisticasJugador().listar_estadisticas()
        goleadores = ab.lista_goleadores(estadisticas)
        goleadores_nombres = [(jugadores_dict.get(jid, f"Jugador {jid}"), g) for jid, g in goleadores]
        ab.graficar_barras(goleadores_nombres[:10], "Goleadores Totales", "Goles", color='green')


    def ejecutar_analisis_asistencias(self):
        jugadores = Jugador().listar_jugadores()
        jugadores_dict = {j['id']: j['nombre'] for j in jugadores}
        estadisticas = EstadisticasJugador().listar_estadisticas()
        asistencias = ab.lista_asistencias(estadisticas)
        asistencias_nombres = [(jugadores_dict.get(jid, f"Jugador {jid}"), a) for jid, a in asistencias]
        ab.graficar_barras(asistencias_nombres[:10], "Asistencias Totales", "Asistencias", color='blue')


    def ejecutar_analisis_minutos(self):
        jugadores = Jugador().listar_jugadores()
        jugadores_dict = {j['id']: j['nombre'] for j in jugadores}
        estadisticas = EstadisticasJugador().listar_estadisticas()
        minutos = ab.lista_minutos(estadisticas)
        minutos_nombres = [(jugadores_dict.get(jid, f"Jugador {jid}"), m) for jid, m in minutos]
        ab.graficar_barras(minutos_nombres[:10], "Minutos Jugados Totales", "Minutos", color='orange')


    def ejecutar_analisis_calificacion(self):
        jugadores = Jugador().listar_jugadores()
        jugadores_dict = {j['id']: j['nombre'] for j in jugadores}
        estadisticas = EstadisticasJugador().listar_estadisticas()
        calificaciones = ab.lista_calificaciones(estadisticas)
        calificaciones_nombres = [(jugadores_dict.get(jid, f"Jugador {jid}"), c) for jid, c in calificaciones]
        ab.graficar_barras(calificaciones_nombres[:10], "Calificación Media", "Calificación", color='purple')
        
        # Tarjetas
        amarillas, rojas = ab.lista_tarjetas(estadisticas)
        amarillas_nombres = [(jugadores_dict.get(jid, f"Jugador {jid}"), t) for jid, t in amarillas]
        rojas_nombres = [(jugadores_dict.get(jid, f"Jugador {jid}"), t) for jid, t in rojas]
        ab.graficar_barras(amarillas_nombres[:10], "Tarjetas Amarillas Totales", "Cantidad", color='yellow')
        ab.graficar_barras(rojas_nombres[:10], "Tarjetas Rojas Totales", "Cantidad", color='red')


    # ------------------------
    # FUNCIONES ESTADÍSTICAS POR 90 MINUTOS
    # ------------------------
    def ejecutar_analisis_goleadores_90(self):
        jugadores = Jugador().listar_jugadores()
        jugadores_dict = {j['id']: j['nombre'] for j in jugadores}
        estadisticas = EstadisticasJugador().listar_estadisticas()
        goleadores_90 = ab.lista_goleadores_por_90(estadisticas)
        goleadores_90_nombres = [(jugadores_dict.get(jid, f"Jugador {jid}"), g) for jid, g in goleadores_90]
        ab.graficar_barras(goleadores_90_nombres[:10], "Goleadores /90 Minutos", "Goles/90", color='green')


    def ejecutar_analisis_asistencias_90(self):
        jugadores = Jugador().listar_jugadores()
        jugadores_dict = {j['id']: j['nombre'] for j in jugadores}
        estadisticas = EstadisticasJugador().listar_estadisticas()
        asistencias_90 = ab.lista_asistencias_por_90(estadisticas)
        asistencias_90_nombres = [(jugadores_dict.get(jid, f"Jugador {jid}"), a) for jid, a in asistencias_90]
        ab.graficar_barras(asistencias_90_nombres[:10], "Asistencias /90 Minutos", "Asistencias/90", color='blue')


    def ejecutar_analisis_tarjetas_amarillas_90(self):
        jugadores = Jugador().listar_jugadores()
        jugadores_dict = {j['id']: j['nombre'] for j in jugadores}
        estadisticas = EstadisticasJugador().listar_estadisticas()
        amarillas_90 = ab.lista_tarjetas_amarillas_por_90(estadisticas)
        amarillas_90_nombres = [(jugadores_dict.get(jid, f"Jugador {jid}"), t) for jid, t in amarillas_90]
        ab.graficar_barras(amarillas_90_nombres[:10], "Tarjetas Amarillas /90 Minutos", "Amarillas/90", color='yellow')


    def ejecutar_analisis_tarjetas_rojas_90(self):
        jugadores = Jugador().listar_jugadores()
        jugadores_dict = {j['id']: j['nombre'] for j in jugadores}
        estadisticas = EstadisticasJugador().listar_estadisticas()
        rojas_90 = ab.lista_tarjetas_rojas_por_90(estadisticas)
        rojas_90_nombres = [(jugadores_dict.get(jid, f"Jugador {jid}"), t) for jid, t in rojas_90]
        ab.graficar_barras(rojas_90_nombres[:10], "Tarjetas Rojas /90 Minutos", "Rojas/90", color='red')


# -----------------------------------------------------------------------------
# EJECUCIÓN DIRECTA
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = Interfaz(root)
    root.mainloop()
