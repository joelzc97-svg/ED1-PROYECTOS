from models.modelNodo import Nodo
class ListaEnlazadaTurnos:
    def __init__(self):
        self.cabeza = None
        self.contador_turnos = 1  # Para autoincrementar el número de ticket (1, 2, 3...)
        self.longitud = 0

    def agregar_turno(self, nombre_cliente: str) -> Nodo:
        nuevo_nodo = Nodo(self.contador_turnos, nombre_cliente)
        self.contador_turnos += 1

        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
        
        self.longitud += 1
        return nuevo_nodo

    def atender_siguiente(self) -> dict:
        """Elimina y retorna el primer elemento de la lista (la cabeza)"""
        if not self.cabeza:
            return None
        
        turno_atendido = {
            'turno': self.cabeza.numero_turno,
            'cliente': self.cabeza.nombre_cliente
        }
        
        # Desplazar la cabeza al siguiente nodo
        self.cabeza = self.cabeza.siguiente
        self.longitud -= 1
        return turno_atendido

    def obtener_todos(self) -> list:
        """Recorre la lista para retornar todos los turnos pendientes"""
        turnos = []
        actual = self.cabeza
        while actual:
            turnos.append({
                'turno': actual.numero_turno,
                'cliente': actual.nombre_cliente
            })
            actual = actual.siguiente
        return turnos