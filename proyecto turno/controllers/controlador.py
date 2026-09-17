class ControladorTurnos:
    def __init__(self, modelo_lista, vista):
        self.modelo = modelo_lista
        self.vista = vista
        self.vista.set_controller(self)

    def agregar_turno(self, nombre_cliente: str):
        try:
            if not nombre_cliente:
                raise ValueError("El nombre del cliente no puede estar vacío.")

            nuevo = self.modelo.agregar_turno(nombre_cliente)
            self.vista.actualizar_lista(self.modelo.obtener_todos())
        except ValueError as e:
            self.vista.mostrar_error("Error de Validación", str(e))
        except Exception as e:
            self.vista.mostrar_error("Error Inesperado", f"Ocurrió un error: {str(e)}")

    def atender_siguiente(self):
        try:
            atendido = self.modelo.atender_siguiente()
            if not atendido:
                self.vista.actualizar_turno_actual("Atendiendo a: Nadie (Fila vacía)")
                raise ValueError("No hay clientes esperando en la fila.")

            texto_atencion = f"📢 ¡Turno #{atendido['turno']} ({atendido['cliente']}) a ventanilla!"
            self.vista.actualizar_turno_actual(texto_atencion)
            self.vista.actualizar_lista(self.modelo.obtener_todos())
        except ValueError as e:
            self.vista.mostrar_info("Información", str(e))
        except Exception as e:
            self.vista.mostrar_error("Error Inesperado", f"Ocurrió un error: {str(e)}")