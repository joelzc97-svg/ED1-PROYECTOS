import tkinter as tk
from tkinter import ttk, messagebox

class VistaTurnos(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema de Turnos - Fila de Espera (MVC)")
        self.geometry("650x500")
        self.resizable(False, False)

        self.controller = None
        self._crear_componentes()

    def set_controller(self, controller):
        self.controller = controller

    def _crear_componentes(self):
        # Panel superior: Turno en atención actual
        frame_actual = ttk.LabelFrame(self, text=" Ventanilla de Atención ")
        frame_actual.pack(fill="x", padx=15, pady=10)

        self.lbl_turno_actual = ttk.Label(frame_actual, text="Atendiendo a: Ninguno", font=("Arial", 14, "bold"))
        self.lbl_turno_actual.pack(pady=15)

        btn_atender = ttk.Button(frame_actual, text="📢 Llamar / Atender Siguiente", command=self._on_atender)
        btn_atender.pack(pady=5, ipadx=10, ipady=5)

        # Panel central: Nuevo Turno
        frame_input = ttk.LabelFrame(self, text=" Generar Nuevo Turno ")
        frame_input.pack(fill="x", padx=15, pady=5)

        ttk.Label(frame_input, text="Nombre del Cliente:").pack(side="left", padx=5, pady=10)
        self.entry_nombre = ttk.Entry(frame_input, width=30)
        self.entry_nombre.pack(side="left", padx=5, pady=10)
        self.entry_nombre.focus()

        btn_generar = ttk.Button(frame_input, text="🎟️ Sacar Ticket", command=self._on_agregar)
        btn_generar.pack(side="left", padx=10, pady=10)

        # Panel inferior: Tabla de la Fila de Espera
        frame_tabla = ttk.LabelFrame(self, text=" Fila de Espera Actual (Lista Enlazada) ")
        frame_tabla.pack(fill="both", expand=True, padx=15, pady=10)

        columnas = ("Turno", "Cliente En Espera")
        self.tree = ttk.Treeview(frame_tabla, columns=columnas, show="headings", selectmode="browse")
        
        self.tree.heading("Turno", text="N° de Turno")
        self.tree.heading("Cliente En Espera", text="Nombre del Cliente")

        self.tree.column("Turno", width=120, anchor="center")
        self.tree.column("Cliente En Espera", width=460, anchor="w")

        scrollbar = ttk.Scrollbar(frame_tabla, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side="right", fill="y")
        self.tree.pack(fill="both", expand=True, padx=5, pady=5)

    def _on_agregar(self):
        nombre = self.entry_nombre.get().strip()
        if self.controller:
            self.controller.agregar_turno(nombre)

    def _on_atender(self):
        if self.controller:
            self.controller.atender_siguiente()

    def actualizar_lista(self, turnos):
        self.tree.delete(*self.tree.get_children())
        for turno in turnos:
            self.tree.insert("", "end", values=(f"#{turno['turno']}", turno['cliente']))
        self.entry_nombre.delete(0, tk.END)

    def actualizar_turno_actual(self, texto):
        self.lbl_turno_actual.config(text=texto)

    def mostrar_info(self, titulo, mensaje):
        messagebox.showinfo(titulo, mensaje)

    def mostrar_error(self, titulo, mensaje):
        messagebox.showerror(titulo, mensaje)