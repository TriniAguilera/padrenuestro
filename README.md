# Tarea 2: DCCazafantasmas :school_satchel:

## Cosas implementadas :white_check_mark: :x:

* Ventanas:
    - Ventana de inicio:
        1. :white_check_mark: Se visualiza correctamente y elementos mínimos no se superponen entre sí. Supongo que da lo mismo que el logo esté sobre la imagen de fondo.
        2. :white_check_mark: Se verifica nombre alfanumérico y que esté dentro del rango de caracteres. Notifica ```pop-up``` en caso de ser necesario.
        3. :white_check_mark: Se selecciona cualquiera de los mapas predefinidos o el modo constructor. Luego se ingresa a ventana de juego/constructor.
        4. :white_check_mark: Botón salir cierra ventana y termina programa.
    - Ventana de juego: 
        1. :white_check_mark: Se visualiza correctamente el mapa con sus elementos.
        2. :white_check_mark: Progresa vida y tiempo durante el juego.
        3. :white_check_mark: Ventana carga mapa si selecciona uno o entrega modo contructor.
        4. :white_check_mark: Panel de construcción contiene todas las entidades que se pueden poner.
        5. :white_check_mark: Panel de contrucción señala cuántos elementos van quedando de cada entidad.
        6. :white_check_mark: El juego se inicia cuando se aprieta el botón jugar de ventana de inicio o constructor.
        7. :white_check_mark: Botón salir cierra ventana actual y sale del programa.
* Mecánicas de juego:
    - Luigi:
        1. :white_check_mark: Al detectar colision con fantasma o fuego, pierde una vida (cuando no está apretado el cheatcode ```INF```) y se vuelve a posición inicial (con o sin cheatcode).
        2. :white_check_mark: Cuando colisiona con pared, luigi no se mueve en esa dirección. Si colisiona con roca y esta se puede mover, es arrastrada y luigi también se mueve.
        3. :white_check_mark: Se muestra consistencia en teclas y dirección hacia donde avanza luigi.
    - Fantasmas:
        1. :white_check_mark: Cada fantasma se mueve de manera independiente de los demas, respetando su velocidad y dirección.
        2. :white_check_mark: La velocidad de los fantasmas es aleatoria, depende del ponderador de velocidades
        3. :white_check_mark: Se implementan correctamente los fantasmas horizontales y verticales.
        4. :white_check_mark: Cuando fantasma choca con fuego desaparece y cuando es con un borde/roca/pared, cambia de dirección.
    - Modo constructor:
        1. :white_check_mark: No se permite poner un personaje cuando una casilla ya está ocupada.
        2. :white_check_mark: El panel de construcción tiene un máximo de elementos por entidad que se pueden poner. Se van actualizando a medida que se ponen en el mapa.
        3. :white_check_mark: Ningún sprite tiene movimiento al no iniciar juego.
        4. :white_check_mark: Permite jugar solo cuando hay un Luigi y una estrella, por lo menos. Si se cumple, el juego comienza con el mapa construido y comienza cuenta regresiva.
    - Fin de ronda:
        1. :white_check_mark: Se calculan correctamente los puntajes al finalizar la ronda.
        2. :white_check_mark: Se finaliza cuando se queda sin vidas, cuenta regresiva llega a cero o se gana partida.
        3. :white_check_mark: Se notifica nombre usuario, puntaje, vidas, tiempo restante y suena música correspondiente.
        4. :white_check_mark: Botón salir cierra ventana y termina programa.
* Interacción con el usuario:
    - Clicks: :white_check_mark: Modo constructor es implementado mediante click izquierdo.
    - Animaciones: :white_check_mark: Movimiento de personajes es fluido y animado mediante _sprites_ correspondientes.
* Funcionalidades del teclado:
    - Pausa: :white_check_mark: Se implementa botón de pausa al clikearlo o con letra P. Se detiene movimiento de fantasmas y deshabilita el de Luigi.
    - K + I + L: :white_check_mark: Al apretar esta combinación de letras (EN ORDEN), se eliminan todos los fantasmas del mapa.
    - I + N + F: :white_check_mark: Al apretar esta combinación de teclas (EN ORDEN), luigi no pierde más vidas cuando es dañado y tiene tiempo infinito (se detiene el timer).
* Archivos:
    - _Sprites_: :white_check_mark: Se trabaja correctamente con los archivos entregados.
    - ```parametros.py```: :white_check_mark: Se importan los parámetros definidos en el archivo cuando es necesario. En este también se definen las rutas de las imagenes.
