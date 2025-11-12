import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from models.jugadores import Jugador
from models.equipo import Equipo
from models.ligas import Liga
from models.partido import Partido
from analisis_estadisticas.analisis_basico   # Asegúrate de tener los análisis en este archivo
from analisis_estadisticas.rendimiento_jugadores   # Asegúrate de tener los análisis en este archivo
from analisis_estadisticas.rendimiento_equipos   # Asegúrate de tener los análisis en este archivo

class FootApp:
    def __init__(self, root):
        self.root = root
        self.root.title("FootAnalisis")
        self.root.geometry("800x600")
        self.menu_principal()

    def menu_principal(self):
        # Limpiar ventana
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Menú Principal", font=("Arial", 20)).pack(pady=20)

        tk.Button(self.root, text="Jugar partido", width=30, command=self.jugar_partido_ui).pack(pady=5)
        tk.Button(self.root, text="Listar jugadores", width=30, command=self.listar_jugadores_ui).pack(pady=5)
        tk.Button(self.root, text="Listar equipos", width=30, command=self.listar_equipos_ui).pack(pady=5)
        tk.Button(self.root, text="Listar ligas", width=30, command=self.listar_ligas_ui).pack(pady=5)
        tk.Button(self.root, text="Listar partidos", width=30, command=self.listar_partidos_ui).pack(pady=5)
        tk.Button(self.root, text="Ver estadísticas", width=30, command=self.ver_estadisticas_ui).pack(pady=5)

    # -------------------- UI de Jugadores --------------------
    def listar_jugadores_ui(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Jugadores", font=("Arial", 18)).pack(pady=10)

        jugador_modelo = Jugador()
        jugadores = jugador_modelo.listar_jugadores()

        cols = ("ID", "Nombre", "Edad", "Posición", "Equipo ID")
        tree = ttk.Treeview(self.root, columns=cols, show="headings")
        for col in cols:
            tree.heading(col, text=col)
        tree.pack(fill=tk.BOTH, expand=True)

        for j in jugadores:
            tree.insert("", tk.END, values=(j["id"], j["nombre"], j["edad"], j["posicion"], j["equipo_id"]))

        tk.Button(self.root, text="Volver", command=self.menu_principal).pack(pady=10)

    # -------------------- UI de Equipos --------------------
    def listar_equipos_ui(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Equipos", font=("Arial", 18)).pack(pady=10)

        equipo_modelo = Equipo()
        equipos = equipo_modelo.listar_equipos()

        cols = ("ID", "Nombre", "Ciudad", "Estadio", "Capacidad", "Liga ID")
        tree = ttk.Treeview(self.root, columns=cols, show="headings")
        for col in cols:
            tree.heading(col, text=col)
        tree.pack(fill=tk.BOTH, expand=True)

        for e in equipos:
            tree.insert("", tk.END, values=(e["id"], e["nombre"], e["ciudad"], e["estadio"], e["capacidad_estadio"], e["liga_id"]))

        tk.Button(self.root, text="Volver", command=self.menu_principal).pack(pady=10)

    # -------------------- UI de Ligas --------------------
    def listar_ligas_ui(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Ligas", font=("Arial", 18)).pack(pady=10)

        liga_modelo = Liga()
        ligas = liga_modelo.listar_ligas()

        cols = ("ID", "Nombre", "Temporada")
        tree = ttk.Treeview(self.root, columns=cols, show="headings")
        for col in cols:
            tree.heading(col, text=col)
        tree.pack(fill=tk.BOTH, expand=True)

        for l in ligas:
            tree.insert("", tk.END, values=(l["id"], l["nombre"], l["temporada_actual"]))

        tk.Button(self.root, text="Volver", command=self.menu_principal).pack(pady=10)

    # -------------------- UI de Partidos --------------------
    def listar_partidos_ui(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Partidos", font=("Arial", 18)).pack(pady=10)

        partido_modelo = Partido()
        partidos = partido_modelo.listar_partidos()

        cols = ("ID", "Fecha", "Local ID", "Visitante ID", "Goles Local", "Goles Visitante", "Liga ID", "Jugado")
        tree = ttk.Treeview(self.root, columns=cols, show="headings")
        for col in cols:
            tree.heading(col, text=col)
        tree.pack(fill=tk.BOTH, expand=True)

        for p in partidos:
            tree.insert("", tk.END, values=(p["id"], p["fecha"], p["equipo_local_id"], p["equipo_visitante_id"],
                                            p["goles_local"], p["goles_visitante"], p["liga_id"], p["jugado"]))

        tk.Button(self.root, text="Volver", command=self.menu_principal).pack(pady=10)

    # -------------------- UI Jugar partido --------------------
    def jugar_partido_ui(self):
        messagebox.showinfo("Jugar Partido", "Aquí puedes implementar la lógica de jugar partido")
        self.menu_principal()

    # -------------------- Ver estadísticas --------------------
    def ver_estadisticas_ui(self):
        # Limpiar ventana
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Estadísticas", font=("Arial", 20)).pack(pady=20)

        tk.Button(self.root, text="Estadísticas Jugadores", width=30, command=self.estadisticas_jugadores_ui).pack(pady=5)
        tk.Button(self.root, text="Estadísticas Partidos", width=30, command=self.estadisticas_partidos_ui).pack(pady=5)
        tk.Button(self.root, text="Volver", command=self.menu_principal).pack(pady=20)

    # -------------------- Estadísticas Jugadores --------------------
    def estadisticas_jugadores_ui(self):
        # Mostrar las estadísticas de jugadores en gráfico
        rendimiento_jugador = rendimiento_jugador()
        stats = rendimiento_jugador.analisis_basico()

        # Graficar estadísticas de goles por partido, asistencias, etc.
        fig, ax = plt.subplots(figsize=(6, 4))
        jugadores = [s['nombre'] for s in stats]
        goles = [s['goles'] for s in stats]
        asistencias = [s['asistencias'] for s in stats]
        
        ax.bar(jugadores, goles, label="Goles")
        ax.bar(jugadores, asistencias, label="Asistencias", alpha=0.6)
        ax.set_ylabel("Cantidad")
        ax.set_xlabel("Jugadores")
        ax.set_title("Estadísticas de Jugadores")
        ax.legend()

        # Convertir la gráfica a un widget de Tkinter
        canvas = FigureCanvasTkAgg(fig, master=self.root)
        canvas.draw()
        canvas.get_tk_widget().pack()

        tk.Button(self.root, text="Volver", command=self.ver_estadisticas_ui).pack(pady=20)

    # -------------------- Estadísticas de Partidos --------------------
    def estadisticas_partidos_ui(self):
        # Mostrar las estadísticas de partidos en gráfico
        rendimiento_partido = rendimiento_partido()
        stats = rendimiento_partido.analisis_basico()

        # Graficar estadísticas de goles, tiros, etc.
        fig, ax = plt.subplots(figsize=(6, 4))
        partidos = [s['fecha'] for s in stats]
        goles_local = [s['goles_local'] for s in stats]
        goles_visitante = [s['goles_visitante'] for s in stats]

        ax.plot(partidos, goles_local, label="Goles Local", marker='o')
        ax.plot(partidos, goles_visitante, label="Goles Visitante", marker='o')
        ax.set_xlabel("Partidos")
        ax.set_ylabel("Goles")
        ax.set_title("Estadísticas de Partidos")
        ax.legend()

        # Convertir la gráfica a un widget de Tkinter
        canvas = FigureCanvasTkAgg(fig, master=self.root)
        canvas.draw()
        canvas.get_tk_widget().pack()

        tk.Button(self.root, text="Volver", command=self.ver_estadisticas_ui).pack(pady=20)

if __name__ == "__main__":
    root = tk.Tk()
    app = FootApp(root)
    root.mainloop()

