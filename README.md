# Pagina-RioQuim
Hola que tal, mi nombre es Cristian Tessa.
Soy de Rio Cuarto - Cordoba - Argentina
Soy estudiantes de Programacion(Python) y esta es mi primera pagina web!!!

La siguiente pagina que desarrolle, tome como plantilla un modelo de boot strap.
La cual la pagina original esta en la carpeta AppCoder/Static
Y realice una copia en el html, llamado padre, donde hago las modificaciones. Las cuales explicare mas adelante.


Luego en el archivo views.py, estan las vistas de inicio, tienda, busqueda, productos y nosotros.
Y en el archivo models.py, estan las clases tienda (no tiene atributos),nosotros (no tiene atributos), busqueda y productos
tiene 2 atributos, llamados elemento y precio, que me sirven para dar de alta el producto y buscarlos dentro de la pagina.
Donde detallo cada uno a continuacion:

La pestaña inicio tiene un inicio.html en donde el cual esta el mensaje de bienvenida y un mensaje, luego que el usuario inicia sesion.
Su url esta configurado con al path " ", al cual se puede acceder con http://127.0.0.1:8000/AppCoder/

Luego la pestaña tienda y nosotros es meramente informativo, donde esta el tienda.html y nosotros.html que tiene info del local.
Sus urls son tienda y nosotros.

En la pagina para poder ver los productos, hay que regustrase y luego iniciar sesion. Donde ademas se puede agregar una imagen o avatar 
en el usuario logeado.

Muchas gracias.


Instrucciones para ejecutar este proyecto en local
Abrir Git Bash para Windows o una terminal para Linux/Unix.

Crear directorio de trabajo para el proyecto de curso.

cd
mkdir -p nombre_folder/nombre_proyectos
cd nombre_folder/nombre_folder_proyectos
Clonar el proyecto.
git clone https://github.com/Cristian2201/Pagina-RioQuim
cd blockbuster
Crear y activar entorno virtual. (Windows)
python -m venv venv
.\venv\Scripts\activate
(Linux)

python3 -m venv venv
source venv/bin/activate
Instalar las dependencias del proyecto.
pip install -r requirements.txt
Crear base de datos a partir de las migraciones.
python manage.py makemigrations
python manage.py migrate
Crear super-usuario.
python manage.py createsuperuser
Ingrese Username, Email address (opcional) y Password

Crear estáticos.
python manage.py collectstatic
Ejecutar proyecto, el servidor de Django expone el servicio por el localhost en el puerto 8000 por defecto http://127.0.0.1:8000/
python manage.py runserver
Comandos útiles para Django
Crear proyecto
django-admin startproject <nombre_proyecto> .
Crear una aplicación en un proyecto
python manage.py startapp <nombre_app>
Actualizar la base de datos del proyecto con cambios en nuestros modelos
Se realiza en dos pasos la creación de las migraciones, una por aplicación, y luego se realiza la creación de las tablas en la base de datos.

python manage.py makemigrations
python manage.py migrate
Comandos básicos para Git
Git clone
Git clone es un comando para descargarte el código fuente existente desde un repositorio remoto (como Github, por ejemplo). Descarga la última versión de tu proyecto en un repositorio y la guarda en tu ordenador.

git clone <https://link-del-repositorio>
Git branch
Creando una nueva rama:
git branch <nombre-rama>
Visualización de ramas:
git branch
git branch --list
Borrar una rama:
git branch -d <nombre-rama>
Git checkout
Para cambiarte a una rama existente
git checkout <nombre-rama>
Para crear y cambiarte a esa rama al mismo tiempo
git checkout -b <nombre-rama>
Git status
El comando de git status nos da toda la información necesaria sobre la rama actual:

Si la rama actual está actualizada.
Si hay algo para confirmar, enviar o recibir (pull).
Si hay archivos en preparación (staged), sin preparación(unstaged) o que no están recibiendo seguimiento (untracked).
Si hay archivos creados, modificados o eliminados status.
git status
Git add
Añadir un único archivo:
git add <nombre_archivo>
Añadir todo de una vez:
git add -A
git add .
git add *
Importante: El comando git add almacena en el stage los cambios de los archivos sin embargo aún no quedan registrados en el repositorio hasta que se utilice el comando de confirmación git commit para registrar un punto de control de los cambios.

Git commit
Git commit establece un punto de control al cual puedes volver más tarde si es necesario. Resulta muy aconsejable escribir un mensaje corto para explicar qué hemos desarrollado o modificado en el código fuente.

git commit -m "mensaje de confirmación"
Git push
Después de haber confirmado tus cambios, el siguiente paso que quieres dar es enviar tus cambios al servidor remoto. Git push envía tus commits al repositorio remoto.

git push <nombre-remoto> <nombre-rama>
git push origin <nombre-rama>
Importante: Git push solamente carga los cambios que han sido confirmados con un git commit.

Git pull
El comando git pull se utiliza para recibir actualizaciones del repositorio remoto.

git pull <nombre-remoto> <nombre-rama>
git pull origin main
Git remote
Sirve para cambiar la dirección url del repositorio que tenemos por origin.

git remote set-url origin <url_del_repositorio_en_GitHub>
