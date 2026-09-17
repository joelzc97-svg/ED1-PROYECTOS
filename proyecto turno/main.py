from controllers.controlador import ControladorTurnos
from views.vista import VistaTurnos
from models.modelLista import ListaEnlazadaTurnos

def main():
    modelo = ListaEnlazadaTurnos()
    vista = VistaTurnos()
    controlador = ControladorTurnos(modelo, vista)
    
    vista.mainloop()

if __name__ == "__main__":
    main()