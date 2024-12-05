import pygame
from razas import Humano, Elfo, Orco
from clases import Guerrero, Hechicero

# Inicializar Pygame
pygame.init()

# Dimensiones de la pantalla
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Creador de Personaje")

# Colores y fuentes
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
DARK_GRAY = (150, 150, 150)
font = pygame.font.Font(None, 36)

# Cargar imágenes
splashart_humano = pygame.image.load("assets/splashart_humano.png")
splashart_elfo = pygame.image.load("assets/splashart_elfo.png")
splashart_orco = pygame.image.load("assets/splashart_orco.png")
splashart_humano = pygame.transform.scale(splashart_humano, (100, 100))  # Escalar imagen
splashart_elfo = pygame.transform.scale(splashart_elfo, (100, 100))  # Escalar imagen
splashart_orco = pygame.transform.scale(splashart_orco, (100, 100))  # Escalar imagen

# Datos del personaje
razas = [Humano(), Elfo(), Orco()]
clases = [Guerrero(), Hechicero()]
raza_idx, clase_idx = 0, 0
vida = 100
xp = 0

# Función para dibujar un botón
def boton(x, y, ancho, alto, texto, accion=None, evento=None):
    """Dibuja un botón y detecta si es clickeado."""
    mouse = pygame.mouse.get_pos()
    rect_color = GRAY if (x < mouse[0] < x + ancho and y < mouse[1] < y + alto) else DARK_GRAY

    pygame.draw.rect(screen, rect_color, (x, y, ancho, alto))
    text = font.render(texto, True, BLACK)
    screen.blit(text, (x + (ancho - text.get_width()) // 2, y + (alto - text.get_height()) // 2))

    if evento and evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
        if x < evento.pos[0] < x + ancho and y < evento.pos[1] < y + alto:
            if accion:
                accion()

# Función para cambiar de raza
def cambiar_raza(accion):
    global raza_idx
    raza_idx = (raza_idx + accion) % len(razas)

# Función para cambiar de clase
def cambiar_clase(accion):
    global clase_idx
    clase_idx = (clase_idx + accion) % len(clases)

# Función para mostrar la información del personaje (splashart, vida, xp)
def mostrar_info_personaje():
    # Mostrar el splashart de la raza seleccionada
    if razas[raza_idx].__class__.__name__ == "Humano":
        screen.blit(splashart_humano, (20, 20))
    elif razas[raza_idx].__class__.__name__ == "Elfo":
        screen.blit(splashart_elfo, (20, 20))
    elif razas[raza_idx].__class__.__name__ == "Orco":
        screen.blit(splashart_orco, (20, 20))

    # Mostrar vida y XP debajo del splashart
    vida_texto = font.render(f"Vida: {vida}", True, BLACK)
    screen.blit(vida_texto, (20, 130))

    xp_texto = font.render(f"XP: {xp}", True, BLACK)
    screen.blit(xp_texto, (20, 170))

# Función para la creación del personaje
def creacion_personaje():
    global raza_idx, clase_idx, vida, xp
    running = True
    while running:
        screen.fill(WHITE)

        # Mostrar raza y clase seleccionadas
        raza_text = font.render(f"Raza: {razas[raza_idx].__class__.__name__}", True, BLACK)
        clase_text = font.render(f"Clase: {clases[clase_idx].__class__.__name__}", True, BLACK)

        # Mostrar la información del personaje (splashart, vida, XP)
        mostrar_info_personaje()

        # Botones para cambiar raza y clase
        boton(150, 50, 50, 30, "<--", lambda: cambiar_raza(-1))
        boton(WIDTH - 200, 50, 50, 30, "-->", lambda: cambiar_raza(1))
        screen.blit(raza_text, (WIDTH // 2 - raza_text.get_width() // 2, 50))

        boton(150, HEIGHT - 100, 50, 30, "<--", lambda: cambiar_clase(-1))
        boton(WIDTH - 200, HEIGHT - 100, 50, 30, "-->", lambda: cambiar_clase(1))
        screen.blit(clase_text, (WIDTH // 2 - clase_text.get_width() // 2, HEIGHT - 100))

        # Botones de navegación
        boton(WIDTH // 4 - 100, HEIGHT - 50, 150, 40, "Volver", menu_inicial)
        boton(3 * WIDTH // 4 - 100, HEIGHT - 50, 150, 40, "Jugar", iniciar_juego)

        # Manejo de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()

# Función para volver al menú principal
def menu_inicial():
    global running
    running = True
    while running:
        screen.fill(WHITE)

        # Mostrar botones
        boton(WIDTH // 2 - 100, HEIGHT // 2 - 50, 200, 50, "Jugar", iniciar_creacion)
        boton(WIDTH // 2 - 100, HEIGHT // 2 + 50, 200, 50, "Salir", salir_juego)

        # Título
        title_text = font.render("Menú Principal", True, BLACK)
        screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, HEIGHT // 4))

        # Manejo de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()

# Función para iniciar la creación de personaje
def iniciar_creacion():
    creacion_personaje()

# Función para salir del juego
def salir_juego():
    global running
    running = False

# Función para iniciar el juego
def iniciar_juego():
    import juego

menu_inicial()

pygame.quit()
