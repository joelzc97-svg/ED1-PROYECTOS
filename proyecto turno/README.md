# Sistema de Turnos - Fila de Espera (MVC)

Aplicación de escritorio en Python que simula un sistema de gestión de turnos (fila de espera), implementado con el patrón de diseño **MVC (Modelo-Vista-Controlador)** y una **lista enlazada simple** como estructura de datos para manejar la cola de clientes.

## 📋 Descripción

El sistema permite generar tickets/turnos para clientes que llegan a un establecimiento y gestionarlos en orden de llegada (FIFO - First In, First Out), simulando el funcionamiento de una ventanilla de atención al público.

## ✨ Características

- Generación de turnos con numeración automática incremental.
- Atención de turnos en orden de llegada (FIFO) mediante una lista enlazada.
- Visualización en tiempo real de la fila de espera en una tabla.
- Interfaz gráfica construida con `tkinter`.
- Validaciones y manejo de errores (nombre vacío, fila vacía, etc.).

## 🏗️ Arquitectura (MVC)

El proyecto sigue el patrón Modelo-Vista-Controlador:

| Capa | Archivo | Responsabilidad |
|---|---|---|
| **Modelo** | `models/modelNodo.py` | Define la estructura `Nodo` (turno individual) de la lista enlazada. |
| **Modelo** | `models/modelLista.py` | Implementa `ListaEnlazadaTurnos`: lógica para agregar, atender y listar turnos. |
| **Vista** | `views/vista.py` | Define `VistaTurnos`: interfaz gráfica (tkinter) con formulario, botón de atención y tabla de espera. |
| **Controlador** | `controllers/controlador.py` | Define `ControladorTurnos`: conecta modelo y vista, gestiona la lógica de negocio y errores. |
| **Principal** | `main.py` | Punto de entrada de la aplicación; inicializa modelo, vista y controlador. |

### Diagrama de flujo

```
main.py
  │
  ├── ListaEnlazadaTurnos (Modelo)
  ├── VistaTurnos (Vista - Tkinter)
  └── ControladorTurnos (Controlador)
          │
          ├── vista.set_controller(self)
          ├── agregar_turno() ──► modelo.agregar_turno() ──► vista.actualizar_lista()
          └── atender_siguiente() ──► modelo.atender_siguiente() ──► vista.actualizar_turno_actual()
```

## 📁 Estructura del proyecto

Para que las importaciones funcionen correctamente, los archivos deben organizarse así:

```
proyecto/
├── main.py
├── controllers/
│   └── controlador.py
├── views/
│   └── vista.py
└── models/
    ├── modelNodo.py
    └── modelLista.py
```

> ⚠️ **Importante:** los archivos fueron entregados en un mismo nivel, pero `main.py` los importa desde subcarpetas (`controllers`, `views`, `models`). Debes moverlos a esas carpetas (y opcionalmente agregar un archivo vacío `__init__.py` en cada una si usas paquetes explícitos) para que el programa se ejecute sin errores de importación.

## 🔧 Requisitos

- Python 3.7 o superior
- `tkinter` (incluido en la instalación estándar de Python en la mayoría de sistemas)

No se requieren dependencias externas adicionales (no hay `requirements.txt` necesario).

### Instalación de tkinter (si no está disponible)

- **Windows/macOS:** viene incluido con Python.
- **Linux (Debian/Ubuntu):**
  ```bash
  sudo apt-get install python3-tk
  ```

## ▶️ Ejecución

Desde la carpeta raíz del proyecto:

```bash
python main.py
```

## 🖥️ Uso de la aplicación

1. **Generar un turno:** escribe el nombre del cliente en el campo de texto y haz clic en **"🎟️ Sacar Ticket"**. El turno se añade al final de la fila con un número autoincremental.
2. **Atender al siguiente cliente:** haz clic en **"📢 Llamar / Atender Siguiente"**. Se atiende al cliente que lleva más tiempo esperando (el primero de la lista) y se elimina de la fila.
3. **Ver la fila de espera:** la tabla inferior muestra en todo momento los turnos pendientes, con su número y nombre de cliente.

## ⚙️ Detalles técnicos

- **Estructura de datos:** lista enlazada simple (`Nodo` con puntero `siguiente`), donde:
  - `agregar_turno()` inserta un nuevo nodo al final (recorrido O(n)).
  - `atender_siguiente()` elimina y retorna el nodo cabeza (O(1)).
  - `obtener_todos()` recorre la lista completa para listar los turnos pendientes.
- **Manejo de errores:** el controlador captura `ValueError` (validaciones de negocio, como nombre vacío o fila vacía) y excepciones genéricas, mostrando mensajes mediante `messagebox` de tkinter.

## 🚀 Posibles mejoras futuras

- Persistencia de datos (guardar turnos en archivo o base de datos).
- Historial de turnos atendidos.
- Prioridades de atención (ej. turnos preferenciales).
- Tiempo estimado de espera por turno.

## 📄 Licencia

Este proyecto es de uso educativo/libre. Ajusta esta sección según corresponda.
