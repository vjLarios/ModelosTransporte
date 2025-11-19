# Modelos de Transporte

Aplicación interactiva para resolver problemas de transporte utilizando algoritmos de optimización clásicos.

## 🎯 Descripción

Esta herramienta permite resolver problemas de transporte mediante dos métodos principales:
- **Algoritmo de Aproximación de Vogel**: Heurística para obtener una solución inicial de buena calidad
- **Método de Paso Secuencial (Stepping Stone)**: Mejora iterativa de la solución

## 📋 Requisitos

- Python 3.7 o superior
- Librerías especificadas en `requirements.txt`

## 🚀 Instalación

1. Clona o descarga el repositorio
2. Instala las dependencias:

```bash
pip install -r requirements.txt
```

## 🎮 Uso

Ejecuta la aplicación principal:

```bash
python main.py
```

### Interfaz de Usuario

1. **Ventana de Entrada de Datos**: Ingresa los costos, oferta y demanda
   - Puedes agregar filas (orígenes) y columnas (destinos) dinámicamente
   - Máximo de 6 filas y 6 columnas
   - Todos los campos deben estar completos para continuar

2. **Menú Principal**: Selecciona el método de resolución:
   - Método de Vogel
   - Método de Paso Secuencial

## 📁 Estructura del Proyecto

```
ModelosTransporte/
├── main.py                 # Punto de entrada principal
├── InsertProblem.py        # Interfaz gráfica para entrada de datos
├── requirements.txt        # Dependencias del proyecto
├── README.md              # Este archivo
└── Methods/
    ├── Vogel.py           # Algoritmo de Vogel
    └── paso_secuencial.py # Método de Paso Secuencial
```

## 🔧 Dependencias

- **dearpygui** (≥1.11.1): Interfaz gráfica moderna y responsiva
- **pyfiglet** (≥0.8.0): Generación de títulos ASCII
- **rich** (≥13.0.0): Terminal con estilos y tablas formateadas
- **questionary** (≥1.10.0): Menú interactivo en la terminal

## 📊 Características

- ✅ Interfaz gráfica intuitiva con Dear PyGui
- ✅ Entrada dinámica de datos (agregar/eliminar filas y columnas)
- ✅ Validación automática de datos
- ✅ Soporte para múltiples algoritmos de optimización
- ✅ Visualización de resultados en tablas formateadas
- ✅ Menú interactivo con navegación sencilla

## 🧮 Algoritmos Implementados

### Método de Vogel (Aproximación)
Heurística que calcula penalizaciones para cada fila y columna, seleccionando las celdas con mayor diferencia entre costos.

### Método de Paso Secuencial (Stepping Stone)
Mejora iterativa de la solución calculando costos de oportunidad para encontrar el óptimo.

## 💡 Ejemplo de Uso

1. Ejecuta: `python main.py`
2. Completa la matriz de costos y recursos en la ventana gráfica
3. Selecciona el método de resolución
4. Observa los resultado y la solución óptima

## 📝 Notas

- La aplicación valida que la suma de ofertas sea igual a la suma de demandas
- Los valores numéricos aceptan decimales
- Es posible reutilizar la solución de Vogel en el Paso Secuencial

## 👨‍💻 Autor

Desarrollado como herramienta educativa para la resolución de problemas de transporte en investigación operativa.