* Bonus:
    - Volver a jugar: :white_check_mark: Cuando se termina la patida, se da la opción de volver a jugar con el mismo mapa utilizado.
    - Follower villain: :x:
    - Drag and Drop: :x:

## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```main.py```. Además, se debe crear los siguientes archivos y directorios adicionales: 
1. ```parametros.py``` en ```T2```
2. ```clases_objetos.py``` en ```T2/backend```
3. ```funciones.py``` en ```T2/backend```
4. ```logica_inicio.py``` en ```T2/backend```
5. ```logica_constructor.py``` en ```T2/backend```
6. ```logica_juego.py``` en ```T2/backend```
7. ```logica_derrota.py``` en ```T2/backend```
8. ```ventana_inicio.py``` en ```T2/frontend```
9. ```ventana_constructor.py``` en ```T2/frontend```
10. ```ventana_juego.py``` en ```T2/frontend```
11. ```ventana_derrota.py``` en ```T2/frontend```
12. ```VentanaInicio.ui``` en ```T2/frontend/QtDesigner```
13. ```mapa modo constructor.txt``` en ```T2/mapas```

## Flujo del programa
1.  **Main.py:** Este contiene la clase que corresponde a la ```QApplication```. Inicializa todas las lógicas y ventanas de inicio/constructor/juego/derrota como atributos. Además, en su método ```conectar``` realiza las conexiones de señales entre ```backend``` y ```frontend```.
2. **VentanaInicio:** Entrega la opción de ingresar un nombre de usuario, elegir un mapa predeterminado o el modo constructor, y la opción de salir y terminar el programa. 
3. **LogicaInicio:** Comprueba si el nombre cumple requisitos. Envia señal a la ```VentanaInicio``` con la respuesta.
4. **VentanaConstructor:** Permite crear un mapa propio. Al apretar algún botón de la sección izquierda, envía a la lógica el nombre del último botón izquierdo ```clickeado```. Al seleccionar el ```comboBox```, se envía el ítem seleccionado a la lógica. Esta envía una señal de desabilitar los botones y labels correspondientes en la sección izquierda. El tablero tiene botones transparentes en las casillas negras y, solo en caso de que se haga ```click``` en una casilla, se inserta el personaje y disminuye la cantidad máxima de este en la sección izquierda (si y solo sí, la cantidad disponible de ese personaje es mayor a 0). En caso de apretar una casilla sin seleccionar antes un personaje o de querer seleccionar una casilla ya ocupada, se muestra un ```pop.up``` con el error (desde lógica se manda señal de activar el ```pop-up```). El botón jugar permite ir a la ventana de juego, solo en caso de que esté luigi y la estrella en el tablero (esto lo verifica la lógica), por lo menos. El botón limpiar quita todos los elementos del tablero. Por último, el botón salir permite cerrar la ventana y terminar el programa.
5. **LogicaConstructor:** Esta rescata el nombre del usuario que se ingresó en la ventana de inicio. También contiene una variable que guarda el último botón izquierdo seleccionado. En una lista de listas (16x11) va guardando los personajes que son agregados al tablero (L/S/H/V/P/F/R). Antes de que se vaya a la ventana de juego, se crea un archivo ```mapa modo constructor.txt``` en la carpeta ```mapas``` con el nuevo mapa creado. Este está escrito en el mismo formato que los mapas predeterminados. En caso de limpiar el tablero, se vuelven a definir los atributos como se encontraban en un comienzo.
6. **VentanaJuego:** Muestra los personajes del tablero, el movimiento de las entidades y la interacción entre los elementos. El movimiento de Luigi y los fantasmas es mediante ```QPropertyAnimation``` y el cambio de _sprites_ es mediante threads (el thread es ejecutado completo en un tiempo igual a la duración de la animación). Es importante mencionar que se envía la señal de la tecla presionada a la lógica SOLO si la animación de Luigi ya finalizó (así evito duplicaciones). Los botones de limpiar y jugar se encuentran deshabilitados. El botón salir permite cerrar la ventana y terminar el programa. Esta ventana muestra la cantidad de vidas y tiempo restante (se va actualizando la información cada UN segundo). Cuando se aprieta el botón pausa o letra P, se pausa el juego. Para seguir hay que apretar la letra P o el botón reanudar. Solo en caso de que el juego no se encuentre en pausa, se permite el movimiento de los personajes. Los cheatcode se usan con las teclase presionadas en ORDEN. Cuando Luigi se encuentra sobre la estrella y se aprieta la letra G, se envia señal a la lógica para terminar partida e indicar que se ganó.
7. **LogicaJuego:** Recibe el nombre del usuario y el nombre del archivo del mapa que se utilizará (```mapa modo constructor.txt``` o uno predeterminado). Lee el archivo, y crea instancias de los elementos. En realidad, solo los elementos que se mueven (L/H/V/R) son instancias de clase, respecto a los otros elementos, en el método de instanciar al personaje, solo envía una señal con la fila y columna donde debe ir la imagen del elemento (son personajes estáticos) y en la lógica se guardan como tupla sus posiciones. Cada vez que luigi se mueve, primero se verifica si su nueva posición será la posicion de la estrella. Se manda un booleano con la respuesta a la ventana. De esta manera, al apretar la letra G, se abrirá la ventana de derrota solo si el booleano es True. Cuando llega la señal de mover a luigi, la lógica verifica si el movimiento es válido y, en caso de serlo, actualiza la nueva posición de Luigi y envia la señal a la ventana para mover el label. Ojo que cuando no se puede mover por una piedra o pared, no se envía la señal de mover a luigi, por eso no ocurre la animación de sprites. En cambio, con los bordes si hago la animación dentro de la misma casilla. Cuando Luigi choca con una piedra, se verifica primero si esta se puede mover. En caso de ser posible, se mueve la piedra y luego Luigi. En caso contrario, no se mueve ninguno de los dos. Cuando choca con fuego o algún fantasma, se resta una vida (solo si INF no está activo) y se reinica el juego (personajes vuelven a las posiciones iniciales y el tiempo se reincia si INF no está activo). El movimiento de fantasmas ocurre mediante ```QTimer```. Cada cierta cantidad de tiempo, se mueve el fantasma (se verifica dirección y nueva posición). El resultado del movimiento se envía a la ventana para mover los labels de fantasmas mediante animaciones y un thread para los sprites. Cuando un fantasma choca con un fuego, se elimina la instancia del fantasma y se manda señal de eliminar su label. Cuando chocan con una pared, piedra o borde, se cambia la dirección. Por último, cada un segundo se verifica si las vidas o tiempo restantes es mayor a cero. En caso de no ser así, se indica que se pierde y termina la partida. Sino, se actualiza el tiempo restante y las vidas.
8. **Ventana Derrota:** Muestra si se ganó o perdió, el nombre del usuario, el puntaje, las vidas que quedan y el tiempo restante. El boton volver, permite volver a jugar el juego con el mismo mapa que se utilizó. También suena la canción correspondiente al resultado.
9. **LogicaDerrota:** Guarda el nombre del usuario y el nombre del mapa en caso de querer volver. Dependiendo si se ganó o perdió, se instancia Musica con canción correspondiente.
10. **clases_objetos.py:** Contiene las clases de luigi, roca, la de ambos fantasmas y la musica. Las clases de los personajes, por lo general tiene un atributo de su fila, columna y dirección, y métodos para calcular su posición en X, en Y, cambiar su dirección, avanzar, entre otros.
11. **funciones.py:** Contiene las funciones ```procesar_archivo```, la cual recibe como argumento el nombre del mapa que se quiere utilizar de la carpeta ```mapas``` y lo retorna como una lista de lista (en formato 16x11), y la función ```calcular_posicion_futura```, la cual se usa en ```LogicaJuego``` para simular el movimiento de algun personaje sin cambiar su posición actual. De esta manera se tiene la nueva fila y columna resultante en caso de que se realice el movimiento, sin cambiar efectivamente los atributos de las instancias. De esta manera, con estos resultados se puede verificar si el movimiento del personaje es válido y, solo en caso de serlo, se actualizan las posiciones.

## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```os:``` para definir las rutas en el módulo de ```parametros.py```, en ```LogicaConstructor``` cuando se guarda el tablero creado en un archivo ```.txt``` en la carpeta ```mapas``` y en ```funciones.py``` para la función ```procesar_archivo```.
2. ```random:``` en ```LogicaJuego``` para definir de manera aleatoria el ponderador de velocidades de los fantasmas.
3. ```time:``` en ```VentanaJuego``` para dormir el thread de los sprites e ir cambiando las imagenes (así no duermo el programa principal).
4. ```threading:``` en ```VentanaJuego``` para crear los threads que se encargan del cambio de los sprites.
5. ```PyQt5:``` ```QtCore, QtWidgets, QtMultimedia, QtGui, uic, entre otras.```
6. ```sys:``` para trabajar bien el termino del programa


### Librerías propias 📘
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```frontend:``` Contiene archivos asociados a las ventanas.
    * ```ventana_inicio.py``` con la clase ```VentanaInicio```.
    * ```ventana_constructor.py``` con la clase ```VentanaConstructor```
    * ```ventana_juego.py``` con la clase ```VentanaJuego```
    * ```ventana_derrota.py``` con la clase ```VentanaDerrota```
2. ```backend:``` Contiene los archivos con sus ```QObjects``` que se encargan de analizar las acciones.
    * ```logica_inicio.py``` con la clase ```LogicaInicio```
    * ```logica_constructor.py``` con la clase ```LogicaConstructor```
    * ```logica_juego.py``` con la clase ```LogicaJuego```
    * ```logica_derrota.py``` con la clase ```LogicaDerrota```
    * ```clases_objetos.py``` con la clase ```Luigi```, ```Roca```, ```FantasmaHorizontal```, ```FantasmaVertical``` y ```Musica```
    * ```funciones.py``` con ```procesar_archivos``` y ```calcular_posicion_futura```.
