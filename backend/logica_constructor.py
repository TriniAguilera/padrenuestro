from PyQt5.QtCore import QObject, pyqtSignal
import os

class LogicaConstructor(QObject):
    
    senal_todos = pyqtSignal()
    senal_bloque = pyqtSignal()
    senal_entidad = pyqtSignal()
    senal_pop_up_error = pyqtSignal(list)
    senal_agregar_elemento = pyqtSignal(str, int, int)
    senal_revision_tablero = pyqtSignal(bool)
    senal_iniciar_juego_constructor = pyqtSignal(str, str)
    senal_entregar_botones = pyqtSignal(list)
    senal_ocultar_ventana = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.boton_izquierdo_actual = "None"
        self.botones_grilla_presionados = []
        self.nombre_archivo = "mapa modo constructor"
        self.tablero = [["", "", "", "", "", "", "", "", "", "", ""],
                        ["", "", "", "", "", "", "", "", "", "", ""],
                        ["", "", "", "", "", "", "", "", "", "", ""],
                        ["", "", "", "", "", "", "", "", "", "", ""],
                        ["", "", "", "", "", "", "", "", "", "", ""],
                        ["", "", "", "", "", "", "", "", "", "", ""],
                        ["", "", "", "", "", "", "", "", "", "", ""],
                        ["", "", "", "", "", "", "", "", "", "", ""],
                        ["", "", "", "", "", "", "", "", "", "", ""],
                        ["", "", "", "", "", "", "", "", "", "", ""],
                        ["", "", "", "", "", "", "", "", "", "", ""],
                        ["", "", "", "", "", "", "", "", "", "", ""],
                        ["", "", "", "", "", "", "", "", "", "", ""],
                        ["", "", "", "", "", "", "", "", "", "", ""],
                        ["", "", "", "", "", "", "", "", "", "", ""],
                        ["", "", "", "", "", "", "", "", "", "", ""]
                        ]

    def definir_nombre(self, nombre):
        self.nombre = nombre

    def elementos_comboBox(self, dificultad):
        if dificultad == "Todos":
            self.senal_todos.emit()
        elif dificultad == "Bloques":
            self.senal_bloque.emit()
        elif dificultad == "Entidades":
            self.senal_entidad.emit()

    def obtener_boton_izquierdo(self, string_boton):
        self.boton_izquierdo_actual = string_boton

    def contar(self, fila, columna):
        if self.boton_izquierdo_actual == "None":
            self.senal_pop_up_error.emit(["None"])
        else:
            if (fila, columna) in self.botones_grilla_presionados:
                print(f"Boton casilla ({fila}, {columna}) apretado más de una vez, sin efecto")
                ### usamos pop up de usar otro boton. Entrego []
                self.senal_pop_up_error.emit([(fila, columna)])
            else: #### boton no ha sido presionado
                print(f"Boton casilla ({fila}, {columna}) apretado por primera vez")
                self.botones_grilla_presionados.append((fila, columna))
                boton_izq = self.boton_izquierdo_actual
                print(f"Agregamos la tupla a la lista de botones presionados")
                print(f"Estamos en contar, vamos a agregar elemento: "\
                      f"{self.boton_izquierdo_actual} a casilla ({fila}, {columna})")
                self.senal_agregar_elemento.emit(boton_izq, int(fila), int(columna))

    def agregar_letra(self, letra, fila, columna):
        self.tablero[fila][columna] = letra
        if letra == "W":
            letra = "P"
        print(f"Letra {letra} fue agregada al tablero en posicion ({fila}, {columna})")

    def revisar_tablero(self, cant_luigi, cant_estrella):
        if cant_luigi == 0 and cant_estrella == 0:
            self.senal_revision_tablero.emit(True)
        else:
            self.senal_revision_tablero.emit(False)

    def crear_archivo(self):
        for f in range(16):
            for c in range(11):
                if not (f == 0 or f == 15 or c == 0 or c == 10) and self.tablero[f][c] == "":
                    self.tablero[f][c] = "-"
        tablero_con_borde = self.tablero
        tablero_con_borde.pop(15) # Quitamos ultima fila de borde
        tablero_con_borde.pop(0) # Quitamos primera fila de borde
        tablero_sin_borde = []
        for fila in tablero_con_borde:
            fila_sin_borde = []
            for elemento in fila:
                if elemento != "":
                    fila_sin_borde.append(elemento)
            tablero_sin_borde.append(fila_sin_borde)
        nombre_archivo_con_extension = self.nombre_archivo + ".txt"
        ruta = os.path.join("mapas", nombre_archivo_con_extension)
        abrir = open(ruta, "w")
        for fila in tablero_sin_borde:
            fila_string = ''.join(fila)
            abrir.write(f"{fila_string}\n")
        abrir.close()
        nombre_usuario = self.nombre
        nombre_archivo = self.nombre_archivo
        self.senal_iniciar_juego_constructor.emit(nombre_usuario, nombre_archivo)
        self.senal_ocultar_ventana.emit()

    def entregar_botones_presionados(self):
        botones = self.botones_grilla_presionados
        self.botones_grilla_presionados = []
        self.tablero = [["", "", "", "", "", "", "", "", "", "", ""],
                        ["", "", "", "", "", "", "", "", "", "", ""],
                        ["", "", "", "", "", "", "", "", "", "", ""],
                        ["", "", "", "", "", "", "", "", "", "", ""],
                        ["", "", "", "", "", "", "", "", "", "", ""],
                        ["", "", "", "", "", "", "", "", "", "", ""],
                        ["", "", "", "", "", "", "", "", "", "", ""],
                        ["", "", "", "", "", "", "", "", "", "", ""],
                        ["", "", "", "", "", "", "", "", "", "", ""],
                        ["", "", "", "", "", "", "", "", "", "", ""],
                        ["", "", "", "", "", "", "", "", "", "", ""],
                        ["", "", "", "", "", "", "", "", "", "", ""],
                        ["", "", "", "", "", "", "", "", "", "", ""],
                        ["", "", "", "", "", "", "", "", "", "", ""],
                        ["", "", "", "", "", "", "", "", "", "", ""],
                        ["", "", "", "", "", "", "", "", "", "", ""]
                        ]
        self.senal_entregar_botones.emit(botones)
    