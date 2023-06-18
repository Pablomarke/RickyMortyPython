# Aplicación Web para visualizar la api de Rick y Morty

Programa creado en python con el framework flask. Desarrollado por Pablo Márquez.


# Necesidades previas 
- La api de Rick y Morty alojada en https://rickandmortyapi.com/ no necesita de apikey.

# Instalación
- crear un entorno en python y ejecutar el comando
```
pip install -r requirements.txt
```
la libreria utilizada en flask https://flask.palletsprojects.com/en/2.2.x/

# Opción de ejecucion RECOMENDADA
- Instalar
  ```pip install python-dotenv```
- Crear un archivo .env y dentro agregar lo siguiente:
``` FLASK_APP=main.py```
``` FLASK_DEBUG=True ```
- Y luego para lanzar seria en la terminal el comando:
``` flask run ```

# Ejecucion del programac clásica
- inicializar el servidor de flask
- en mac: ```export FLASK_APP=main.py```
- en windows: ```set FLASK_APP=main.py```

# Comando para ejecutar el servidor:
```flask --app main run```
# Comando para ejecutar el servidor en otro puerto diferente por default es el 5000
```flask --app main run -p 5002```
# Comando para ejecutar el servidor en modo debug, para realizar cambios en tiempo real
```flask --app main --debug run```