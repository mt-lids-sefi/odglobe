# odglobe
Aplicación desarrollada para el Seminario Final de la Licenciatura en Informática de la Universidad Nacional de Quilmes.
Dicho seminario consiste en investigar, desarrollar e implementar una aplicación que tome datos abiertos georeferenciados y, mediante algoritmos de aprendizaje
automático o minería de datos, encuentre patrones o clasificaciones que antes no se conocían para luego mostrarlos en un mapa.

## Aplicación para trabajar con mapas.
Esta primer parte del trabajo incluye una aplicación que recibe un archivo con información de coordenadas y muestra los puntos indicados por dichas coordenadas en un mapa.


### Sobre los archivos
Los archivos que recibe la aplicación deben tener formato CSV con las columnas separadas por comas.

Las coordenadas deben tener el formato 土##,######, cuidando que no sea un string. 


### Para ejecutar:


`pip install -r requirements.txt`

`python manage.py makemigrations`

`python manage.py migrate`

`python manage.py runserver`