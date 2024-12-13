import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Juego")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
DARK_GRAY = (150, 150, 150)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

font = pygame.font.Font(None, 24) 

bosque_img = pygame.image.load("assets/bosque.png")
papiro_img = pygame.image.load("assets/papiro.png")
orco_img = pygame.image.load("assets/Orco-Splashart.png")

historia = [
    "Te encuentras volviendo a la ciudad con tus 2 amigos, luego de una larga noche de aventura,",
    "Cuando de repente ven una gran cantidad de humo saliendo de las profundidades del bosque.",
    "Cada uno de ellos opinan algo distinto, por lo que la responsabilidad de elegir qué hacer recae en ti."
]


opciones = [
    ("Ir a la ciudad", 'ir_a_ciudad'),
    ("Explorar el bosque", 'explorar_bosque')
]

decision_idx = 0
vida_pj = 100  
def boton(x, y, ancho, alto, texto, accion=None):
    """Dibuja un botón y detecta si es clickeado."""
    mouse = pygame.mouse.get_pos()
    rect_color = GRAY if (x < mouse[0] < x + ancho and y < mouse[1] < y + alto) else DARK_GRAY

    pygame.draw.rect(screen, rect_color, (x, y, ancho, alto))
    text = font.render(texto, True, BLACK)
    screen.blit(text, (x + (ancho - text.get_width()) // 2, y + (alto - text.get_height()) // 2))

    if pygame.mouse.get_pressed()[0]:
        if x < mouse[0] < x + ancho and y < mouse[1] < y + alto:
            if accion:
                accion()

def mostrar_menu():
    """Muestra el menú con la opción de salir en la esquina superior izquierda."""
    boton(10, 10, 150, 40, "Salir", salir)

def dibujar_estado_personaje():
    """Dibuja la imagen del personaje y la barra de vida."""
    orco_resized = pygame.transform.scale(orco_img, (100, 100))
    screen.blit(orco_resized, (WIDTH - 120, 20))

    barra_x = WIDTH - 140
    barra_y = 130
    barra_ancho = 100
    barra_alto = 20

    pygame.draw.rect(screen, DARK_GRAY, (barra_x, barra_y, barra_ancho, barra_alto))
    vida_ancho = int((vida_pj / 100) * barra_ancho)
    pygame.draw.rect(screen, GREEN if vida_pj > 30 else RED, (barra_x, barra_y, vida_ancho, barra_alto))

def jugar():
    global decision_idx

    running = True
    while running:
        screen.fill(WHITE)

        bosque_resized = pygame.transform.scale(bosque_img, (WIDTH, HEIGHT // 2))
        screen.blit(bosque_resized, (0, 0))


        papiro_resized = pygame.transform.scale(papiro_img, (WIDTH - 10, HEIGHT // 2 + 50))
        papiro_x = (WIDTH - papiro_resized.get_width()) // 2
        papiro_y = HEIGHT // 2 - 20
        screen.blit(papiro_resized, (papiro_x, papiro_y))

        
        y_offset = papiro_y + 50 
        for i, line in enumerate(historia[:decision_idx + 1]):
            historia_text = font.render(line, True, BLACK)
            screen.blit(historia_text, (papiro_x, y_offset + i * 30))  
        if decision_idx == len(historia) - 1:
            for i, (texto, accion) in enumerate(opciones):
                boton(papiro_x + 50, papiro_y + 200 + i * 60, papiro_resized.get_width() - 100, 50, texto, globals()[accion])

        dibujar_estado_personaje()

        mostrar_menu()
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if decision_idx < len(historia) - 1:
            decision_idx += 1

    pygame.quit()
    sys.exit()

def ir_a_ciudad():
    global decision_idx
    print("El jugador decide ir a la ciudad.")
    decision_idx = 0

def explorar_bosque():
    global decision_idx
    print("El jugador decide explorar el bosque.")
    decision_idx = 0

def salir():
    """Función para salir del juego."""
    pygame.quit()
    sys.exit()

def seleccionar_personaje():
    jugar()

if __name__ == "__main__":
    seleccionar_personaje()
