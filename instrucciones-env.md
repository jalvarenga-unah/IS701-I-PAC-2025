# Configuración de un Proyecto de Python con Visual Studio Code

Este documento proporciona instrucciones paso a paso para crear y configurar un proyecto de Python en Windows o Mac utilizando Visual Studio Code (VS Code).

---

## **1. Requisitos previos**

1. **Python**: Descarga e instala Python desde [python.org](https://www.python.org/downloads/).
   - Durante la instalación en Windows, asegúrate de marcar la casilla **"Add Python to PATH"**.

2. **Visual Studio Code**: Descarga e instala VS Code desde [code.visualstudio.com](https://code.visualstudio.com/).

3. **Extensión de Python para VS Code**:
   - Abre VS Code.
   - Ve a la pestaña de **Extensiones** (`Ctrl+Shift+X` / `Cmd+Shift+X`).
   - Busca "Python" y selecciona la extensión oficial de Microsoft, luego instálala.

---

## **2. Crear un Proyecto de Python**

### **Paso 1: Crear una carpeta para el proyecto**
- Crea una carpeta en tu sistema para alojar el proyecto.

### **Paso 2: Abrir la carpeta en VS Code**
- Ve a **Archivo > Abrir carpeta...** y selecciona la carpeta creada.

### **Paso 3: Crear un archivo Python**
- En la barra lateral izquierda, haz clic en el icono de **nuevo archivo**.
- Nombra el archivo con la extensión `.py` (por ejemplo, `main.py`).

---

## **3. Crear un Entorno Virtual (Opcional pero Recomendado)**

### **Paso 1: Abrir la terminal en VS Code**
- Ve a **Ver > Terminal** o presiona `Ctrl+\` / `Cmd+\`.

### **Paso 2: Crear el entorno virtual**
- En la terminal, escribe el siguiente comando:

  ```bash
  python -m venv venv
  ```

- Esto creará una carpeta llamada `venv` dentro de tu proyecto.

### **Paso 3: Activar el entorno virtual**

- **En Windows:**
  ```bash
  venv\Scripts\activate
  ```

- **En Mac:**
  ```bash
  source venv/bin/activate
  ```

### **Paso 4: Seleccionar el intérprete de Python del entorno virtual**
- Presiona `Ctrl+Shift+P` / `Cmd+Shift+P`.
- Escribe **"Python: Select Interpreter"** y selecciona el intérprete que corresponde al entorno virtual (`venv`).

---

## **4. Escribir y Ejecutar tu Código**

1. Abre el archivo `main.py` y escribe tu código. Por ejemplo:

   ```python
   print("¡Hola, mundo!")
   ```

2. Guarda el archivo (`Ctrl+S` / `Cmd+S`).

3. Ejecuta el programa:
   - Abre la terminal y escribe:

     ```bash
     python main.py
     ```

   - O utiliza el botón de **Ejecutar** en la esquina superior derecha del editor.