3. ```parametros.py``` que contiene los parámetros mínimos especificados en el enunciado y las rutas de los sprites.
4. ```main.py``` con la clase ```DCCazafantasmas``` y corresponde al archivo que se debe ejecutar.

## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. No modificar el tamaño de la ventana, calculé las posiciones de los label y la grilla en función al tamaño que le asigné.
2. La animación de Luigi le asigné una duración de tal manera que en ese rango de tiempo, también ocurra el movimiento de sprites
en el thread y se logre apreciar el cambio. Se puede aumentar o disminuir el tiempo en caso de querer.
3. Igual lo mencione en ```VentanaConstructor```, pero en las casillas negras (que no son borde) le inserté botones transparentes para insertar los personajes, en caso de que sea posible.
4. Respecto a los threads, estos se crean y su duración es igual al tiempo que dura la animación del personaje (o un poco menor). Cuando hago un movimiento o reinicio el juego (luigi es dañado), primero hago que terminen los threads (animaciones) de los personajes. Así evito que queden duplicados.
5. Encontré buena idea que mi juego recibiera elnombre del usuario y el nombre del archivo que contiene el tablero, independiente si es uno predefinido o el que se creó en el modo constructor. Por eso tuve que crear el archivo ```mapa modo constructor.txt``` en la carpeta ```mapas```. 
6. En el modo constructor, primero se debe presionar un boton de la sección izquierda para elegir el personaje. Luego se inserta en el mapa. Creo que este problema igual lo dejé arreglado con un ```pop-up```, pero es por si ocurre algo que no debería jeje.
7. Las rocas no se sobreponen entre ellas. Si hay dos rocas pegadas y Luigi se mueve en esa dirección, moverá ambas en una casilla. En caso de que una no pueda moverse (choca con pared o borde), entonces no ocurre el movimiento. 
8. Se guarda el último ```cheatcode``` que fue aplicado. Al reiniciar el juego porque Luigi es dañado, se considera el cheatcode que hay. El atributo es ```True``` o ```False``` para ```INF``` y ```KIL```, respectivamente.
9. Las vidas y los segundos restantes se actualizan cada un segundo. Por eso, si se pierde por vidas hay un pequeño "desfase" en que se cierre la ventana de juego y aparezca la de derrota indicando que se perdió.
10. Al reiniciar un nivel, se reinicia el tiempo solo si no está aplicado el ```cheatcode``` de ```INF```. En caso de que este esté aplicado, las vidas y el tiempo restante se mantienen estáticos. Igual permito que se reinicie el juego cuando Luigi choca con un fuego o un fantasma, pero las vidas no se ven afectadas. Solo las posiciones.
10. Respecto al ```cheatcode``` ```KIL```, este elimina los fantasmas, pero si luigi choca con un fuego, estos vuelven a aparecer cuando se reinicia el nivel.
11. La velocidad de los fantasmas es aleatoria, pero es la misma para todos porque uso el mismo ponderador. Cuando se reincia el juego, esta velocidad puede cambiar porque se vuelve a instanciar todo de nuevo, entonces se calcula nuevamente el ponderador de velocidades.
12. Si se aprieta KIL, luego INF, los villanos no reaparecen a menos que Luigi choque con un fuego. En caso de chocar con fuego, los fantasmas aparecen, pero no se pierde vida ni tiempo porque el ultimo cheatcode es INF. Hay que volver a apretar KIL para que se active lo de perder vidas y restar tiempo.
