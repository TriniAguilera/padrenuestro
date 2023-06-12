import os

ANCHO_GRILLA = 11 # NO EDITAR
LARGO_GRILLA = 16 # NO EDITAR

### cantidad máxima en cada bloque
MAXIMO_LUIGI = 1
MAXIMO_ESTRELLA = 1
MAXIMO_PARED = 5
MAXIMO_ROCA = 2
MAXIMO_FUEGO = 3
MAXIMO_FANTASMAS_HORIZONTAL = 3 ######## blancos
MAXIMO_FANTASMAS_VERTICAL = 3 ########## rojos

### tamaño ventana juego y constructor
TAMANO_VENTANA_JUEGO = 300, 300, 900, 900

### cantidad inicial vidas
CANTIDAD_VIDAS = 5

### cantidad inicial segundos
TIEMPO_CUENTA_REGRESIVA = 120

### multiplicador puntaje
MULTIPLICADOR_PUNTAJE = 1000

### caracteres del nombre
MIN_CARACTERES = 5
MAX_CARACTERES = 15

### velocidad fantasma para ponderador velocidad de tiempo movimiento
MIN_VELOCIDAD = 0.001
MAX_VELOCIDAD = 0.0025

### medidas tablero con y sin borde
MIN_X_BORDE = 372
MAX_X_BORDE = 372 + 53 * 10 + 10
MIN_X_TABLERO = 372 + 53 * 1 + 1
MAX_X_TABLERO = 372 + 53 * 9 + 9

MIN_Y_BORDE = 21
MAX_Y_BORDE = 21 + 53 * 15
MIN_Y_TRABLERO = 21 + 53 * 1
MAX_Y_TABLERO = 21 + 53 * 14

### ruta ventana de inicio Designer
RUTA_VENTANA_INICIO = os.path.join("frontend", "QtDesigner", "VentanaInicio.ui")

### ruta mapas
RUTA_MAPA_FANTASMA_MUERE = os.path.join("mapas", "fantasma muere.txt")
RUTA_MAPA_ENUNCIADO = os.path.join("mapas", "mapa enunciado.txt")
RUTA_MAPA_FACIL = os.path.join("mapas", "mapa facil.txt")
RUTA_ROCA_SALVA_FANTASMA = os.path.join("mapas", "ruta salva fantasma.txt")

### musica
RUTA_MUSICA_VICTORIA = os.path.join("sounds", "stageClear.wav")
RUTA_MUSICA_DERROTA = os.path.join("sounds", "gameOver.wav")

### ruta imagen elementos
RUTA_BORDE = os.path.join("sprites", "Elementos", "bordermap.png")
RUTA_FUEGO = os.path.join("sprites", "Elementos", "fire.png")
RUTA_LOGO = os.path.join("sprites", "Elementos", "logo.png")
RUTA_ESTRELLA = os.path.join("sprites", "Elementos", "osstar.png")
RUTA_ROCA = os.path.join("sprites", "Elementos", "roca_desierto_cortada.png")
RUTA_PARED = os.path.join("sprites", "Elementos", "wall.png")

### ruta fondo inicio
RUTA_FONDO = os.path.join("sprites", "Fondos", "fondo_inicio.png")
RUTA_DESIERTO = os.path.join("sprites", "Fondos", "desierto.jpg")
RUTA_DESIERTO_CORTADO = os.path.join("sprites", "Fondos", "desierto_cortado.png")

### ruta personaje luigi
RUTA_LUIGI_DOWN_1 = os.path.join("sprites", "Personajes", "luigi_down_1.png")
RUTA_LUIGI_DOWN_2 = os.path.join("sprites", "Personajes", "luigi_down_2.png")
RUTA_LUIGI_DOWN_3 = os.path.join("sprites", "Personajes", "luigi_down_3.png")
RUTA_LUIGI_FRONT = os.path.join("sprites", "Personajes", "luigi_front.png")
RUTA_LUIGI_LEFT_1 = os.path.join("sprites", "Personajes", "luigi_left_1.png")
RUTA_LUIGI_LEFT_2 = os.path.join("sprites", "Personajes", "luigi_left_2.png")
RUTA_LUIGI_LEFT_3 = os.path.join("sprites", "Personajes", "luigi_left_3.png")
RUTA_LUIGI_RIGHT_1 = os.path.join("sprites", "Personajes", "luigi_rigth_1.png")
RUTA_LUIGI_RIGHT_2 = os.path.join("sprites", "Personajes", "luigi_rigth_2.png")
RUTA_LUIGI_RIGHT_3 = os.path.join("sprites", "Personajes", "luigi_rigth_3.png")
RUTA_LUIGI_UP_1 = os.path.join("sprites", "Personajes", "luigi_up_1.png")
RUTA_LUIGI_UP_2 = os.path.join("sprites", "Personajes", "luigi_up_2.png")
RUTA_LUIGI_UP_3 = os.path.join("sprites", "Personajes", "luigi_up_3.png")

### ruta fantasma rojo vertical
RUTA_RED_GHOST_VERTICAL_1 = os.path.join("sprites", "Personajes", "red_ghost_vertical_1.png")
RUTA_RED_GHOST_VERTICAL_2 = os.path.join("sprites", "Personajes", "red_ghost_vertical_2.png")
RUTA_RED_GHOST_VERTICAL_3 = os.path.join("sprites", "Personajes", "red_ghost_vertical_3.png")

### ruta fantasma blanco horizontal
RUTA_WHITE_GHOST_LEFT_1 = os.path.join("sprites", "Personajes", "white_ghost_left_1.png")
RUTA_WHITE_GHOST_LEFT_2 = os.path.join("sprites", "Personajes", "white_ghost_left_2.png")
RUTA_WHITE_GHOST_LEFT_3 = os.path.join("sprites", "Personajes", "white_ghost_left_3.png")
RUTA_WHITE_GHOST_RIGHT_1 = os.path.join("sprites", "Personajes", "white_ghost_rigth_1.png")
RUTA_WHITE_GHOST_RIGHT_2 = os.path.join("sprites", "Personajes", "white_ghost_rigth_2.png")
RUTA_WHITE_GHOST_RIGHT_3 = os.path.join("sprites", "Personajes", "white_ghost_rigth_3.png")

