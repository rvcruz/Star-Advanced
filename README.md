# Tarea 0: Star Advanced :school_satchel:

Estudiante: Rodolfo Javier Cruz Olivares

## Consideraciones generales :octocat:

Se debe crear carpeta "partidas" en el mismo directorio en donde se clonen los archivos

### Cosas implementadas y no implementadas :white_check_mark: :x:

* <Programacion Orientada a Objetos<sub>1</sub>>
   * <Menú de Inicio<sub>1.1</sub>>: Hecha completa :white_check_mark:
   * <Funcionalidades partida nueva<sub>1.2</sub>>: Hecha completa :white_check_mark:
   * <Funcionalidades cargar partida<sub>1.3</sub>>: Hecha completa :white_check_mark:
   * <Salir programa<sub>1.4</sub>>: Hecha completa :white_check_mark:
   * <Puntajes<sub>1.5</sub>>: Hecha completa :white_check_mark:
* <Flujo del Juego<sub>2</sub>>   
   * <Menú de Juego<sub>2.1</sub>>: Hecha completa :white_check_mark:
   * <Generar Tablero<sub>2.2</sub>>: Hecha completa :white_check_mark:
   * <Visualizacion Tablero<sub>2.3</sub>>: Hecha completa :white_check_mark:
   * <Actualizacion Tablero<sub>2.4</sub>>: Hecha completa :white_check_mark:
   * <Calculo Bestias<sub>2.5</sub>>: Hecha completa :white_check_mark:
   * <Sector sin Bestias<sub>2.6</sub>>: Hecha completa :white_check_mark:
   * <Guardado Automatico<sub>2.7</sub>>: Hecha completa :white_check_mark:
* <Termino del Juego<sub>3</sub>>
   * <Fin Juego: Derrota<sub>3.1</sub>>: Hecha completa :white_check_mark:
   * <Fin Juego: Victoria<sub>3.2</sub>>: Hecha completa :white_check_mark:
   * <Calculo Puntaje<sub>3.3</sub>>: Hecha completa :white_check_mark:
   * <Guardas Puntaje<sub>3.4</sub>>: Hecha completa :white_check_mark:
* <General<sub>4</sub>>
   * <Menus<sub>4.1</sub>>: Hecha completa :white_check_mark:
   * <Parametros<sub>4.2</sub>>: Hecha completa :white_check_mark:
   * <PEP8<sub>4.3</sub>>: Hecha completa :white_check_mark:

## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```main.py```. Además se debe crear los siguientes archivos y directorios adicionales:
1. ```Directorio: "partidas"``` en ```el mismo directorio donde se encuentra archivo main.py y modulacion.py```

## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```tablero```: ```print_tablero()```
2. ```parametros```: ```PROB_BESTIA, POND_PUNT``` 
3. ```math```: ```ceil()```
4. ```os```: ```path()```
5. ```random```: ```randint()```

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```modulacion```: Contiene a ```calculo_puntaje```, ```data_filter```, ```numeros_validos```, ```crear_tablero```,
```calcular_bestias```, ```invocar_bestias```, ```dicti```, ```valor_casilla```, ```bonus```, ```comprobar_tablero```,
```cargar_partida```, ```escribir_partida```, ```cargar_ranking```, ```escribir_ranking```.
Esta libreria incluye la clase Jugador()


## Supuestos y consideraciones adicionales :thinking:

Los supuestos que realicé durante la tarea son los siguientes:
1. <Inspire el desarrollo de mi programa en el ejercicio Pro-Gra-Oh! de la semana 0, debido a esto decidi utilizar una estructura orientada a objetos> 
2. <Si bien utilice referencias para inspirarme en la construccion de las funciones que necesitaba, ** adapte estas referencias a mis necesidades de codigo**>
3. <Cree una libreria "modulacion" para cargar funciones y acortar el codigo main.py>
4. <En "modulacion.py" importe librerias os, math, random y parametros>
5. <En "main.py" importe librerias modulacion y tablero>
6. Se le recuerda al ayudante crear un directorio con nombre "partidas" en el mismo directorio en donde se encuentran los script main.py y modulacion.py
7. La clase Jugador incluye atributos nombre y puntaje, para facilitar el traspaso de informacion.
* <8. El formato para guardar partidas es el siguiente:>
  * <4 Lineas de string en el siguiente orden: VISIBLES, BESTIAS, OCULTO, DIMENSIONES. Cada elemento del string separados por ";">
  * <VISIBLES: contiene las casillas abiertas por el usuario, el formato es:>
    * <[valor_casilla, coordenada_filas, coordenada_columna]>
  * <BESTIAS: contiene el valor de las coordenadas en donde exist una bestia, el formato es:>
    * <[coordenada_fila, coordenada_columna]>
  * <OCULTO: contiene todas las casillas de un tablero oculto con sus respectivas coordenadas, el formato es:>
    * <[valor_casilla, coordenada_fila, coordenada_columna]>
  * <Dimensiones: contine el valor de las dimensiones del tablero, el formato es:>
    * <[dimension_fila, dimension_columna]>
* <9. El formato del archivo puntajes.txt por jugador es sencillo donde cada elemento del string se separa por ";", el formato es:>
  * <Cada linea que se ingrese sera el valor del puntaje en esa partida, el formato es:>
    * <"nombre_jugador; Puntaje jugador">
* <10. El formato de impresion del TOP10 es mostrar los primeros 10 mejores puntajes del archivo puntajes.txt, el formato es:>
  * <Numero en Ranking)                     NOMBRE_JUGADOR:PUNTAJE JUGADOR>
  


## Referencias de código externo :book:

Para realizar mi tarea saqué código de:
1. \<https://github.com/IIC2233/contenidos/blob/master/semana-01/ejercicios_propuestos/ejercicios_propuestos.ipynb> Me inspire en Pro-Gra-OH! para estructurar mi tarea para que fuera orientada a objetos.
2. \<https://www.youtube.com/watch?v=XK2bG7fMBms&t=489s>: este hace \<crear tableros> y está implementado en el archivo <modulacion.py> en las líneas <49,56> y hace \<la creacion de tableros segun filas, columnas y valor de casilla>
3. \<https://www.youtube.com/watch?v=XK2bG7fMBms&t=489s>: este hace \<invocar bestias> y está implementado en el archivo <modulacion.py> en las líneas <267,275> y hace \<la invocacion de bestias en el tablero de forma aleatoria>
4. \<https://www.youtube.com/watch?v=NU3MGDvNNnI>: este hace \<iteracion de valores> y está implementado en el archivo <modulacion.py> en las líneas <230,260> y hace \<la implementacion del bonus en la iteracion de valores para las casillas cero y sus casillas adyacentes>
5. \<https://www.youtube.com/watch?v=O2mlGuaVTxY>: este hace \<pistas casillas adyacentes a bestia> y está implementado en el archivo <modulacion.py> en las líneas <278,289> y hace \<la implementacion de las pistas en las casillas adyacentes a la ubicacion de las bestias>
