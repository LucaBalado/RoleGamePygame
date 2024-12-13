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

font = pygame.font.Font(None, 24) 

# Cargar imágenes
bosque_img = pygame.image.load("assets/bosque.png")
papiro_img = pygame.image.load("assets/papiro.png")

# Historia
historia = [
    "Te encuentras volviendo a la ciudad con tus 2 amigos, luego de una larga noche de aventura,",
    "Cuando de repente ven una gran cantidad de humo saliendo de las profundidades del bosque.",
    "Cada uno de ellos opinan algo distinto, por lo que la responsabilidad de elegir que hacer recae en ti."
]

# Opciones de botones
opciones = [
    ("Ir a la ciudad", 'ir_a_ciudad'),
    ("Explorar el bosque", 'explorar_bosque')
]

# Variable global para seguir el índice de la historia
decision_idx = 0  

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

def jugar():
    global decision_idx

    running = True
    while running:
        screen.fill(WHITE)  # Rellenar con el color blanco para la parte de fondo

        # Mostrar el menú de la esquina superior izquierda
        

        # Mostrar la imagen del bosque en la mitad superior
        bosque_resized = pygame.transform.scale(bosque_img, (WIDTH, HEIGHT // 2))  # Redimensiona la imagen para que ocupe la mitad superior
        screen.blit(bosque_resized, (0, 0))

        # Mostrar la imagen del papiro en la mitad inferior
        papiro_resized = pygame.transform.scale(papiro_img, (WIDTH, HEIGHT // 2))  # Redimensiona la imagen para que ocupe la mitad inferior
        screen.blit(papiro_resized, (0, HEIGHT // 2))

        # Mostrar el texto de la historia línea por línea
        y_offset = HEIGHT // 8  # Ajuste la posición vertical del texto
        for i, line in enumerate(historia[:decision_idx + 1]):
            historia_text = font.render(line, True, BLACK)
            screen.blit(historia_text, (WIDTH // 2 - historia_text.get_width() // 2, y_offset + i * 25))  # Reducir el espacio entre líneas

        # Mostrar opciones al final del último párrafo
        if decision_idx == len(historia) - 1:
            for i, (texto, accion) in enumerate(opciones):
                boton(WIDTH // 2 - 150, HEIGHT // 2 + 160 + i * 60, 300, 50, texto, globals()[accion])
        
        mostrar_menu()

        pygame.display.flip()  # Actualizar la pantalla

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if decision_idx == len(historia) - 1:
                    # Si el índice es el último, se muestran los botones
                    for i, (texto, accion) in enumerate(opciones):
                        if WIDTH // 2 - 150 < pygame.mouse.get_pos()[0] < WIDTH // 2 + 150 and HEIGHT // 2 + 160 + i * 60 < pygame.mouse.get_pos()[1] < HEIGHT // 2 + 160 + i * 60 + 50:
                            globals()[accion]()  # Llama a la acción correspondiente

        # Si el jugador ha llegado al final de la historia, podemos pasar a la siguiente parte
        if decision_idx < len(historia) - 1:
            decision_idx += 1

    pygame.quit()
    sys.exit()

def ir_a_ciudad():
    global decision_idx
    print("El jugador decide ir a la ciudad.")
    decision_idx = 0  # Vuelves al primer párrafo o a donde quieras continuar

def explorar_bosque():
    global decision_idx
    print("El jugador decide explorar el bosque.")
    decision_idx = 0  # Vuelves al primer párrafo o a donde quieras continuar

def salir():
    """Función para salir del juego."""
    pygame.quit()
    sys.exit()

def seleccionar_personaje():
    jugar()

if __name__ == "__main__":
    seleccionar_personaje()
