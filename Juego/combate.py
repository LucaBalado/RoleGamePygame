import pygame
from pygame.locals import *
import pathlib as pl
import random
import sys

ANCHO, ALTO = 800,600
TAMANIO_CUADRILLA = 32
COLOR_CUADRILLA = (200, 200, 200)
COLOR_BTN = (100, 100, 255)
COLOR_BTN_PRESIONADO = (255, 100, 100)
PORCENTAJE_OCUPACION = 0.7
TAMANO_BOTON = (150, 50)
COLOR_FONDO_SUBMENU = (255, 255, 255)
rangomover = 3

# Clase para el enemigo
class Enemigo:
    def __init__(self, pos=(10, 4)):
        self.pos = pos
        enemy_path = "assets/sprites/Enemigo.png"
        try:
            self.sprite = pygame.image.load(enemy_path)
            self.sprite = pygame.transform.scale(self.sprite, (TAMANIO_CUADRILLA, TAMANIO_CUADRILLA))
        except pygame.error as e:
            print(f"Error cargando la imagen del enemigo: {e}")
            sys.exit()

class Pelea:
    def __init__(self, juego, fondo_path, sprite_path):
        pygame.init()
        self.juego = juego
        self.screen = pygame.display.set_mode((ANCHO, ALTO))
        pygame.display.set_caption("Campo de Batalla")
        
        # Cargar el fondo
        fondo = pl.Path(fondo_path)
        fondo.resolve()
        sprite = pl.Path(sprite_path)
        sprite.resolve()
        try:
            self.fondo = pygame.image.load(str(fondo))
            self.fondo = pygame.transform.scale(self.fondo, (ANCHO, ALTO))
        except pygame.error as e:
            print(f"Error cargando la imagen de fondo: {e}")
            sys.exit()
        try:
            self.sprite_orco = pygame.image.load(str(sprite))
            self.sprite_orco = pygame.transform.scale(self.sprite_orco, (TAMANIO_CUADRILLA, TAMANIO_CUADRILLA))
        except pygame.error as e:
            print(f"Error cargando la imagen del sprite: {e}")
            sys.exit()
        
        self.cuadras = []
        self.offset_x = 0
        self.offset_y = 0
        self.botones = []
        self.radio_movimiento = rangomover
        self.movimiento_activo = False
        self.casillas_movimiento = []
        self.orco_pos = (4, 4)
        # Instanciar el enemigo en la posición deseada (por ejemplo, (10, 4))
        self.enemigo = Enemigo((10, 4))
        self.movimientos_realizados = 0
        self.turno_jugador = True
        self.turno_enemigo_flag = False
        self.mostrar_submenu = False
        self.submenu_tipo = None
        # Definir acciones según la clase del personaje
        if self.juego.clase == "Hechicero":
            self.acciones = {
                'accion': ["Tiro Con Arco", "Bola de Fuego"],
                'accion_adicional': ["Aumentar Armadura", "Curación"]
            }
        else:
            self.acciones = {
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
    
    def dibujar_botones(self):
        etiquetas = ["Acción", "Acción Adicional", "Mover", "Terminar Turno"]
        font_btn = pygame.font.Font(None, 28)
        for boton, texto in zip(self.botones, etiquetas):
            pygame.draw.rect(self.screen, COLOR_BTN, boton)
            pygame.draw.rect(self.screen, (0, 0, 0), boton, 2)
            text_surface = font_btn.render(texto, True, (0, 0, 0))
            text_rect = text_surface.get_rect(center=boton.center)
            self.screen.blit(text_surface, text_rect)
    
    def dibujar_escenario(self):
        self.screen.blit(self.fondo, (0, 0))
        for cuad in self.cuadras:
            pygame.draw.rect(self.screen, COLOR_CUADRILLA, (*cuad, TAMANIO_CUADRILLA, TAMANIO_CUADRILLA), 1)
        # Dibujar el sprite del personaje (orco)
        orco_pos_x = self.offset_x + self.orco_pos[0] * TAMANIO_CUADRILLA
        orco_pos_y = self.offset_y + self.orco_pos[1] * TAMANIO_CUADRILLA
        self.screen.blit(self.sprite_orco, (orco_pos_x, orco_pos_y))
        # Dibujar el enemigo
        enemy_x = self.offset_x + self.enemigo.pos[0] * TAMANIO_CUADRILLA
        enemy_y = self.offset_y + self.enemigo.pos[1] * TAMANIO_CUADRILLA
        self.screen.blit(self.enemigo.sprite, (enemy_x, enemy_y))
        self.dibujar_botones()
        if self.movimiento_activo:
            self.dibujar_movimiento()
        if self.mostrar_submenu:
            self.dibujar_submenu()
    
    def dibujar_texto(self, texto, rect):
        font_text = pygame.font.Font(None, 30)
        text_surface = font_text.render(texto, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=rect.center)
        self.screen.blit(text_surface, text_rect)
    
    def dibujar_movimiento(self):
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
                        movimiento_surface.set_alpha(100)
                        movimiento_surface.fill((0, 0, 255))
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
        """Restablece el rango de movimiento y activa el turno del enemigo."""
        self.radio_movimiento = rangomover
        self.movimiento_activo = False
        print("Turno del jugador terminado, rango de movimiento restaurado.")
        self.accion_utilizada = False
        self.accion_adicional_utilizada = False
        self.turno_enemigo()
    
    def turno_enemigo(self):
        """Simula el turno del enemigo: se mueve y ejecuta una acción."""
        self.turno_enemigo_flag = True
        print("Turno del enemigo:")
        # Movimiento aleatorio: elige desplazamientos en x e y (-1, 0 o 1)
        dx = random.choice([-1, 0, 1])
        dy = random.choice([-1, 0, 1])
        new_x = self.enemigo.pos[0] + dx
        new_y = self.enemigo.pos[1] + dy
        self.enemigo.pos = (new_x, new_y)
        print("El enemigo se movió a:", self.enemigo.pos)
        # Simular acción aleatoria (por ejemplo, "Atacar" o "Defender")
        enemy_action = random.choice(["Atacar", "Defender"])
        print("El enemigo realiza la acción:", enemy_action)
        pygame.time.delay(1000)  # Pausa 1 segundo para visualizar la acción
        self.turno_enemigo_flag = False
        self.turno_jugador = True
        print("Fin del turno del enemigo. Vuelve el turno del jugador.")
    
    def activar_submenu(self, tipo):
        self.mostrar_submenu = True
        self.submenu_tipo = tipo
        self.submenu_opciones = self.acciones.get(tipo, [])
    
    def seleccionar_accion(self, opcion):
        print(f"Acción seleccionada: {opcion}")
        self.mostrar_submenu = False
    
    def dibujar_submenu(self):
        submenu_width = 200
        submenu_height = 100 + len(self.submenu_opciones) * 40
        submenu_rect = pygame.Rect((ANCHO - submenu_width) // 2,
                                   (ALTO - submenu_height) // 2,
                                   submenu_width, submenu_height)
        pygame.draw.rect(self.screen, COLOR_FONDO_SUBMENU, submenu_rect)
        for i, opcion in enumerate(self.submenu_opciones):
            y_offset = (i + 1) * 40
            opcion_rect = pygame.Rect(submenu_rect.x + 10,
                                      submenu_rect.y + y_offset,
                                      submenu_width - 20, 30)
            pygame.draw.rect(self.screen, COLOR_BTN, opcion_rect)
            pygame.draw.rect(self.screen, (0, 0, 0), opcion_rect, 2)
            self.dibujar_texto(opcion, opcion_rect)
    
    def manejar_eventos(self):
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                # Botón Acción
                if self.botones[0].collidepoint(pos):
                    if not self.accion_utilizada:
                        self.activar_submenu('accion')
                        self.accion_utilizada = True
                    else:
                        print("Ya has utilizado tu acción principal este turno.")
                # Botón Acción Adicional
                elif self.botones[1].collidepoint(pos):
                    if not self.accion_adicional_utilizada:
                        if self.mostrar_submenu and self.submenu_tipo == 'accion_adicional':
                            self.mostrar_submenu = False
                        else:
                            self.activar_submenu('accion_adicional')
                        self.accion_adicional_utilizada = True
                    else:
                        print("Ya has utilizado tu acción adicional este turno.")
                # Botón Mover
                elif self.botones[2].collidepoint(pos):
                    self.movimiento_activo = True
                # Botón Terminar Turno
                elif self.botones[3].collidepoint(pos):
                    self.terminar_turno()
                    print("Turno terminado.")
                # Verificar clic en casillas de movimiento
                if self.movimiento_activo:
                    for casilla in self.casillas_movimiento:
                        casilla_x, casilla_y = casilla
                        casilla_rect = pygame.Rect(self.offset_x + casilla_x * TAMANIO_CUADRILLA,
                                                   self.offset_y + casilla_y * TAMANIO_CUADRILLA,
                                                   TAMANIO_CUADRILLA, TAMANIO_CUADRILLA)
                        if casilla_rect.collidepoint(pos):
                            self.mover_orco(casilla_x, casilla_y)
                            break
                # Verificar clic en opciones del submenú
                if self.mostrar_submenu:
                    submenu_rect = pygame.Rect((ANCHO - 200) // 2,
                                               (ALTO - 100 - len(self.submenu_opciones) * 40) // 2,
                                               200, 100 + len(self.submenu_opciones) * 40)
                    for i, opcion in enumerate(self.submenu_opciones):
                        y_offset = (i + 1) * 40
                        opcion_rect = pygame.Rect(submenu_rect.x + 10,
                                                  submenu_rect.y + y_offset,
                                                  submenu_rect.width - 20, 30)
                        if opcion_rect.collidepoint(pos):
                            self.seleccionar_accion(opcion)
                            break
                # Otra verificación de casillas de movimiento (si es necesaria)
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
                    submenu_rect = pygame.Rect((ANCHO - 200) // 2,
                                               (ALTO - 100 - len(self.submenu_opciones) * 40) // 2,
                                               200, 100 + len(self.submenu_opciones) * 40)
                    for i, opcion in enumerate(self.submenu_opciones):
                        y_offset = (i + 1) * 40
                        opcion_rect = pygame.Rect(submenu_rect.x + 10,
                                                  submenu_rect.y + y_offset,
                                                  submenu_rect.width - 20, 30)
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
