from PyQt5.QtCore import QObject, pyqtSignal, QTimer
from backend.clases_objetos import Luigi, Roca, FantasmaHorizontal, FantasmaVertical
from backend.funciones import procesar_archivo, calcular_posicion_futura
import parametros as p; import random

class LogicaJuego(QObject):
    senal_iniciar_juego_ventana = pyqtSignal(); senal_mostrar_ventana_juego = pyqtSignal()
    senal_crear_luigi = pyqtSignal(int, int); senal_crear_estrella = pyqtSignal(int, int)
    senal_crear_pared = pyqtSignal(int, int); senal_crear_fuego = pyqtSignal(int, int)
    senal_crear_roca = pyqtSignal(int, int, int)
    senal_crear_fantasma_horizontal = pyqtSignal(int, int, int)
    senal_crear_fantasma_vertical = pyqtSignal(int, int, int)
    senal_mover_luigi = pyqtSignal(str, tuple, tuple, tuple)
    senal_mover_roca = pyqtSignal(int, tuple, tuple) 
    senal_mover_fantasma_horizontal = pyqtSignal(int, tuple, tuple, int, tuple) 
    senal_mover_fantasma_vertical = pyqtSignal(int, tuple, tuple, int, tuple) 
    senal_eliminar_fantasma_horizontal = pyqtSignal(int)
    senal_eliminar_fantasma_vertical = pyqtSignal(int)
    senal_luigi_en_estrella = pyqtSignal(bool); senal_tiempo_vidas = pyqtSignal(int, int)
    senal_reiniciar_juego = pyqtSignal(); senal_terminar_juego = pyqtSignal()
    senal_terminar_juego_logica = pyqtSignal(str, str, bool) 
    senal_terminar_juego_ventana = pyqtSignal(int, int, int, str, bool) 

    def __init__(self):
        super().__init__(); self.definir_atributos()

    def definir_atributos(self):
        self.identificador_roca = 0; self.identificador_fantasma_horizontal = 0
        self.identificador_fantasma_vertical = 0
        self.lista_elementos = None; self.dict_tupla_elementos_inicial = {}
        self.dict_tupla_elementos = {"S": [], "L": [], "H": [], "V": [], "R": [], "F": [], "P": []}
        self.dict_instancias_elementos = {"S": [], "L": [], "H": {}, "V": {}, "R": {}, "F": [], \
            "P": []}; self.posicion_estrella = (); self.cheatcode = False
        self.lista_horizontales_eliminados = []; self.lista_verticales_eliminados = [] 
        self.vidas = p.CANTIDAD_VIDAS; self.vidas_ocupadas = 0; self.puntaje_total = 0
        self.vidas_inicial = p.CANTIDAD_VIDAS; self.tiempo_restante = p.TIEMPO_CUENTA_REGRESIVA 

    def definir_nombre(self, nombre, actual):
        self.nombre = nombre; self.archivo = actual; self.nombre_archivo(self.archivo)

    def nombre_archivo(self, archivo):
        self.lista_elementos = procesar_archivo(archivo)
        for f in range(16): ########################## creamos diccionario #############
            for c in range(11):
                if self.lista_elementos[f][c] == "L":
                    self.dict_tupla_elementos["L"].append((f, c))
                elif self.lista_elementos[f][c] == "S":
                    self.dict_tupla_elementos["S"].append((f, c)); self.posicion_estrella = (f, c)
                elif self.lista_elementos[f][c] == "H":
                    self.dict_tupla_elementos["H"].append((f, c))
                elif self.lista_elementos[f][c] == "V":
                    self.dict_tupla_elementos["V"].append((f, c))
                elif self.lista_elementos[f][c] == "F":
                    self.dict_tupla_elementos["F"].append((f, c))
                elif self.lista_elementos[f][c] == "R":
                    self.dict_tupla_elementos["R"].append((f, c))
                elif self.lista_elementos[f][c] == "P":
                    self.dict_tupla_elementos["P"].append((f, c))
        self.dict_tupla_elementos_inicial = self.dict_tupla_elementos; self.instanciar_elementos()

    def instanciar_elementos(self):
        for llave in self.dict_tupla_elementos.keys():
            if len(self.dict_tupla_elementos[llave]) > 0 and llave != "L":
                if llave == "S":
                    print("voy a instanciar a estrella"); self.instanciar_estrella()
                if llave == "P":
                    for elemento in self.dict_tupla_elementos["P"]:
                        print(f"Voy a instanciar pared ({elemento[0]}, {elemento[1]})")
                        self.instanciar_pared(elemento[0], elemento[1])
                if llave == "F":
                    for elemento in self.dict_tupla_elementos["F"]:
                        print(f"Voy a instanciar fuego ({elemento[0]}, {elemento[1]})")
                        self.instanciar_fuego(elemento[0], elemento[1])
                if llave == "R":
                    for elemento in self.dict_tupla_elementos["R"]:
                        print(f"Voy a instanciar roca ({elemento[0]}, {elemento[1]})")
                        self.identificador_roca += 1
                        self.instanciar_roca(elemento[0], elemento[1], self.identificador_roca)
                if llave == "H":
                    for elemento in self.dict_tupla_elementos["H"]:
                        print(f"Voy a instanciar f horizontal ({elemento[0]}, {elemento[1]})")
                        self.identificador_fantasma_horizontal += 1
                        self.instanciar_fantasma_horizontal(elemento[0], elemento[1], \
                                                        self.identificador_fantasma_horizontal)
                if llave == "V":
                    for elemento in self.dict_tupla_elementos["V"]:
                        print(f"Voy a instanciar f vertical ({elemento[0]}, {elemento[1]})")
                        self.identificador_fantasma_vertical += 1
                        self.instanciar_fantasma_vertical(elemento[0], elemento[1], \
                                                        self.identificador_fantasma_vertical)
        print("voy a instanciar a luigi")
        self.instanciar_luigi(); self.instanciar_timer(); self.senal_iniciar_juego_ventana.emit()

    def instanciar_timer(self):
        self.subtick = 0; self.timer = QTimer()
        self.timer.timeout.connect(self.timer_tick); self.timer.setInterval(int(1000))
        ponderador_velocidad_fantasmas = random.uniform(p.MIN_VELOCIDAD, p.MAX_VELOCIDAD)
        tiempo_movimiento_fantasmas = 1 / ponderador_velocidad_fantasmas
        if len(self.dict_instancias_elementos["H"].keys()) > 0:
            self.timer_fantasma_horizontal = QTimer()
            self.timer_fantasma_horizontal.timeout.connect(self.avanzar_fantasma_horizontal)
            self.timer_fantasma_horizontal.setInterval(int(tiempo_movimiento_fantasmas)) 
        if len(self.dict_instancias_elementos["V"].keys()) > 0:
            self.timer_fantasma_vertical = QTimer()
            self.timer_fantasma_vertical.timeout.connect(self.avanzar_fantasma_vertical)
            self.timer_fantasma_vertical.setInterval(int(tiempo_movimiento_fantasmas)) 

    def iniciar_timer_tiempo(self):
        if self.cheatcode == False:
            self.timer.start()
    
    def iniciar_timer_fantasmas(self):
        if len(self.dict_instancias_elementos["H"].keys()) > 0:
            self.timer_fantasma_horizontal.start()
        if len(self.dict_instancias_elementos["V"].keys()) > 0:
            self.timer_fantasma_vertical.start()

    def detener_timer_tiempo(self):
        self.timer.stop()
    
    def detener_timer_fantasmas(self):
        if len(self.dict_instancias_elementos["H"].keys()) > 0:
            self.timer_fantasma_horizontal.stop()
        if len(self.dict_instancias_elementos["V"].keys()) > 0:
            self.timer_fantasma_vertical.stop()
        
    def instanciar_luigi(self):
        f_l = self.dict_tupla_elementos["L"][0][0]; c_l = self.dict_tupla_elementos["L"][0][1]
        self.dict_instancias_elementos["L"].append(Luigi(f_l, c_l))
        self.senal_crear_luigi.emit(f_l, c_l)
    
    def instanciar_estrella(self):
        self.dict_instancias_elementos["S"].append(self.posicion_estrella)
        self.senal_crear_estrella.emit(self.posicion_estrella[0], self.posicion_estrella[1])

    def instanciar_pared(self, f, c):
        self.dict_instancias_elementos["P"].append((f, c)); self.senal_crear_pared.emit(f, c)

    def instanciar_fuego(self, f, c):
        self.dict_instancias_elementos["F"].append((f, c)); self.senal_crear_fuego.emit(f, c)

    def instanciar_roca(self, f, c, id):
        self.dict_instancias_elementos["R"][id] = Roca(f, c, id)
        self.senal_crear_roca.emit(f, c, id)

    def instanciar_fantasma_horizontal(self, fila, columna, id):
        self.dict_instancias_elementos["H"][id] = FantasmaHorizontal(fila, columna, id)
        self.senal_crear_fantasma_horizontal.emit(fila, columna, id)

    def instanciar_fantasma_vertical(self, fila, columna, id):
        self.dict_instancias_elementos["V"][id] = FantasmaVertical(fila, columna, id)
        self.senal_crear_fantasma_vertical.emit(fila, columna, id)

    def timer_tick(self):
        self.subtick += 1; self.tiempo_restante -= 1
        if not self.verificar_seguir(): #### aca perdemos por vida o tiempo
            self.ganar_perder(False)
        print(f"VIDAS: {self.vidas}, OCUPADAS: {self.vidas_ocupadas}")
        self.senal_tiempo_vidas.emit(self.vidas, self.tiempo_restante)

    def verificar_seguir(self):
        devolver = True
        if self.vidas <= 0:
            devolver = False
        elif self.tiempo_restante <= 0:
            devolver = False
        return devolver

    def cambiar_direccion_luigi(self, direccion):
        self.dict_instancias_elementos["L"][0].cambiar_direccion(direccion)

    def avanzar_luigi(self):
        choca_con_pared = False; choca_con_fuego = False; choca_con_roca = False
        direccion_luigi = self.dict_instancias_elementos["L"][0].obtener_direccion()
        f_l = self.dict_instancias_elementos["L"][0].fila
        c_l = self.dict_instancias_elementos["L"][0].columna
        fila_luigi, columna_luigi = calcular_posicion_futura("L", direccion_luigi, f_l, c_l)
        ### estrella
        fila_estrella = self.posicion_estrella[0]; columna_estrella = self.posicion_estrella[1]
        if fila_estrella == fila_luigi and columna_estrella == columna_luigi:
            direccion, f_c, pos, media = self.dict_instancias_elementos["L"][0].avanzar()
            self.senal_mover_luigi.emit(direccion, f_c, pos, media)
            self.senal_luigi_en_estrella.emit(True)
        else:
            self.senal_luigi_en_estrella.emit(False)
            ### pared
            if len(self.dict_instancias_elementos["P"]) > 0:
                for pared in self.dict_instancias_elementos["P"]:
                    if pared[0] == fila_luigi and pared[1] == columna_luigi:
                        choca_con_pared = True
            ### fuego
            if len(self.dict_instancias_elementos["F"]) > 0:
                for fuego in self.dict_instancias_elementos["F"]:
                    if fuego[0] == fila_luigi and fuego[1] == columna_luigi:
                        choca_con_fuego = True
                        if self.cheatcode == False:
                            self.vidas -= 1; self.vidas_ocupadas += 1
                        print(f"Luigi va a chocar con fuego en casilla ({fuego[0]}, {fuego[1]})")
            if choca_con_fuego:
                direccion, f_c, pos, media = self.dict_instancias_elementos["L"][0].avanzar()
                self.senal_mover_luigi.emit(direccion, f_c, pos, media)
                if self.vidas > 0:
                    self.reiniciar()
            ### roca
            if self.identificador_roca > 0:
                print(f"Debemos verificar rocas, hay {self.identificador_roca} en el tablero")
                for llave in self.dict_instancias_elementos["R"].keys():
                    roca_revisando = self.dict_instancias_elementos["R"][llave]
                    if roca_revisando.fila == fila_luigi and roca_revisando.columna == \
                        columna_luigi:
                        print("Luigi se movió a una celda donde hay roca")
                        choca_con_roca = True
                        roca_revisando.cambiar_direccion(direccion_luigi) 
                        resultado, segunda_roca = self.verificar_movimiento_roca(roca_revisando, \
                                                                                True)  
                        if resultado:
                            if segunda_roca == False:
                                print("Movemos luigi")
                                direccion, f_c, pos, media = self.dict_instancias_elementos["L"][0\
                                                                                        ].avanzar()
                                print("Falta hacer mover a roca"); self.avanzar_roca(roca_revisando)
                                self.senal_mover_luigi.emit(direccion, f_c, pos, media)
                            else:
                                print("Vamos a mover a luigi y las dos rocas")
                                for llave in self.dict_instancias_elementos["R"].keys():
                                    roca_revisando = self.dict_instancias_elementos["R"][llave]
                                    self.avanzar_roca(roca_revisando) 
                                direccion, f_c, pos, media = self.dict_instancias_elementos["L"][0\
                                                                                        ].avanzar()
                                self.senal_mover_luigi.emit(direccion, f_c, pos, media)      
            if choca_con_pared == False and choca_con_fuego == False and choca_con_roca == False:
                direccion, f_c, pos, media = self.dict_instancias_elementos["L"][0].avanzar()
                self.senal_mover_luigi.emit(direccion, f_c, pos, media)

    def avanzar_roca(self, i_roca):
        f_c, pos = i_roca.avanzar(); self.senal_mover_roca.emit(i_roca.identificador, f_c, pos)

    def avanzar_fantasma_horizontal(self):
        lista_eliminar = []; choca_luigi = False
        if len(self.dict_instancias_elementos["H"].keys()) > 0:
            for llave in self.dict_instancias_elementos["H"].keys():
                print(f"Vamos a mover fantasma horizontal {llave}")
                instancia = self.dict_instancias_elementos["H"][llave]
                direccion_fh = instancia.obtener_direccion()
                f_fh = instancia.fila; c_fh = instancia.columna
                fila_fh, columna_fh = calcular_posicion_futura("H", direccion_fh, f_fh, c_fh)
                if len(self.dict_instancias_elementos["P"]) > 0:
                    for pared in self.dict_instancias_elementos["P"]:
                        if pared[0] == fila_fh and pared[1] == columna_fh:
                            if instancia.direccion == 1:
                                instancia.direccion = -1
                            elif instancia.direccion == -1:
                                instancia.direccion = 1
                if self.identificador_roca > 0:
                    for roca in self.dict_instancias_elementos["R"].keys():
                        roca_revisando = self.dict_instancias_elementos["R"][roca]
                        if fila_fh == roca_revisando.fila and columna_fh == roca_revisando.columna:
                            if instancia.direccion == 1:
                                instancia.direccion = -1
                            elif instancia.direccion == -1:
                                instancia.direccion = 1
                if len(self.dict_instancias_elementos["F"]) > 0:
                    for fuego in self.dict_instancias_elementos["F"]:
                        if fuego[0] == fila_fh and fuego[1] == columna_fh:
                            id = instancia.identificador
                            self.lista_horizontales_eliminados.append(id); lista_eliminar.append(id)
                            self.senal_eliminar_fantasma_horizontal.emit(id)
                if fila_fh == self.dict_instancias_elementos["L"][0].fila and columna_fh == \
                    self.dict_instancias_elementos["L"][0].columna:
                    choca_luigi = True; direccion, f_c, pos, media = instancia.avanzar()
                    self.senal_mover_fantasma_horizontal.emit(direccion, f_c, pos, llave, media)
                    if self.cheatcode == False:
                        self.vidas -= 1; self.vidas_ocupadas += 1
                if choca_luigi:
                    self.reiniciar()
                else:
                    direccion, f_c, pos, media = instancia.avanzar()
                    self.senal_mover_fantasma_horizontal.emit(direccion, f_c, pos, llave, media)
            if len(lista_eliminar) > 0:
                for id in lista_eliminar:
                    self.dict_instancias_elementos["H"].pop(id)

    def avanzar_fantasma_vertical(self):
        lista_eliminar = []; choca_luigi = False
        if len(self.dict_instancias_elementos["V"].keys()) > 0:
            for llave in self.dict_instancias_elementos["V"].keys():
                print(f"Vamos a mover fantasma vertical {llave}")
                instancia = self.dict_instancias_elementos["V"][llave]
                direccion_fv = instancia.obtener_direccion()
                f_fv = instancia.fila; c_fv = instancia.columna
                fila_fv, columna_fv = calcular_posicion_futura("V", direccion_fv, f_fv, c_fv)
                if len(self.dict_instancias_elementos["P"]) > 0:
                    for pared in self.dict_instancias_elementos["P"]:
                        if pared[0] == fila_fv and pared[1] == columna_fv:
                            if instancia.direccion == 1:
                                instancia.direccion = -1
                            elif instancia.direccion == -1:
                                instancia.direccion = 1
                if self.identificador_roca > 0:
                    for roca in self.dict_instancias_elementos["R"].keys():
                        roca_revisando = self.dict_instancias_elementos["R"][roca]
                        if fila_fv == roca_revisando.fila and columna_fv == roca_revisando.columna:
                            if instancia.direccion == 1:
                                instancia.direccion = -1
                            elif instancia.direccion == -1:
                                instancia.direccion = 1
                if len(self.dict_instancias_elementos["F"]) > 0:
                    for fuego in self.dict_instancias_elementos["F"]:
                        if fuego[0] == fila_fv and fuego[1] == columna_fv:
                            id = instancia.identificador
                            self.lista_verticales_eliminados.append(id); lista_eliminar.append(id)
                            self.senal_eliminar_fantasma_vertical.emit(id)
                if fila_fv == self.dict_instancias_elementos["L"][0].fila and columna_fv == \
                    self.dict_instancias_elementos["L"][0].columna:
                    choca_luigi = True; direccion, f_c, pos, media = instancia.avanzar()
                    self.senal_mover_fantasma_vertical.emit(direccion, f_c, pos, llave, media)
                    if self.cheatcode == False:
                        self.vidas -= 1; self.vidas_ocupadas += 1
                if choca_luigi:
                    self.reiniciar()
                else:
                    direccion, f_c, pos, media = instancia.avanzar()
                    self.senal_mover_fantasma_vertical.emit(direccion, f_c, pos, llave, media)
            if len(lista_eliminar) > 0:
                for id in lista_eliminar:
                    self.dict_instancias_elementos["V"].pop(id)

    def aplicar_cheatcode(self, string):
        if string == "KIL":
            self.cheatcode = False; self.iniciar_timer_tiempo()
            if len(self.dict_instancias_elementos["H"].keys()) > 0:
                for f_h in self.dict_instancias_elementos["H"].keys():
                    if f_h not in self.lista_horizontales_eliminados:
                        self.lista_horizontales_eliminados.append(f_h)
                self.dict_instancias_elementos["H"] = {}
            if len(self.dict_instancias_elementos["V"].keys()) > 0:
                for f_v in self.dict_instancias_elementos["V"].keys():
                    if f_v not in self.lista_verticales_eliminados:
                        self.lista_verticales_eliminados.append(f_v)
                self.dict_instancias_elementos["V"] = {}
        elif string == "INF":
            self.detener_timer_tiempo(); self.cheatcode = True

    def verificar_movimiento_roca(self, i_roca, primera_vez):
        primera_vez_revisando = primera_vez
        posicion_antigua = (i_roca.posicion_X(), i_roca.posicion_Y())
        print(f"Posicion antigua roca : {posicion_antigua}")
        choca_con_pared = False; choca_con_roca = False; mover_segunda_roca = False
        direccion_roca = i_roca.obtener_direccion(); f_roca = i_roca.fila; c_roca = i_roca.columna
        fila_roca, columna_roca = calcular_posicion_futura("R", direccion_roca, f_roca, c_roca)

        if len(self.dict_instancias_elementos["P"]) > 0:
            for pared in self.dict_instancias_elementos["P"]:
                if pared[0] == fila_roca and pared[1] == columna_roca:
                    choca_con_pared = True
        if self.identificador_roca == 2 and primera_vez_revisando == True:
            print("Debemos verificar la posicion de la segunda roca")
            for llave in self.dict_instancias_elementos["R"].keys():
                if llave != i_roca.identificador:
                    roca_revisando = self.dict_instancias_elementos["R"][llave]
                    if roca_revisando.fila == fila_roca and roca_revisando.columna == columna_roca:
                        choca_con_roca = True; roca_revisando.cambiar_direccion(direccion_roca) 
                        resultado, segunda_roca = self.verificar_movimiento_roca(roca_revisando, \
                                                                                False)
                        if resultado:
                            print("Movemos ambas rocas y luigi"); mover_segunda_roca = True
                        else:
                            print("No podemos mover a la roca primera") 
                            return False, mover_segunda_roca
        posicion_nueva = (372 + 53 * columna_roca + columna_roca, 21 + 53 * fila_roca)
        print(f"Posicion nueva roca: {posicion_nueva}")
        if posicion_antigua == posicion_nueva or choca_con_pared:
            return False, mover_segunda_roca
        else:
            return True, mover_segunda_roca     

    def reiniciar(self):
        if self.cheatcode == False:
            self.tiempo_restante = 120
        self.identificador_roca = 0; self.identificador_fantasma_horizontal = 0
        self.identificador_fantasma_vertical = 0
        self.lista_horizontales_eliminados = []; self.lista_verticales_eliminados = []
        self.dict_instancias_elementos = {"S": [], "L": [], "H": {}, "V": {}, "R": {}, "F": [], \
            "P": []}; self.senal_reiniciar_juego.emit(); self.instanciar_elementos() 

    def pausar_juego(self):
        self.detener_timer_tiempo(); self.detener_timer_fantasmas()

    def reanudar_juego(self):
        self.iniciar_timer_tiempo(); self.iniciar_timer_fantasmas()

    def ganar_perder(self, booleano):
        if self.vidas_ocupadas == 0:
            self.vidas_ocupadas += 1; self.vidas -= 1
        print(f"NO HAY QUE SEGUIIIIR"); self.detener_timer_tiempo(); self.detener_timer_fantasmas()
        self.senal_terminar_juego.emit()
        self.senal_terminar_juego_logica.emit(self.nombre, self.archivo, booleano)
        self.senal_terminar_juego_ventana.emit(self.tiempo_restante, self.vidas, int((\
            self.tiempo_restante * p.MULTIPLICADOR_PUNTAJE) / (self.vidas_ocupadas)), self.nombre,\
            booleano); self.senal_reiniciar_juego.emit(); self.definir_atributos()        