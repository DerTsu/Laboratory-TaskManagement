- Jhonatan Ortega - jaortegac@correo.usbcali.edu.co
- Sofia Moreno - smorenoq@correo.usbcali.edu.co
- Maria Jose Ramirez - mjramirezm@correo.usbcali.edu.co 

# Task Management

Este proyecto es una aplicación de gestión de tareas desarrollada en Python con Django.

## Instalación y configuración

Sigue estos pasos para configurar el entorno de desarrollo e iniciar la aplicación:

1. **Crear un entorno virtual** (recomendado para evitar conflictos con dependencias globales):

   ```sh
   python -m venv env
   ```

2. **Activar el entorno virtual:**
   - En Windows:
     ```sh
     env\Scripts\activate
     ```

3. **Instalar las dependencias del proyecto:**

   ```sh
   pip install -r requirements.txt
   ```

4. **Posicionarse en la carpeta `task_management`:**

   ```sh
   cd task_management
   ```

5. **Ejecutar el servidor de desarrollo:**

   ```sh
   python manage.py runserver
   ```

6. **Acceder a la aplicación:**
   Abre un navegador y visita: [http://127.0.0.1:8000](http://127.0.0.1:8000)

## Notas adicionales
- Asegúrate de que tienes Python instalado (recomendado: Python 3.8 o superior).
- Si necesitas realizar migraciones de base de datos, usa:
  ```sh
  python manage.py migrate
  ```

