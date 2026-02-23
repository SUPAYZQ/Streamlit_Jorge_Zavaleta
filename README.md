# 🦂 Python Fundamentals – Módulo 1
### Especialización en Python for Analytics · DMC Institute

---

## 📋 Descripción

Aplicación interactiva desarrollada con **Streamlit** que integra los conceptos fundamentales del Módulo 1:

- **Variables y Condicionales** → Verificador de presupuesto en tiempo real
- **Listas y Diccionarios** → Registro dinámico de actividades financieras
- **Funciones y Programación Funcional** → Cálculo de retorno con `map` y `lambda`
- **POO (Programación Orientada a Objetos)** → Clase `Actividad` con atributos y métodos propios

---

## 🗂️ Estructura del proyecto

```
python-fundamentals-modulo1/
│
├── app.py               # Aplicación principal Streamlit
├── requirements.txt     # Dependencias del proyecto
└── README.md            # Este archivo
```

---

## 🚀 Instrucciones de ejecución

### 1. Clonar el repositorio
```bash
git clone https://github.com/tu-usuario/python-fundamentals-modulo1.git
cd python-fundamentals-modulo1
```

### 2. Crear entorno virtual (recomendado)
```bash
python -m venv venv
source venv/bin/activate        # macOS / Linux
venv\Scripts\activate           # Windows
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Ejecutar la aplicación
```bash
streamlit run app.py
```

La aplicación se abrirá automáticamente en tu navegador en `http://localhost:8501`.

---

## 📦 Dependencias

| Librería | Versión mínima | Uso |
|---|---|---|
| `streamlit` | 1.32.0 | Framework de la aplicación web |
| `pandas` | 2.0.0 | Manejo y visualización de tablas de datos |

---

## 🧩 Contenido de los ejercicios

### Ejercicio 1 – Variables y Condicionales
Verificador de presupuesto interactivo. El usuario ingresa un presupuesto y un gasto real; el sistema evalúa la condición con un `if/else`, muestra la diferencia y el porcentaje de uso mediante una barra de progreso visual.

### Ejercicio 2 – Listas y Diccionarios
Registro de actividades financieras. Cada actividad se almacena como un **diccionario** dentro de una **lista** usando `st.session_state`. Se muestra una tabla con `st.dataframe()` y se evalúa el estado de cada actividad mediante un bucle `for`.

### Ejercicio 3 – Funciones y Programación Funcional
Cálculo del retorno esperado con la fórmula:

```
Retorno = presupuesto × tasa × meses
```

Se define la función `calcular_retorno()` y se aplica a todas las actividades usando **`map()` + `lambda`** — sin ningún bucle explícito.

### Ejercicio 4 – POO (Programación Orientada a Objetos)
Implementación de la clase `Actividad`:

```python
class Actividad:
    def __init__(self, nombre, tipo, presupuesto, gasto_real): ...
    def esta_en_presupuesto(self) -> bool: ...
    def mostrar_info(self) -> dict: ...
```

Los registros del Ejercicio 2 se convierten en objetos mediante una **list comprehension**.

---

## 🔗 Enlaces

- **Repositorio GitHub:** [https://github.com/tu-usuario/python-fundamentals-modulo1](https://github.com/tu-usuario/python-fundamentals-modulo1)
- **Aplicación en Streamlit Cloud:** [https://tu-app.streamlit.app](https://tu-app.streamlit.app)

---

## 👤 Autor

**Tu Nombre Aquí**  
Especialización en Python for Analytics · DMC Institute  
2025

---

> *"No es necesario saberlo todo para comenzar a crear; es suficiente con comprender bien las herramientas que ya se tienen."*  
> — Carlos Carrillo Villavicencio
