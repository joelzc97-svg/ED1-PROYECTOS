class Nodo:
    def __init__(self, numero_turno: int, nombre_cliente: str):
        self.numero_turno = numero_turno
        self.nombre_cliente = nombre_cliente
        self.siguiente = None

    def __repr__(self):
        return f"Turno #{self.numero_turno} - {self.nombre_cliente}"