## 🕹️ Lista de Tareas Retro
## Descripción del Proyecto

Esta es una aplicación web de lista de tareas desarrollada en Django con Python. El proyecto te permite gestionar tus tareas diarias de forma simple, con funcionalidades para crear, leer, actualizar, eliminar y buscar tareas.

El diseño de la interfaz se inspira en una estética minimalista gamer retro, con una paleta de colores de terminal, tipografías pixeladas y un estilo de UI de 8 bits.

### Funcionalidades Principales
Crear tareas: Añade nuevas tareas con un título y una categoría.

-- Actualizar tareas: Edita el título y la categoría de las tareas existentes.

-- Eliminar tareas: Borra tareas que ya no necesitas.

-- Marcar como completada: Cambia el estado de una tarea con un simple clic.

-- Búsqueda y filtro: Filtra tareas por título o por una de las tres categorías predefinidas: hogar, estudio y trabajo.

--  Diseño responsivo: La interfaz se adapta a diferentes tamaños de pantalla, desde computadoras de escritorio hasta dispositivos móviles.

### Tecnologías Utilizadas
-- Backend: Python y Django

-- Frontend: HTML5 y CSS3

-- Base de Datos: SQLite (por defecto en Django, ideal para desarrollo)

### Configuración y Ejecución del Proyecto
Sigue estos pasos para tener una copia local del proyecto en funcionamiento.

####1. Requisitos Previos
Asegúrate de tener Python y pip instalados en tu sistema.

####2. Clonar el Repositorio
Abre tu terminal y ejecuta el siguiente comando para clonar el proyecto desde GitHub:

-- Bash

git clone https://github.com/tu-usuario/nombre-del-repositorio.git
cd nombre-del-repositorio
####3. Crear un Entorno Virtual (Recomendado)
Es una buena práctica crear un entorno virtual para aislar las dependencias del proyecto.

-- Bash

python -m venv venv
Activa el entorno virtual:

Windows: venv\Scripts\activate

macOS / Linux: source venv/bin/activate

####4. Instalar Dependencias
Instala todas las librerías necesarias para el proyecto:

### Bash

pip install -r requirements.txt
Si aún no tienes el archivo requirements.txt, puedes crearlo manualmente o usar el siguiente comando después de instalar Django:

### Bash

pip install Django
pip freeze > requirements.txt
####5. Aplicar Migraciones
Las migraciones preparan la base de datos para que puedas empezar a usar los modelos.

### Bash

python manage.py makemigrations
python manage.py migrate
####6. Ejecutar el Servidor
Inicia el servidor de desarrollo local de Django:

### Bash

python manage.py runserver
La aplicación estará disponible en tu navegador en la siguiente dirección:

http://127.0.0.1:8000/
