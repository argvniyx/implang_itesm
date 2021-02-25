# Implang - ITESM

Proyecto de visualización de datos y narrativa.

## Instrucciones 
Hay que clonar el repositorio primero:

``` sh
git clone https://github.com/j-m-r-c/implang_itesm # Original
git clone https://github.com/argvniyx/implang_itesm # Desarrollo del proyecto
```

Una vez clonado, es necesario contar con `python`, `pip` y `pipenv` y,
dentro del directorio del repositorio hacer:

``` sh
pipenv install dash dash-bootstrap-components dash-html-components pandas
```

Para correr el servidor de desarrollo local, simplemente hay que hacer
`pipenv run python app.py`. Si se prefiere, puede hacerse `pipenv shell` primero
y luego simplemente `python app.py`.
