TODO
====

- Mejorar la documentación del modulo porque no se entiende a buenas y primeras
  lo que devuelve.
- falta crear un template con una vista generica para ponerla como parte del
  proceso
- depuerar las opciones de la cli para hacerlas excluyentes en algunos casos 
  (esto se logra haciendo un group con argsparse)
- permitir la opción de trabajar un nuevo modulo sin tener que estar haciendo
  una copia del un repositorio padre y creando un nuevo branch. 
- Utilizar la libreria python de launchpad-bzr para bajar la información de 
  los integrantes del equipo y manejar la información de cada desarrollador
  para lo que es la creación del modulo (launchpad-id, firmas de commits, 
  seudonimo que utiliza  para sus branches) e autogenerar información que va
  impresa en las licencias.
- manejar en un archivo externo xml una lista de repositorios con la 
  información de los repositorios configurados en la herramienta.
- agregar una opcion de cli -a --append que permita agregar archivos tomando
  en cuenta un template base para modelos, wizards, vistas y workflows... para
  todo en realidad.
- crear opciones de listado que permitan --show la información de los 
  repositorios configurados y de los developers, asi como tambien una funcion
  para modificar uno o crear uno nuevo directamente de la linea de comandos.
- hacer un decorador para manejar que los paramtros que ya fueron validados
  en argsparse function () vuelvan a revisarse antes de ejectuar la funcion
  de inicializacion del objeto oerp_module.
- agregar un template para el archivo de index.html
- agregar template para archivos dentro de /doc