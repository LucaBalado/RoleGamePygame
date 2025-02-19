import pygame
from pygame.locals import *
import pathlib as pl

ANCHO, ALTO = 800, 600
TAMANIO_CUADRILLA = 32
COLOR_CUADRILLA = (200, 200, 200)
COLOR_BTN = (100, 100, 255)
COLOR_BTN_PRESIONADO = (255, 100, 100)
PORCENTAJE_OCUPACION = 0.7
TAMANO_BOTON = (150, 50)  
COLOR_FONDO_SUBMENU=(255,255,255)
rangomover= 3

class Pelea:
    def __init__(self, juego, fondo_path, sprite_path):
        pygame.init()
        self.juego = juego
        self.screen = pygame.display.set_mode((ANCHO, ALTO))
        pygame.display.set_caption("Campo de Batalla")
        fondo = pl.Path(fondo_path)
        fondo.resolve()
        sprite = pl.Path(sprite_path)
        sprite.resolve()
        try:

            self.fondo = pygame.image.load(fondo)
            self.fondo = pygame.transform.scale(self.fondo, (ANCHO, ALTO))
        except pygame.error as e:
            print(f"Error cargando la imagen de fondo: {e}")
            exit()


        try:
            self.sprite_orco = pygame.image.load(sprite)
            self.sprite_orco = pygame.transform.scale(self.sprite_orco, (TAMANIO_CUADRILLA, TAMANIO_CUADRILLA))
        except pygame.error as e:
            print(f"Error cargando la imagen del sprite: {e}")
            exit()


        self.cuadras = []
        self.offset_x = 0
        self.offset_y = 0
        self.botones = []
        self.radio_movimiento = rangomover
        self.movimiento_activo = False
        self.casillas_movimiento = []
        self.orco_pos = (4, 4)  
        self.movimientos_realizados = 0
        self.turno_jugador = True
        self.turno_enemigo = False
        self.mostrar_submenu = False
        self.submenu_tipo = None
        if self.juego.clase == "Hechicero":
            self.acciones = {
               'accion': ["Tiro Con Arco", "Bola de Fuego"],
               'accion_adicional': ["Aumentar Armadura", "Curación"]
            }
        else:
            self.acciones ={
                'accion': ["Ataque Normal", "Ataque Doble"],
                'accion_adicional': ["Circulo de Defensa", "Aumentar Armadura"]
            }
        self.submenu_opciones = []
        self.accion_utilizada = False
        self.accion_adicional_utilizada = False                      
       

    def crear_cuadrillas(self):
        filas = int((ALTO * PORCENTAJE_OCUPACION) // TAMANIO_CUADRILLA)
        columnas = int((ANCHO * PORCENTAJE_OCUPACION) // TAMANIO_CUADRILLA)


        self.offset_x = (ANCHO - (columnas * TAMANIO_CUADRILLA)) // 2
        self.offset_y = (ALTO - (filas * TAMANIO_CUADRILLA)) // 2


        for y in range(1, filas):
            for x in range(columnas):
                self.cuadras.append((
                    self.offset_x + x * TAMANIO_CUADRILLA,
                    self.offset_y + y * TAMANIO_CUADRILLA
                ))


    def crear_botones(self):
        boton_espaciado = 20
        x_inicial = (ANCHO - (4 * TAMANO_BOTON[0] + 3 * boton_espaciado)) // 2


        self.botones.append(pygame.Rect(x_inicial, ALTO - 100, *TAMANO_BOTON))  # Acción
        self.botones.append(pygame.Rect(x_inicial + TAMANO_BOTON[0] + boton_espaciado, ALTO - 100, *TAMANO_BOTON))  # Acción Adicional
        self.botones.append(pygame.Rect(x_inicial + 2 * (TAMANO_BOTON[0] + boton_espaciado), ALTO - 100, *TAMANO_BOTON))  # Mover
        self.botones.append(pygame.Rect(x_inicial + 3 * (TAMANO_BOTON[0] + boton_espaciado), ALTO - 100, *TAMANO_BOTON))  # Terminar Turno




    def dibujar_escenario(self):
        self.screen.blit(self.fondo, (0, 0))


        for cuad in self.cuadras:
            pygame.draw.rect(self.screen, COLOR_CUADRILLA,
                             (*cuad, TAMANIO_CUADRILLA, TAMANIO_CUADRILLA), 1)


        orco_pos_x = self.offset_x + self.orco_pos[0] * TAMANIO_CUADRILLA
        orco_pos_y = self.offset_y + self.orco_pos[1] * TAMANIO_CUADRILLA
        self.screen.blit(self.sprite_orco, (orco_pos_x, orco_pos_y))
        self.crear_botones()
        if self.movimiento_activo:
            self.dibujar_movimiento()



    def dibujar_texto(self, texto, rect):
        font = pygame.font.Font(None, 30)
        text_surface = font.render(texto, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=rect.center)
        self.screen.blit(text_surface, text_rect)


    def dibujar_movimiento(self):
        orco_pos_x = self.offset_x + self.orco_pos[0] * TAMANIO_CUADRILLA
        orco_pos_y = self.offset_y + self.orco_pos[1] * TAMANIO_CUADRILLA


        self.casillas_movimiento.clear()


        for y in range(-self.radio_movimiento, self.radio_movimiento + 1):
            for x in range(-self.radio_movimiento, self.radio_movimiento + 1):
                if abs(x) + abs(y) <= self.radio_movimiento:
                    casilla_x = self.orco_pos[0] + x
                    casilla_y = self.orco_pos[1] + y


                    if 0 <= casilla_x < len(self.cuadras) // 10 and 1 <= casilla_y < len(self.cuadras) // 10:
                        if x == 0 and y == 0:
                            continue
                       
                        self.casillas_movimiento.append((casilla_x, casilla_y))


                        movimiento_surface = pygame.Surface((TAMANIO_CUADRILLA, TAMANIO_CUADRILLA))
                        movimiento_surface.set_alpha(100)  # 0 es completamente transparente, 255 es opaco
                        movimiento_surface.fill((0, 0, 255))  # Color azul


                        casilla_x_pos = self.offset_x + casilla_x * TAMANIO_CUADRILLA
                        casilla_y_pos = self.offset_y + casilla_y * TAMANIO_CUADRILLA
                        self.screen.blit(movimiento_surface, (casilla_x_pos, casilla_y_pos))


    def mover_orco(self, x, y):
        distancia = abs(x - self.orco_pos[0]) + abs(y - self.orco_pos[1])


        if distancia <= self.radio_movimiento:
            self.orco_pos = (x, y)


            self.radio_movimiento -= distancia


            if self.radio_movimiento <= 0:
                self.movimiento_activo = False 
                print(f"Rango de movimiento agotado. Movimientos restantes: {self.radio_movimiento}")


    def terminar_turno(self):
        """Restablecer el rango de movimiento al final del turno."""
        self.radio_movimiento = rangomover
        self.movimiento_activo = False
        print("Turno terminado, rango de movimiento restaurado.")


    def iniciar_turno(self):
        """Inicia el turno del jugador o enemigo."""
        self.turno_jugador = True
        self.turno_enemigo = False
        self.movimiento_activo = False 
       
    def activar_submenu(self, tipo):
       if self.submenu_tipo == tipo:
            self.submenu_opciones = self.acciones[tipo]
            self.mostrar_submenu = True
       else:
            self.mostrar_submenu = True
            self.submenu_tipo = tipo
            self.submenu_opciones = self.acciones.get(tipo, [])
       
   
       




    def seleccionar_accion(self, opcion):
        print(f"Acción seleccionada: {opcion}")
        self.mostrar_submenu = False                            
                           


    def dibujar_submenu(self):
        submenu_width = 200
        submenu_height = 100 + len(self.submenu_opciones) * 40
        submenu_rect = pygame.Rect((ANCHO - submenu_width) // 2, (ALTO - submenu_height) // 2, submenu_width, submenu_height)
        pygame.draw.rect(self.screen, COLOR_FONDO_SUBMENU, submenu_rect)



        for i, opcion in enumerate(self.submenu_opciones):
            y_offset = (i + 1) * 40
            opcion_rect = pygame.Rect(submenu_rect.x + 10, submenu_rect.y + y_offset, submenu_width - 20, 30)
            pygame.draw.rect(self.screen, COLOR_BTN, opcion_rect)
            pygame.draw.rect(self.screen, (0, 0, 0), opcion_rect, 2)
            self.dibujar_texto(opcion, opcion_rect)
       
       


    def manejar_eventos(self):
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                exit()
            if evento.type == MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()


                # Verificar si se hizo clic en algún botón principal
                if self.botones[0].collidepoint(pos):  # Acción
                    if not self.accion_utilizada:  # Si no se ha utilizado la acción principal
                        self.activar_submenu('accion')
                        self.accion_utilizada = True  # Marcar como utilizada
                    else:
                        print("Ya has utilizado tu acción principal este turno.")
                elif self.botones[1].collidepoint(pos):  # Acción Adicional
                    if not self.accion_adicional_utilizada:  # Si no se ha utilizado la acción adicional
                        if self.mostrar_submenu and self.submenu_tipo == 'accion_adicional':
                            self.mostrar_submenu = False
                        else:
                            self.activar_submenu('accion_adicional')
                        self.accion_adicional_utilizada = True  # Marcar como utilizada
                    else:
                        print("Ya has utilizado tu acción adicional este turno.")
                elif self.botones[2].collidepoint(pos):  # Mover
                    self.movimiento_activo = True  # Activar el modo de movimiento
                elif self.botones[3].collidepoint(pos):  # Terminar Turno
                    self.terminar_turno()
                    print("Turno terminado.")
                    # Reiniciar las acciones al final del turno
                    self.accion_utilizada = False
                    self.accion_adicional_utilizada = False


                # Verificar si se hizo clic en una casilla de movimiento
                if self.movimiento_activo:
                    for casilla in self.casillas_movimiento:
                        casilla_x, casilla_y = casilla
                        casilla_rect = pygame.Rect(self.offset_x + casilla_x * TAMANIO_CUADRILLA,
                                                   self.offset_y + casilla_y * TAMANIO_CUADRILLA,
                                                   TAMANIO_CUADRILLA, TAMANIO_CUADRILLA)
                        if casilla_rect.collidepoint(pos):
                            self.mover_orco(casilla_x, casilla_y)
                            break

                if self.mostrar_submenu:
                    submenu_rect = pygame.Rect((ANCHO - 200) // 2, (ALTO - 100 - len(self.submenu_opciones) * 40) // 2, 200, 100 + len(self.submenu_opciones) * 40)
                    for i, opcion in enumerate(self.submenu_opciones):
                        y_offset = (i + 1) * 40
                        opcion_rect = pygame.Rect(submenu_rect.x + 10, submenu_rect.y + y_offset, submenu_rect.width - 20, 30)
                        if opcion_rect.collidepoint(pos):
                            self.seleccionar_accion(opcion)
                            break
                   


                if self.movimiento_activo:
                    for casilla in self.casillas_movimiento:
                        casilla_x, casilla_y = casilla
                        casilla_rect = pygame.Rect(self.offset_x + casilla_x * TAMANIO_CUADRILLA,
                                                self.offset_y + casilla_y * TAMANIO_CUADRILLA,
                                                TAMANIO_CUADRILLA, TAMANIO_CUADRILLA)
                        if casilla_rect.collidepoint(pos):
                            self.mover_orco(casilla_x, casilla_y)
                            break


                if self.mostrar_submenu:
                    submenu_rect = pygame.Rect((ANCHO - 200) // 2, (ALTO - 100 - len(self.submenu_opciones) * 40) // 2, 200, 100 + len(self.submenu_opciones) * 40)
                    for i, opcion in enumerate(self.submenu_opciones):
                        y_offset = (i + 1) * 40
                        opcion_rect = pygame.Rect(submenu_rect.x + 10, submenu_rect.y + y_offset, submenu_rect.width - 20, 30)
                        if opcion_rect.collidepoint(pos):
                            self.seleccionar_accion(opcion)
                            break

    def main(self):
        self.crear_cuadrillas()
        self.crear_botones()
        while True:
            self.manejar_eventos()
            self.dibujar_escenario()
            pygame.display.update()