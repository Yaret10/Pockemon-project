# Pokemon Project

Se plantea hacer una copia de la base de datos de la PokeAPI hacia una propia en la nube, posterior a ello implementar las rutas principales que ofrece la PokeAPI:

 - [Obtener todos los pokemon con paginación incluida](https://pokeapi.co/api/v2/pokemon/)
 - [Obtener pokemon por id o nombre](https://pokeapi.co/api/v2/pokemon/1/)
 - [Obtener todas las pokedex](https://pokeapi.co/api/v2/pokedex/)
 - [Obtener pokedex por id o nombre](https://pokeapi.co/api/v2/pokedex/1/)

## Deployment

Crear un archivo ".env" dentro del proyecto, que contenga lo siguiente:

```
  FLASK_APP='...', FLASK_DEBUG='...' y SECRET_KEY='...'
```
Crear un entorno virtual:

```
  virtualenv venv
```
Activar el entorno virtual:
```
  \venv\Scripts>activate.bat
```
Instalar las dependencias:
```
  pip install -r requirements.txt
```
Ejecutar el proyecto:
```
  flask run
```

## Project endpoints

Con respecto a los Pokemones:
```
Copiado de la BD de Pokemon a la BD MongoDB:

http://127.0.0.1:5000/pokemon/save
```
```
Obtención de todos los Pokemones de la BD MongoDB:

http://127.0.0.1:5000/pokemon/list
```
```
Obtención de todos los Pokemones de la BD MongoDB por ID:

http://127.0.0.1:5000/pokemon/details/<int:id>
```
```
Obtención de todos los Pokemones de la BD MongoDB por NOMBRE:

http://127.0.0.1:5000/pokemon/details/<string:nombre>
```

Con respecto a los Pokedex:
```
Copiado de la BD de Pokedex a la BD MongoDB:

http://127.0.0.1:5000/pokedex/save
```
```
Obtención de todos los Pokedex de la BD MongoDB:

http://127.0.0.1:5000/pokedex/list
```
```
Obtención de todos los Pokedex de la BD MongoDB por ID:

http://127.0.0.1:5000/pokedex/details/<int:id>
```
```
Obtención de todos los Pokedex de la BD MongoDB por NOMBRE:

http://127.0.0.1:5000/pokedex/details/<string:nombre>
```

## Authors

- [Mijail Denis Zavala Llanco](https://github.com/MIDEZA-22)
- [Gerson Daniel Vargas Polo](https://github.com/Gersaurio)
- [César Yaret Chuica Cordero](https://github.com/Yaret10)
- [Jordy Cruz Suasnabar](https://github.com/dyjhor014)