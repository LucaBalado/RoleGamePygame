import pygame
from razas import Humano, Elfo, Orco  # Las clases de las razas
from clases import Guerrero, Hechicero  # Las clases del personaje
import sys

# Inicialización de Pygame
pygame.init()

# Configuración de la pantalla
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Juego")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
DARK_GRAY = (150, 150, 150)

# Fuentes
font = pygame.font.Font(None, 36)

# Cargar imágenes de splashart
assets = {
    "Humano": pygame.image.load("assets/Orco-Splashart.png"),
    "Elfo": pygame.image.load("assets/Orco-Splashart.png"),
    "Orco": pygame.image.load("assets/Orco-Splashart.png")
}

def mostrar_estado(raza, vida, xp):
    vida_text = font.render(f"Vida: {vida}", True, BLACK)
    screen.blit(vida_text, (20, HEIGHT - 120))

    xp_text = font.render(f"XP: {xp}", True, BLACK)
    screen.blit(xp_text, (20, HEIGHT - 80))

    splashart = assets.get(raza.__class__.__name__, None)
    if splashart:
        splashart = pygame.transform.scale(splashart, (100, 100))  
        screen.blit(splashart, (WIDTH - 120, 20))

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

def jugar(raza, clase):
    personaje = clase
    personaje.vida = 10 
    personaje.xp = 0

    # Variables de la narrativa
    historia = [
        "Te encuentras en una taberna, charlando y bebiendo con tus tres amigos, cuando de repente",
        "Un grupo de guardias reales irrumpen en el lugar exigiendo un grupo de aventureros temerarios",
        "Ëllos, al ver que ustedes son los unicos que puden mantenerse en pie, se acercan hacia ustedes..."
    ]
    opciones = [
        ("Ir a la ciudad", ir_a_ciudad),
        ("Explorar el bosque", explorar_bosque)
    ]
    
    decision_idx = 0  # Comienza con la primera parte de la historia

    # Bucle principal del juego
    running = True
    while running:
        screen.fill(WHITE)  # Limpiar pantalla

        # Mostrar estado del personaje
        mostrar_estado(raza, personaje.vida, personaje.xp)

        # Mostrar el texto de la historia
        historia_text = font.render(historia[decision_idx], True, BLACK)
        screen.blit(historia_text, (WIDTH // 2 - historia_text.get_width() // 2, HEIGHT // 4))

        # Dibujar los botones de decisiones
        for i, (texto, accion) in enumerate(opciones):
            boton(WIDTH // 2 - 150, HEIGHT // 2 + i * 60, 300, 50, texto, accion)

        pygame.display.flip()  # Actualizar la pantalla

        # Manejo de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()
    sys.exit()

# Funciones para las decisiones
def ir_a_ciudad():
    print("El jugador decide ir a la ciudad.")
    # Aquí agregas la lógica de lo que pasa cuando el jugador decide ir a la ciudad.
    # Puedes cambiar la historia, la ubicación, o lo que desees.

def explorar_bosque():
    print("El jugador decide explorar el bosque.")
    # Aquí agregas la lógica de lo que pasa cuando el jugador decide explorar el bosque.
    # Puedes cambiar la historia, agregar combate o eventos.

# Función para seleccionar la raza y clase
def seleccionar_personaje():

    raza = Humano()  
    clase = Guerrero()  

    jugar(raza, clase)

if __name__ == "__main__":
    seleccionar_personaje()
