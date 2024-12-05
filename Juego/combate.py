import pygame
from personaje import Guerrero, Hechicero

pygame.init()

# Definimos los parámetros de la pantalla
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Combate Turno por Turno")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARK_GRAY = (150, 150, 150)
font = pygame.font.Font(None, 36)

# Crear las instancias de los personajes
guerrero = Guerrero()
hechicero = Hechicero()

# Selección de personaje, supongamos que el jugador elige Guerrero o Hechicero
personaje_seleccionado = guerrero  # Puede ser guerrero o hechicero

# Función para dibujar botones
def boton(x, y, ancho, alto, texto, accion=None):
    mouse = pygame.mouse.get_pos()
    rect_color = DARK_GRAY if (x < mouse[0] < x + ancho and y < mouse[1] < y + alto) else WHITE

    pygame.draw.rect(screen, rect_color, (x, y, ancho, alto))
    text = font.render(texto, True, BLACK)
    screen.blit(text, (x + (ancho - text.get_width()) // 2, y + (alto - text.get_height()) // 2))

    if pygame.mouse.get_pressed()[0] and (x < mouse[0] < x + ancho and y < mouse[1] < y + alto):
        if accion:
            accion()

# Funciones de acción
def seleccionar_accion():
    print(personaje_seleccionado.realizar_accion(0))  # 0: Primer acción (o Ataque Doble o Curación)

def seleccionar_accion_bonus():
    print(personaje_seleccionado.realizar_accion_bonus(0))  # 0: Primer acción bonus (Aumentar Defensa)

def iniciar_combate():
    global personaje_seleccionado
    # Mostrar la interfaz de combate
    while True:
        screen.fill(WHITE)

        # Dibujar splashart y vida
        splashart = pygame.image.load("assets/splashart_guerrero.png")  # Imagen de ejemplo
        splashart = pygame.transform.scale(splashart, (100, 100))
        screen.blit(splashart, (10, 10))

        # Mostrar texto de vida y experiencia
        vida_text = font.render("Vida: 100", True, BLACK)
        xp_text = font.render("XP: 0", True, BLACK)
        screen.blit(vida_text, (120, 10))
        screen.blit(xp_text, (120, 50))

        # Botones para seleccionar acción y bonus
        boton(100, HEIGHT - 100, 150, 50, "Acción", seleccionar_accion)
        boton(300, HEIGHT - 100, 150, 50, "Acción Bonus", seleccionar_accion_bonus)

        # Mostrar las opciones disponibles basadas en el personaje seleccionado
        if isinstance(personaje_seleccionado, Guerrero):
            print("Acción seleccionada: Ataque Doble")
            print("Acción bonus: Aumentar Defensa")
        elif isinstance(personaje_seleccionado, Hechicero):
            print("Acción seleccionada: Curación o Ataque")
            print("Acción bonus: Aumentar Defensa o Buffea Equipo")

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

iniciar_combate()
