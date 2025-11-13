import tkinter as tk
from tkinter import ttk, messagebox
from analisis_estadisticas.rendimiento_jugadores import EstadisticasJugador
from models.ligas import Liga
from models.equipo import Equipo
from models.jugadores import Jugador
from analisis_estadisticas.analisis_basico import analisis_basico_jugadores as ab


class Interfaz:
    def __init__(self, root):
        self.root = root
        self.root.title("FootAnalisis - Sistema de Gestión y Estadísticas")
        self.root.geometry("1000x650")
        self.root.config(bg="#f9fafb")

        # 🔹 Diccionario para manejar pantallas (frames)
        self.frames = {}

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
                self.menu_frame,
                text=texto,
                font=("Arial", 12, "bold"),
                bg="#374151",
                fg="white",
                relief="flat",
                activebackground="#2563eb",
                activeforeground="white",
                command=comando,
                pady=12
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

    def mostrar_frame(self, nombre):
        """Muestra un frame específico y oculta los demás"""
        self.limpiar_main()
        frame = self.frames[nombre]
        frame.pack(expand=True, fill="both")

    def volver_menu(self, frame_actual):
        """Vuelve al menú principal desde cualquier pantalla"""
        frame_actual.pack_forget()
        self.mostrar_home()

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
    def mostrar_analisis(self):
        """Pantalla de análisis estadístico con botones para todas las métricas"""
        self.limpiar_main()
        frame = tk.Frame(self.main_frame, bg="#f9fafb")
        frame.pack(expand=True, fill="both")
        self.frames["analisis"] = frame

        tk.Label(frame, text="📊 Análisis de Rendimiento de Jugadores",
                font=("Arial", 18, "bold"), bg="#f9fafb").pack(pady=15)

        tk.Label(frame, text="Haz clic en el botón correspondiente para generar cada gráfico",
                font=("Arial", 12), bg="#f9fafb").pack(pady=5)

        # Función interna para obtener estadisticas y diccionario id->nombre
        def obtener_datos():
            jugadores = Jugador().listar_jugadores()
            jugadores_dict = {j['id']: j['nombre'] for j in jugadores}
            estadisticas = EstadisticasJugador().listar_estadisticas()
            return jugadores_dict, estadisticas

        jugadores_dict, estadisticas = obtener_datos()

        # -----------------------
        # Botones para estadísticas generales
        # -----------------------
        tk.Label(frame, text="📈 Estadísticas Generales", font=("Arial", 14, "bold"), bg="#f9fafb").pack(pady=10)

        tk.Button(frame, text="Goleadores", bg="#2563eb", fg="white", font=("Arial", 13, "bold"),
                relief="flat", padx=15, pady=8,
                command=lambda: ab.graficar_barras(
                    [(jugadores_dict.get(jid, f"Jugador {jid}"), g) for jid, g in ab.lista_goleadores(estadisticas)[:10]],
                    "Goleadores", "Goles", color='green')
                ).pack(pady=5)

        tk.Button(frame, text="Asistencias", bg="#10b981", fg="white", font=("Arial", 13, "bold"),
                relief="flat", padx=15, pady=8,
                command=lambda: ab.graficar_barras(
                    [(jugadores_dict.get(jid, f"Jugador {jid}"), a) for jid, a in ab.lista_asistencias(estadisticas)[:10]],
                    "Asistencias", "Asistencias", color='blue')
                ).pack(pady=5)

        tk.Button(frame, text="Minutos Jugados", bg="#f59e0b", fg="white", font=("Arial", 13, "bold"),
                relief="flat", padx=15, pady=8,
                command=lambda: ab.graficar_barras(
                    [(jugadores_dict.get(jid, f"Jugador {jid}"), m) for jid, m in ab.lista_minutos(estadisticas)[:10]],
                    "Minutos Jugados", "Minutos", color='orange')
                ).pack(pady=5)

        tk.Button(frame, text="Calificación Media", bg="#8b5cf6", fg="white", font=("Arial", 13, "bold"),
                relief="flat", padx=15, pady=8,
                command=lambda: ab.graficar_barras(
                    [(jugadores_dict.get(jid, f"Jugador {jid}"), c) for jid, c in ab.lista_calificaciones(estadisticas)[:10]],
                    "Calificación Media", "Calificación", color='purple')
                ).pack(pady=5)

        tk.Button(frame, text="Tarjetas Amarillas", bg="#facc15", fg="black", font=("Arial", 13, "bold"),
                relief="flat", padx=15, pady=8,
                command=lambda: ab.graficar_barras(
                    [(jugadores_dict.get(jid, f"Jugador {jid}"), t) for jid, t in ab.lista_tarjetas(estadisticas)[0][:10]],
                    "Tarjetas Amarillas", "Cantidad", color='yellow')
                ).pack(pady=5)

        tk.Button(frame, text="Tarjetas Rojas", bg="#ef4444", fg="white", font=("Arial", 13, "bold"),
                relief="flat", padx=15, pady=8,
                command=lambda: ab.graficar_barras(
                    [(jugadores_dict.get(jid, f"Jugador {jid}"), t) for jid, t in ab.lista_tarjetas(estadisticas)[1][:10]],
                    "Tarjetas Rojas", "Cantidad", color='red')
                ).pack(pady=5)

    # -----------------------
    # Botones para estadísticas por 90 minutos
    # -----------------------
        tk.Label(frame, text="⏱️ Estadísticas por 90 Minutos", font=("Arial", 14, "bold"), bg="#f9fafb").pack(pady=15)

        tk.Button(frame, text="Goles /90 Minutos", bg="#2563eb", fg="white", font=("Arial", 13, "bold"),
                relief="flat", padx=15, pady=8,
                command=lambda: ab.graficar_barras(
                    [(jugadores_dict.get(jid, f"Jugador {jid}"), g) for jid, g in ab.lista_goleadores_por_90(estadisticas)[:10]],
                    "Goleadores /90", "Goles/90", color='green')
                ).pack(pady=5)

        tk.Button(frame, text="Asistencias /90 Minutos", bg="#10b981", fg="white", font=("Arial", 13, "bold"),
                relief="flat", padx=15, pady=8,
                command=lambda: ab.graficar_barras(
                    [(jugadores_dict.get(jid, f"Jugador {jid}"), a) for jid, a in ab.lista_asistencias_por_90(estadisticas)[:10]],
                    "Asistencias /90", "Asistencias/90", color='blue')
                ).pack(pady=5)

        tk.Button(frame, text="Tarjetas Amarillas /90", bg="#f59e0b", fg="white", font=("Arial", 13, "bold"),
                relief="flat", padx=15, pady=8,
                command=lambda: ab.graficar_barras(
                    [(jugadores_dict.get(jid, f"Jugador {jid}"), t) for jid, t in ab.lista_tarjetas_amarillas_por_90(estadisticas)[:10]],
                    "Tarjetas Amarillas /90", "Amarillas/90", color='yellow')
                ).pack(pady=5)

        tk.Button(frame, text="Tarjetas Rojas /90", bg="#ef4444", fg="white", font=("Arial", 13, "bold"),
                relief="flat", padx=15, pady=8,
                command=lambda: ab.graficar_barras(
                    [(jugadores_dict.get(jid, f"Jugador {jid}"), t) for jid, t in ab.lista_tarjetas_rojas_por_90(estadisticas)[:10]],
                    "Tarjetas Rojas /90", "Rojas/90", color='red')
                ).pack(pady=5)


# -----------------------------------------------------------------------------
# EJECUCIÓN DIRECTA
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = Interfaz(root)
    root.mainloop()
