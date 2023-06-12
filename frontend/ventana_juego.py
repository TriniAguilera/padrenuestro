import typing
import sys
from PyQt5.QtCore import pyqtSignal, Qt, QRect, QPoint, QSize, QPropertyAnimation
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import (QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QGridLayout)
import parametros as p
import threading
from time import sleep

class VentanaJuego(QWidget):

    senal_iniciar_tiempo = pyqtSignal(); senal_iniciar_fantasmas = pyqtSignal()
    senal_instanciar_elementos = pyqtSignal(); senal_tecla = pyqtSignal(str)
    senal_pausa = pyqtSignal(); senal_reanudar = pyqtSignal()
    senal_cheatcode = pyqtSignal(str); senal_ganar = pyqtSignal(bool)

    def __init__(self):
        super().__init__()
        self.init_gui()
        self.pausar_juego = False; self.mover = False; self.ganado = False; self.dict_threads = {}
        self.dict_label_elementos = {"S": [], "L": [], "H": {}, "V": {}, "R": {}, "F": [], "P": []}
        self.k = False; self.i = False; self.l = False; self.n = False; self.f = False
        self.lista_fantasmas_horizontales_eliminados = []
        self.lista_fantasmas_verticales_eliminados = []
        self.imagenes_luigi = {"D": [p.RUTA_LUIGI_DOWN_1, p.RUTA_LUIGI_DOWN_2, 
                            p.RUTA_LUIGI_DOWN_3], "L": [p.RUTA_LUIGI_LEFT_1, p.RUTA_LUIGI_LEFT_2, 
                            p.RUTA_LUIGI_LEFT_3], "R": [p.RUTA_LUIGI_RIGHT_1, p.RUTA_LUIGI_RIGHT_2,
                            p.RUTA_LUIGI_RIGHT_3], "U": [p.RUTA_LUIGI_UP_1, p.RUTA_LUIGI_UP_2, 
                            p.RUTA_LUIGI_UP_3], "F": [p.RUTA_LUIGI_FRONT]}
        self.imagenes_horizontal = {-1: [p.RUTA_WHITE_GHOST_LEFT_1, p.RUTA_WHITE_GHOST_LEFT_2,
                                p.RUTA_WHITE_GHOST_LEFT_3], 1: [p.RUTA_WHITE_GHOST_RIGHT_1,
                                p.RUTA_WHITE_GHOST_RIGHT_2, p.RUTA_WHITE_GHOST_RIGHT_3]}
        self.imagenes_vertical = {1: [p.RUTA_RED_GHOST_VERTICAL_1, p.RUTA_RED_GHOST_VERTICAL_2,
                                p.RUTA_RED_GHOST_VERTICAL_3]}
    def init_gui(self):
        self.setGeometry(100, 100, 1000, 900); self.setWindowTitle("Ventana Juego")

        self.label_vida = QLabel("VIDAS: ", self); self.label_vida.setFont(QFont("calibri", 12))
        self.label_vida.setGeometry(QRect(QPoint(20, 10), QSize(150, 42)))

        self.label_tiempo = QLabel("TIEMPO:", self); self.label_tiempo.setFont(QFont("calibri", 12))
        self.label_tiempo.setGeometry(QRect(QPoint(20, 50), QSize(150, 42)))

        self.widget_principal_horizontal = QWidget(self)
        self.layout_principal_horizontal = QHBoxLayout()

        self.boton_pausa = QPushButton(self); self.boton_pausa.setObjectName("boton_pausa")
        self.boton_pausa.setGeometry(QRect(QPoint(110, 400), QSize(150, 42)))
        self.boton_pausa.setText("Pausa"); self.boton_pausa.setFont(QFont("calibri", 12))
        self.boton_pausa.clicked.connect(self.pausa)

        self.boton_reanudar = QPushButton(self); self.boton_reanudar.setObjectName("boton_reanudar")
        self.boton_reanudar.setGeometry(QRect(QPoint(110, 450), QSize(150, 42)))
        self.boton_reanudar.setText("Reanudar"); self.boton_reanudar.setFont(QFont("calibri", 12))
        self.boton_reanudar.clicked.connect(self.reanudar); self.boton_reanudar.setEnabled(False)

        self.boton_limpiar_constructor = QPushButton(self)
        self.boton_limpiar_constructor.setObjectName("boton_limpiar_constructor")
        self.boton_limpiar_constructor.setGeometry(QRect(QPoint(25, 800), QSize(150, 42)))
        self.boton_limpiar_constructor.setText("Limpiar tablero")
        self.boton_limpiar_constructor.setFont(QFont("calibri", 12))
        self.boton_limpiar_constructor.clicked.connect(self.limpiar_tablero)
        self.boton_limpiar_constructor.setEnabled(False)

        self.boton_jugar_constructor = QPushButton(self)
        self.boton_jugar_constructor.setObjectName("boton_jugar_constructor")
        self.boton_jugar_constructor.setGeometry(QRect(QPoint(185, 800), QSize(150, 42)))
        self.boton_jugar_constructor.setText("Jugar")
        self.boton_jugar_constructor.setFont(QFont("calibri", 12))
        self.boton_jugar_constructor.clicked.connect(self.limpiar_tablero)
        self.boton_jugar_constructor.setEnabled(False)

        self.boton_salir_constructor = QPushButton(self)
        self.boton_salir_constructor.setObjectName("boton_salir_constructor")
        self.boton_salir_constructor.setGeometry(QRect(QPoint(100, 750), QSize(150, 42)))
        self.boton_salir_constructor.setText("Salir")
        self.boton_salir_constructor.setFont(QFont("calibri", 12))
        self.boton_salir_constructor.clicked.connect(self.salir)

        self.widget_izquierdo = QWidget(self); self.layout_izquierdo = QVBoxLayout()
        self.layout_principal_horizontal.addLayout(self.layout_izquierdo)
        self.crear_grilla()
       
    def crear_grilla(self):
        self.widget_grilla = QWidget(self)
        self.widget_grilla.setGeometry(QRect(QPoint(360, 10), QSize(620, 870)))
        self.layout_grilla = QGridLayout()
        self.layout_grilla.setHorizontalSpacing(1); self.layout_grilla.setVerticalSpacing(1)
        self.widget_grilla.setLayout(self.layout_grilla)
        self.widget_grilla.setStyleSheet(""" background-color: #876244;
            border-color: 1px solid #000000; """)
        for fila in range(16):
            for columna in range(11):
                if fila == 0 or fila == 15 or columna == 0 or columna == 10:
                    casilla = QLabel(self)
                    casilla.setStyleSheet("background-color: #d1a77a")
                    ruta_foto = p.RUTA_BORDE
                    foto = QPixmap(ruta_foto); casilla.setPixmap(foto)
                    casilla.setScaledContents(True); casilla.setFixedSize(52, 52)
                    self.layout_grilla.addWidget(casilla, fila, columna)
                else:
                    casilla = QLabel(self); casilla.setFixedSize(52, 52)
                    casilla.setStyleSheet("background-color: #d1a77a")
                    self.layout_grilla.addWidget(casilla, fila, columna)                    
        self.layout_principal_horizontal.addWidget(self.widget_grilla)
        self.senal_instanciar_elementos.emit()

    def crear_luigi(self, f, c):
        print(f"Vamos a poner imagen luigi ({f}, {c})")
        self.label_luigi = QLabel(self); self.label_luigi.setObjectName("L_1")
        self.label_luigi.setPixmap(QPixmap(self.imagenes_luigi["F"][0])) 
        self.label_luigi.setScaledContents(True)
        self.label_luigi.setGeometry(QRect(QPoint(372 + 53 * c + c, 21 + 53 * f), QSize(53, 53)))
        self.dict_label_elementos["L"].append(self.label_luigi); self.label_luigi.show()

    def crear_estrella(self, f, c):
        print(f"Vamos a poner imagen estrella ({f}, {c})")
        self.label_estrella = QLabel(self); self.label_estrella.setObjectName("S_1")
        self.label_estrella.setPixmap(QPixmap(p.RUTA_ESTRELLA))
        self.label_estrella.setScaledContents(True)
        self.label_estrella.setGeometry(QRect(QPoint(372 + 53 * c + c, 21 + 53 * f), QSize(53, 53)))
        self.dict_label_elementos["S"].append(self.label_estrella); self.label_estrella.show()

    def crear_pared(self, f, c):
        print(f"Vamos a poner imagen pared ({f}, {c})")
        nombre = f"{f}_{c}"; self.label_pared = QLabel(self); self.label_pared.setObjectName(nombre)
        self.label_pared.setPixmap(QPixmap(p.RUTA_PARED)); self.label_pared.setScaledContents(True)
        self.label_pared.setGeometry(QRect(QPoint(372 + 53 * c + c, 21 + 53 * f), QSize(53, 53)))
        self.dict_label_elementos["P"].append(self.label_pared); self.label_pared.show()

    def crear_fuego(self, f, c):
        print(f"Vamos a poner imagen fuego ({f}, {c})")
        nombre = f"{f}_{c}"; self.label_fuego = QLabel(self); self.label_fuego.setObjectName(nombre)
        self.label_fuego.setPixmap(QPixmap(p.RUTA_FUEGO)) ;self.label_fuego.setScaledContents(True)
        self.label_fuego.setGeometry(QRect(QPoint(372 + 53 * c + c, 21 + 53 * f), QSize(53, 53)))
        self.dict_label_elementos["F"].append(self.label_fuego); self.label_fuego.show()
        
    def crear_roca(self, f, c, identificador):
        print(f"Vamos a poner imagen roca {identificador} en ({f}, {c})")
        nombre = f"R_{identificador}"; self.label_roca = QLabel(self)
        self.label_roca.setObjectName(nombre); self.label_roca.setPixmap(QPixmap(p.RUTA_ROCA)) 
        self.label_roca.setScaledContents(True)
        self.label_roca.setGeometry(QRect(QPoint(372 + 53 * c + c, 21 + 53 * f), QSize(53, 53)))
        self.dict_label_elementos["R"][nombre] = self.label_roca; self.label_roca.show()

    def crear_fantasma_horizontal(self, fila, columna, id):
        print(f"Vamos a poner imagen fantasma horizontal {id} en ({fila}, {columna})")
        nombre = f"H_{id}"; self.label_fantasma_horizontal = QLabel(self)
        self.label_fantasma_horizontal.setObjectName(nombre)
        self.label_fantasma_horizontal.setPixmap(QPixmap(p.RUTA_WHITE_GHOST_RIGHT_1)) 
        self.label_fantasma_horizontal.setScaledContents(True)
        self.label_fantasma_horizontal.setGeometry(QRect(QPoint(372 + 53 * columna + columna, 21 \
                                                                + 53 * fila), QSize(53, 53)))
        self.dict_label_elementos["H"][nombre] = self.label_fantasma_horizontal
        self.label_fantasma_horizontal.show()

    def crear_fantasma_vertical(self, fila, columna, id):
        print(f"Vamos a poner imagen fantasma vertical {id} en ({fila}, {columna})")
        nombre = f"V_{id}"; self.label_fantasma_vertical = QLabel(self)
        self.label_fantasma_vertical.setObjectName(nombre)
        self.label_fantasma_vertical.setPixmap(QPixmap(p.RUTA_RED_GHOST_VERTICAL_1)) 
        self.label_fantasma_vertical.setScaledContents(True)
        self.label_fantasma_vertical.setGeometry(QRect(QPoint(372 + 53 * columna + columna, 21 + \
                                                            53 * fila), QSize(53, 53)))
        self.dict_label_elementos["V"][nombre] = self.label_fantasma_vertical
        self.label_fantasma_vertical.show()

    def ganar_o_perder(self, booleano):
        self.ganado = booleano

    def keyPressEvent(self, event):
        if self.mover == False:
            if self.pausar_juego == False:
                if event.key() == Qt.Key_K:
                    self.k = True
                elif event.key() == Qt.Key_I and self.k:
                    self.i = True
                elif event.key() == Qt.Key_L and self.i:
                    print("K I L, eliminar villanos"); self.detener_thread_fantasmas()
                    self.eliminar_villanos(); self.senal_cheatcode.emit("KIL")
                    self.k, self.i, self.l, self.n, self.f = False, False, False, False, False
                elif event.key() == Qt.Key_I and not self.k:
                    self.i = True
                elif event.key() == Qt.Key_N and self.i:
                    self.n = True
                elif event.key() == Qt.Key_F and self.n:
                    print("I N F, congelar coontador"); self.senal_cheatcode.emit("INF")
                    self.k, self.i, self.l, self.n, self.f = False, False, False, False, False
                elif event.key() == Qt.Key_D:
                    self.senal_tecla.emit("R"); print("Derecha")
                    self.k, self.i, self.l, self.n, self.f = False, False, False, False, False
                elif event.key() == Qt.Key_W:
                    self.senal_tecla.emit("U"); print("Arriba")
                    self.k, self.i, self.l, self.n, self.f = False, False, False, False, False
                elif event.key() == Qt.Key_A:
                    self.senal_tecla.emit("L"); print("Izquierda")
                    self.k, self.i, self.l, self.n, self.f = False, False, False, False, False
                elif event.key() == Qt.Key_S:
                    self.senal_tecla.emit("D"); print("Abajo")
                    self.k, self.i, self.l, self.n, self.f = False, False, False, False, False
                elif event.key() == Qt.Key_G and self.ganado:
                    self.ocultar(); self.senal_ganar.emit(True); print("LLegamos a la estrella")
                else:
                    self.k, self.i, self.l, self.n, self.f = False, False, False, False, False
            if event.key() == Qt.Key_P and self.pausar_juego:
                self.reanudar()
                self.k, self.i, self.l, self.n, self.f = False, False, False, False, False
            elif event.key() == Qt.Key_P and not self.pausar_juego:
                self.pausa()
                self.k, self.i, self.l, self.n, self.f = False, False, False, False, False

    def mover_luigi(self, direccion, f_c, pos_antigua, media):
        n_p = (372 + 53 * f_c[1] + f_c[1], 21 + 53 * f_c[0])
        self.mover = True; self.label_luigi.setPixmap(QPixmap(self.imagenes_luigi[direccion][0]))
        thread_luigi = threading.Thread(name= "L", target= self.sprites_luigi, args=(direccion))
        self.dict_threads["L"] = thread_luigi; thread_luigi.start()
        if pos_antigua != n_p:
            self.mover = True
            self.anima_luigi = QPropertyAnimation(self.label_luigi, b"pos")
            self.anima_luigi.setDuration(160); self.anima_luigi.setEndValue(QPoint(n_p[0], n_p[1]))
            self.anima_luigi.start()
            self.anima_luigi.finished.connect(self.detener_animacion_luigi)
    
    def detener_animacion_luigi(self):
        self.mover = False 

    def sprites_luigi(self, d):
        for lugar in [0, 1, 2]:
            self.label_luigi.setPixmap(QPixmap(self.imagenes_luigi[d][lugar])); sleep(0.05)
        self.label_luigi.setPixmap(QPixmap(self.imagenes_luigi[d][0])); self.mover = False

    def mover_roca(self, identificador, f_c, pos_antigua):
        n_p = (372 + 53 * f_c[1] + f_c[1], 21 + 53 * f_c[0])
        llave = f"R_{identificador}"
        self.dict_label_elementos["R"][llave].setGeometry(\
            QRect(QPoint(n_p[0], n_p[1]), QSize(53, 53)))

    def mover_fantasma_horizontal(self, d, f_c, pos_antigua, id, media):
        n_p = (372 + 53 * f_c[1] + f_c[1], 21 + 53 * f_c[0])
        llave = f"H_{id}"
        if llave not in self.lista_fantasmas_horizontales_eliminados:
            label_f_h = self.dict_label_elementos["H"][llave]
            thread_f_h = threading.Thread(name= llave, target= self.sprites_f_horizontal, \
                                        args=(label_f_h, d))
            self.dict_threads[llave] = thread_f_h; thread_f_h.start()
            if id == 1:
                self.anima_f_h_1 = QPropertyAnimation(label_f_h, b"pos")
                self.anima_f_h_1.setDuration(100)
                self.anima_f_h_1.setEndValue(QPoint(n_p[0], n_p[1])); self.anima_f_h_1.start()
            elif id == 2:
                self.anima_f_h_2 = QPropertyAnimation(label_f_h, b"pos")
                self.anima_f_h_2.setDuration(100)
                self.anima_f_h_2.setEndValue(QPoint(n_p[0], n_p[1])); self.anima_f_h_2.start()
            elif id == 3:
                self.anima_f_h_3 = QPropertyAnimation(label_f_h, b"pos")
                self.anima_f_h_3.setDuration(100)
                self.anima_f_h_3.setEndValue(QPoint(n_p[0], n_p[1])); self.anima_f_h_3.start()
        print(self.dict_threads) 

    def sprites_f_horizontal(self, label, direccion):
        for lugar in [0, 1, 2]:
            label.setPixmap(QPixmap(self.imagenes_horizontal[direccion][lugar]))
            sleep(0.1)
        label.setPixmap(QPixmap(self.imagenes_horizontal[direccion][0]))

    def mover_fantasma_vertical(self, d, f_c, pos_antigua, id, media):
        n_p = (372 + 53 * f_c[1] + f_c[1], 21 + 53 * f_c[0])
        llave = f"V_{id}"
        if llave not in self.lista_fantasmas_verticales_eliminados:
            label_f_v = self.dict_label_elementos["V"][llave]
            thread_f_v = threading.Thread(name= llave, target= self.sprites_f_vertical, \
                                        args=(label_f_v, d))
            self.dict_threads[llave] = thread_f_v; thread_f_v.start()
            if id == 1:
                self.anima_f_v_1 = QPropertyAnimation(label_f_v, b"pos")
                self.anima_f_v_1.setDuration(100)
                self.anima_f_v_1.setEndValue(QPoint(n_p[0], n_p[1])); self.anima_f_v_1.start()
            elif id == 2:
                self.anima_f_v_2 = QPropertyAnimation(label_f_v, b"pos")
                self.anima_f_v_2.setDuration(100)
                self.anima_f_v_2.setEndValue(QPoint(n_p[0], n_p[1])); self.anima_f_v_2.start()
            elif id == 3:
                self.anima_f_v_3 = QPropertyAnimation(label_f_v, b"pos")
                self.anima_f_v_3.setDuration(100)
                self.anima_f_v_3.setEndValue(QPoint(n_p[0], n_p[1])); self.anima_f_v_3.start()
        print(self.dict_threads) 

    def sprites_f_vertical(self, label, d):
        for lugar in [0, 1, 2]:
            label.setPixmap(QPixmap(self.imagenes_vertical[1][lugar])); sleep(0.1)
        label.setPixmap(QPixmap(self.imagenes_vertical[1][0]))
              
    def detener_thread_fantasmas(self):
        if len(self.dict_threads.keys()) > 0:
            for llave in self.dict_threads.keys():
                if llave != "L":
                    self.dict_threads[llave].join()
                    print(f"Detuvimos thread {self.dict_threads[llave].name}")
        self.dict_threads = {}

    def eliminar_villanos(self):
        if len(self.dict_label_elementos["H"].keys()) > 0:
            for f_h in self.dict_label_elementos["H"].keys():
                if f_h not in self.lista_fantasmas_horizontales_eliminados:
                    self.dict_label_elementos["H"][f_h].clear()
                    self.lista_fantasmas_horizontales_eliminados.append(f_h)
        self.dict_label_elementos["H"] = {}
        if len(self.dict_label_elementos["V"].keys()) > 0:
            for f_v in self.dict_label_elementos["V"].keys():
                if f_v not in self.lista_fantasmas_verticales_eliminados:
                    self.dict_label_elementos["V"][f_v].clear()
                    self.lista_fantasmas_verticales_eliminados.append(f_v)
        self.dict_label_elementos["V"] = {}

    def eliminar_fantasma_horizontal(self, id):
        print(f"Vamos a eliminar fantasma horizontal {id}")
        nombre = f"H_{id}"
        self.dict_label_elementos["H"][nombre].clear(); self.dict_label_elementos["H"].pop(nombre)
        self.lista_fantasmas_horizontales_eliminados.append(nombre)

    def eliminar_fantasma_vertical(self, id):
        print(f"Vamos a eliminar fantasma vertical {id}")
        nombre = f"V_{id}"
        self.dict_label_elementos["V"][nombre].clear(); self.dict_label_elementos["V"].pop(nombre)
        self.lista_fantasmas_verticales_eliminados.append(nombre)

    def mostrar(self):
        self.senal_iniciar_tiempo.emit(); self.senal_iniciar_fantasmas.emit(); self.show()

    def ocultar(self):
        self.hide()

    def actualizar_informacion(self, vidas, tiempo):
        self.label_vida.hide()
        self.label_vida = QLabel(f"VIDAS:   {vidas}", self)
        self.label_vida.setFont(QFont("calibri", 12))
        self.label_vida.setGeometry(QRect(QPoint(20, 10), QSize(150, 42)))
        self.label_vida.show(); self.label_tiempo.hide()
        self.label_tiempo = QLabel(f"TIEMPO:   {int(tiempo)} segundos", self)
        self.label_tiempo.setFont(QFont("calibri", 12))
        self.label_tiempo.setGeometry(QRect(QPoint(20, 50), QSize(250, 42)))
        self.label_tiempo.show()

    def pausa(self):
        self.boton_reanudar.setEnabled(True); self.boton_pausa.setEnabled(False)
        self.pausar_juego = True; print("Vamos a pausar"); self.senal_pausa.emit()

    def reanudar(self):
        self.boton_reanudar.setEnabled(False); self.boton_pausa.setEnabled(True)
        self.pausar_juego = False; print("Vamos a reanudar"); self.senal_reanudar.emit()

    def limpiar_tablero(self):
        print("Voy a limpiar el tablero")
        self.pausar_juego = False
        for elemento in self.dict_label_elementos.keys():
            if elemento == "S":
                self.dict_label_elementos["S"].clear()
            elif elemento == "L":
                self.dict_label_elementos["L"][0].clear()
            elif elemento == "F" and len(self.dict_label_elementos["F"]) > 0:
                for fuego in self.dict_label_elementos["F"]:
                    fuego.clear()
            elif elemento == "P" and len(self.dict_label_elementos["P"]) > 0:
                for pared in self.dict_label_elementos["P"]:
                    pared.clear()
            elif elemento == "R" and len(self.dict_label_elementos["R"].keys()) > 0:
                for roca in self.dict_label_elementos["R"].keys():
                    self.dict_label_elementos["R"][roca].clear()
            elif elemento == "H" and len(self.dict_label_elementos["H"].keys()) > 0:
                for f_h in self.dict_label_elementos["H"].keys():
                    self.dict_label_elementos["H"][f_h].clear()
            elif elemento == "V" and len(self.dict_label_elementos["V"].keys()) > 0:
                for f_v in self.dict_label_elementos["V"].keys():
                    self.dict_label_elementos["V"][f_v].clear()
        self.dict_label_elementos = {"S": [], "L": [], "H": {}, "V": {}, "R": {}, "F": [], "P": []}
        self.k = False; self.i = False; self.l = False; self.n = False; self.f = False
        self.ganado = False; self.lista_fantasmas_horizontales_eliminados = []
        self.lista_fantasmas_verticales_eliminados = []
    
    def salir(self):
        self.hide()
        sys.exit()