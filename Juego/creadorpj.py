import pygame
from pjbase import PersonajeBase
from razas import Humano, Elfo, Orco
from clases import Guerrero, Hechicero
from historia import jugar
import os

pygame.init()

WIDTH, HEIGHT = 800, 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Creador de Personaje")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
DARK_GRAY = (150, 150, 150)

font = pygame.font.Font(None, 36)
description_font = pygame.font.Font(None, 24)  # Fuente más pequeña para las descripciones

assets = {
    ("Humano", "Guerrero"): pygame.image.load("assets/Hechicero-Humano.png"),
    ("Humano", "Hechicero"): pygame.image.load("assets/Hechicero-Humano.png"),
    ("Elfo", "Guerrero"): pygame.image.load("assets/Hechicero-Elfo.png"),
    ("Elfo", "Hechicero"): pygame.image.load("assets/Hechicero-Elfo.png"),
    ("Orco", "Guerrero"): pygame.image.load("assets/Hechicero-Orco.png"),
    ("Orco", "Hechicero"): pygame.image.load("assets/Hechicero-Orco.png"),
}

razas = [Humano(), Elfo(), Orco()]
clases = [Guerrero(), Hechicero()]

raza_idx, clase_idx = 0, 0
running = True

descripciones = {
    "Humano": "Los Humanos son versátiles, con un gran balance entre fuerza y agilidad.",
    "Elfo": "Los Elfos son ágiles y sabios, expertos en el uso de magia y arcos.",
    "Orco": "Los Orcos son fuertes y resistentes, excelentes guerreros en combate cuerpo a cuerpo.",
    "Guerrero": "El Guerrero es un experto en combate físico, con alta resistencia y daño.",
    "Hechicero": "El Hechicero es un maestro de la magia, capaz de lanzar poderosos conjuros a distancia."
}

def boton(x, y, ancho, alto, texto, accion=None, evento=None):
    """Dibuja un botón y detecta si es clickeado."""
    mouse = pygame.mouse.get_pos()
    rect_color = GRAY if (x < mouse[0] < x + ancho and y < mouse[1] < y + alto) else DARK_GRAY
    # Dibujar el botón
    pygame.draw.rect(screen, rect_color, (x, y, ancho, alto))
    text = font.render(texto, True, BLACK)
    screen.blit(text, (x + (ancho - text.get_width()) // 2, y + (alto - text.get_height()) // 2))

    # Procesar clic si el evento es MOUSEBUTTONDOWN y está dentro del área del botón
    if evento and evento.type == pygame.MOUSEBUTTONDOWN:
        if x < evento.pos[0] < x + ancho and y < evento.pos[1] < y + alto:
            if accion:
                accion()

def cambiar_raza(accion):
    global raza_idx
    raza_idx = (raza_idx + accion) % len(razas)

def cambiar_clase(accion):
    global clase_idx
    clase_idx = (clase_idx + accion) % len(clases)

def menu_inicial():
    global running
    while running:
        screen.fill(WHITE)
        # Mostrar título del menú
        title_text = font.render("Menú Principal", True, BLACK)
        screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, HEIGHT // 4))

        # Manejo de eventos
        evento_actual = None
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                evento_actual = event

        # Botones principales
        boton(WIDTH // 2 - 100, HEIGHT // 2 - 50, 200, 50, "Iniciar", iniciar_creacion, evento_actual)
        boton(WIDTH // 2 - 100, HEIGHT // 2 + 50, 200, 50, "Salir", salir_juego, evento_actual)

        pygame.display.flip()

def iniciar_creacion():
    creacion_personaje()

def salir_juego():
    global running
    running = False

def creacion_personaje():
    global running
    while running:
        screen.fill(WHITE)
        raza_text = font.render(f"{razas[raza_idx].__class__.__name__}", True, BLACK)
        clase_text = font.render(f"{clases[clase_idx].__class__.__name__}", True, BLACK)
        key = (razas[raza_idx].__class__.__name__, clases[clase_idx].__class__.__name__)
        if key in assets:
            image = assets[key]
            # Escala la imagen a un tamaño mayor, por ejemplo, 1.5x su tamaño original
            scaled_width = int(image.get_width() * 2)
            scaled_height = int(image.get_height() * 2)
            scaled_image = pygame.transform.scale(image, (scaled_width, scaled_height))
            # Dibuja la imagen escalada en el centro
            screen.blit(scaled_image, (WIDTH // 2 - scaled_width // 2, HEIGHT // 2 - scaled_height // 2))  
        # Verificar si el mouse está sobre el texto de la raza o la clase
        mouse_x, mouse_y = pygame.mouse.get_pos()
        raza_rect = raza_text.get_rect(center=(WIDTH // 2, 50))
        clase_rect = clase_text.get_rect(center=(WIDTH // 2, HEIGHT - 100))
        
        if raza_rect.collidepoint(mouse_x, mouse_y):
            descripcion_text = description_font.render(descripciones[razas[raza_idx].__class__.__name__], True, BLACK)
            screen.blit(descripcion_text, (WIDTH // 2 - descripcion_text.get_width() // 2, 100))

        if clase_rect.collidepoint(mouse_x, mouse_y):
            descripcion_text = description_font.render(descripciones[clases[clase_idx].__class__.__name__], True, BLACK)
            screen.blit(descripcion_text, (WIDTH // 2 - descripcion_text.get_width() // 2, HEIGHT - 150))

        evento_actual = None
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                evento_actual = event
        
        # Botones de cambio de raza
        boton(150, 50, 50, 30, "<--", lambda: cambiar_raza(-1), evento_actual)
        boton(WIDTH - 200, 50, 50, 30, "-->", lambda: cambiar_raza(1), evento_actual)
        screen.blit(raza_text, (WIDTH // 2 - raza_text.get_width() // 2, 50))

        # Botones de cambio de clase
        boton(150, HEIGHT - 100, 50, 30, "<--", lambda: cambiar_clase(-1), evento_actual)
        boton(WIDTH - 200, HEIGHT - 100, 50, 30, "-->", lambda: cambiar_clase(1), evento_actual)
        screen.blit(clase_text, (WIDTH // 2 - clase_text.get_width() // 2, HEIGHT - 100))

        # Botones de navegación
        boton(WIDTH // 4 - 100, HEIGHT - 50, 150, 40, "Volver", menu_inicial, evento_actual)
        boton(3 * WIDTH // 4 - 100, HEIGHT - 50, 150, 40, "Jugar", iniciar_juego, evento_actual)

        pygame.display.flip()

def iniciar_juego():
    global running
    while running:
        jugar()


menu_inicial()
pygame.quit()
