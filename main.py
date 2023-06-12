import sys
from PyQt5.QtWidgets import QApplication
from frontend.ventana_inicio import VentanaInicio
from frontend.ventana_constructor import VentanaConstructor
from frontend.ventana_juego import VentanaJuego
from frontend.ventana_derrota import VentanaDerrota
from backend.logica_inicio import LogicaInicio
from backend.logica_constructor import LogicaConstructor
from backend.logica_juego import LogicaJuego
from backend.logica_derrota import LogicaDerrota

class DCCazafantasmas(QApplication):

    def __init__(self, argv):
        super().__init__(argv)

        self.ventana_inicio = VentanaInicio()
        self.ventana_constructor = VentanaConstructor()
        self.ventana_juego = VentanaJuego()
        self.ventana_derrota = VentanaDerrota()
        self.logica_inicio = LogicaInicio()
        self.logica_constructor = LogicaConstructor()
        self.logica_juego = LogicaJuego()
        self.logica_derrota = LogicaDerrota()

    def conectar(self):

        ### ventana inicio
        self.ventana_inicio.senal_verificar_usuario.connect(self.logica_inicio.comprobar_nombre)
        self.ventana_inicio.senal_iniciar_constructor.connect(self.ventana_constructor.mostrar)
        self.ventana_inicio.senal_iniciar_constructor.connect(\
            self.logica_constructor.definir_nombre)
        self.ventana_inicio.senal_iniciar_juego.connect(self.logica_juego.definir_nombre)

        ### ventana constructora
        self.ventana_constructor.senal_dificultad.connect(\
            self.logica_constructor.elementos_comboBox)
        self.ventana_constructor.senal_boton_actual_izquierdo.connect(\
            self.logica_constructor.obtener_boton_izquierdo)
        self.ventana_constructor.senal_casilla_presionada.connect(self.logica_constructor.contar)
        self.ventana_constructor.senal_agregar_letra_tablero.connect(\
            self.logica_constructor.agregar_letra)
        self.ventana_constructor.senal_revisar_luigi_y_estrella.connect(\
            self.logica_constructor.revisar_tablero)
        self.ventana_constructor.senal_crear_txt.connect(self.logica_constructor.crear_archivo)
        self.ventana_constructor.senal_pedir_botones_presionados.connect(\
            self.logica_constructor.entregar_botones_presionados)

        ### ventana juego
        self.ventana_juego.senal_instanciar_elementos.connect(\
            self.logica_juego.instanciar_elementos)
        self.ventana_juego.senal_tecla.connect(self.logica_juego.cambiar_direccion_luigi)
        self.ventana_juego.senal_tecla.connect(self.logica_juego.avanzar_luigi)
        self.ventana_juego.senal_iniciar_tiempo.connect(self.logica_juego.iniciar_timer_tiempo)
        self.ventana_juego.senal_iniciar_fantasmas.connect(\
            self.logica_juego.iniciar_timer_fantasmas)
        self.ventana_juego.senal_pausa.connect(self.logica_juego.pausar_juego)
        self.ventana_juego.senal_reanudar.connect(self.logica_juego.reanudar_juego)
        self.ventana_juego.senal_cheatcode.connect(self.logica_juego.aplicar_cheatcode)
        self.ventana_juego.senal_ganar.connect(self.logica_juego.ganar_perder)

        ### ventana derrota
        self.ventana_derrota.senal_inicio_musica.connect(self.logica_derrota.comenzar_musica)
        self.ventana_derrota.senal_detener_musica.connect(self.logica_derrota.stop_musica)
        self.ventana_derrota.senal_volver_jugar.connect(self.logica_derrota.volver_jugar)

        ### logica inicio
        self.logica_inicio.senal_respuesta_validacion.connect(\
            self.ventana_inicio.recibir_validacion)
        
        ### logica constructor
        self.logica_constructor.senal_todos.connect(self.ventana_constructor.todos)
        self.logica_constructor.senal_bloque.connect(self.ventana_constructor.bloque)
        self.logica_constructor.senal_entidad.connect(self.ventana_constructor.entidad)
        self.logica_constructor.senal_pop_up_error.connect(\
            self.ventana_constructor.pop_up_error_constructor)
        self.logica_constructor.senal_agregar_elemento.connect(\
            self.ventana_constructor.agregar_elemento_tablero)
        self.logica_constructor.senal_revision_tablero.connect(\
            self.ventana_constructor.respuesta_revision)
        self.logica_constructor.senal_entregar_botones.connect(\
            self.ventana_constructor.limpiar_lables_grilla)
        self.logica_constructor.senal_ocultar_ventana.connect(\
            self.ventana_constructor.ocultar)
        self.logica_constructor.senal_iniciar_juego_constructor.connect(\
            self.logica_juego.definir_nombre)

        ### logica juego
        self.logica_juego.senal_iniciar_juego_ventana.connect(self.ventana_juego.mostrar)
        self.logica_juego.senal_crear_luigi.connect(self.ventana_juego.crear_luigi)
        self.logica_juego.senal_crear_estrella.connect(self.ventana_juego.crear_estrella)
        self.logica_juego.senal_crear_pared.connect(self.ventana_juego.crear_pared)
        self.logica_juego.senal_crear_fuego.connect(self.ventana_juego.crear_fuego)
        self.logica_juego.senal_crear_roca.connect(self.ventana_juego.crear_roca)
        self.logica_juego.senal_crear_fantasma_horizontal.connect(\
            self.ventana_juego.crear_fantasma_horizontal)
        self.logica_juego.senal_crear_fantasma_vertical.connect(\
            self.ventana_juego.crear_fantasma_vertical)
        self.logica_juego.senal_mover_luigi.connect(self.ventana_juego.mover_luigi)
        self.logica_juego.senal_mover_roca.connect(self.ventana_juego.mover_roca)
        self.logica_juego.senal_mover_fantasma_horizontal.connect(\
            self.ventana_juego.mover_fantasma_horizontal)
        self.logica_juego.senal_mover_fantasma_vertical.connect(\
            self.ventana_juego.mover_fantasma_vertical)
        self.logica_juego.senal_eliminar_fantasma_horizontal.connect(\
            self.ventana_juego.eliminar_fantasma_horizontal)
        self.logica_juego.senal_eliminar_fantasma_vertical.connect(\
            self.ventana_juego.eliminar_fantasma_vertical)
        self.logica_juego.senal_luigi_en_estrella.connect(self.ventana_juego.ganar_o_perder)
        self.logica_juego.senal_tiempo_vidas.connect(self.ventana_juego.actualizar_informacion)
        self.logica_juego.senal_reiniciar_juego.connect(self.ventana_juego.detener_thread_fantasmas)
        self.logica_juego.senal_reiniciar_juego.connect(self.ventana_juego.limpiar_tablero)
        self.logica_juego.senal_terminar_juego.connect(self.ventana_juego.detener_thread_fantasmas)
        self.logica_juego.senal_terminar_juego.connect(self.ventana_juego.limpiar_tablero)
        self.logica_juego.senal_terminar_juego.connect(self.ventana_juego.ocultar)
        self.logica_juego.senal_terminar_juego_logica.connect(self.logica_derrota.definir_nombre)
        self.logica_juego.senal_terminar_juego_ventana.connect(self.ventana_derrota.mostrar)

        ### logica derrota
        self.logica_derrota.senal_iniciar_juego.connect(self.logica_juego.definir_nombre)

    def comenzar_juego(self):
        self.ventana_inicio.mostrar()

if __name__ == '__main__':
    def hook(type, traceback):
        print(type)
        print(traceback)
    sys.__excepthook__ = hook
    app = DCCazafantasmas([])
    app.conectar()
    app.comenzar_juego()
    sys.exit(app.exec())
    
