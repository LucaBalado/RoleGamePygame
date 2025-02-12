import pygame
from pjbase import guardar_personaje, razas, clases
import datos_personaje




pygame.init()


WIDTH, HEIGHT = 800, 600


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Creador de Personaje")


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
DARK_GRAY = (150, 150, 150)


font = pygame.font.Font(None, 36)


assets = {
    ("Humano", "Guerrero"): pygame.image.load("assets/Humano-Guerrero.png"),
    ("Humano", "Hechicero"): pygame.image.load("assets/Humano-Hechicero.png"),
    ("Elfo", "Guerrero"): pygame.image.load("assets/Elfo-Guerrero.png"),
    ("Elfo", "Hechicero"): pygame.image.load("assets/Elfo-Hechicero.png"),
    ("Orco", "Guerrero"): pygame.image.load("assets/Orco-Guerrero.png"),
    ("Orco", "Hechicero"): pygame.image.load("assets/Orco-Hechicero.png"),
}


print(f"Tipo de razas: {type(razas)}")
print(f"Tipo de clases: {type(clases)}")


if isinstance(razas, dict):
    razas = list(razas.keys())


if isinstance(clases, dict):
    clases = list(clases.keys())


raza_idx, clase_idx = 0, 0
running = True


def boton(x, y, ancho, alto, texto, accion=None, evento=None):
    mouse = pygame.mouse.get_pos()
    rect_color = GRAY if (x < mouse[0] < x + ancho and y < mouse[1] < y + alto) else DARK_GRAY
    pygame.draw.rect(screen, rect_color, (x, y, ancho, alto))
    text = font.render(texto, True, BLACK)
    screen.blit(text, (x + (ancho - text.get_width()) // 2, y + (alto - text.get_height()) // 2))


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


def creacion_personaje():
    global running
    while running:
        screen.fill(WHITE)
        raza_text = font.render(f"{razas[raza_idx]}", True, WHITE)
        clase_text = font.render(f"{clases[clase_idx]}", True, WHITE)


        key = (razas[raza_idx], clases[clase_idx])
        if key in assets:
            image = assets[key]
            scaled_image = pygame.transform.scale(image, (WIDTH, HEIGHT))
            screen.blit(scaled_image, (0,0))


        evento_actual = None
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                evento_actual = event


        boton(150, 50, 50, 30, "<--", lambda: cambiar_raza(-1), evento_actual)
        boton(WIDTH - 200, 50, 50, 30, "-->", lambda: cambiar_raza(1), evento_actual)
        screen.blit(raza_text, (WIDTH // 2 - raza_text.get_width() // 2, 50))


        boton(150, HEIGHT - 100, 50, 30, "<--", lambda: cambiar_clase(-1), evento_actual)
        boton(WIDTH - 200, HEIGHT - 100, 50, 30, "-->", lambda: cambiar_clase(1), evento_actual)
        screen.blit(clase_text, (WIDTH // 2 - clase_text.get_width() // 2, HEIGHT - 100))


        boton(WIDTH // 4 - 100, HEIGHT - 50, 150, 40, "Volver", menu_inicial, evento_actual)
        boton(3 * WIDTH // 4 - 100, HEIGHT - 50, 150, 40, "Jugar", lambda: [guardar_actual(), iniciar_juego()], evento_actual)


        pygame.display.flip()


def menu_inicial():
    global running
    while running:
        screen.fill(WHITE)
        title_text = font.render("Menú Principal", True, BLACK)
        screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, HEIGHT // 4))


        evento_actual = None
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                evento_actual = event


        boton(WIDTH // 2 - 100, HEIGHT // 2 - 50, 200, 50, "Iniciar", creacion_personaje, evento_actual)
        boton(WIDTH // 2 - 100, HEIGHT // 2 + 50, 200, 50, "Salir", salir_juego, evento_actual)


        pygame.display.flip()


def guardar_actual():
    raza = razas[raza_idx]
    clase = clases[clase_idx]
    guardar_personaje(raza, clase)
    datos_personaje.personaje_seleccionado = {"raza": raza, "clase": clase}
    print("Guardado:", datos_personaje.personaje_seleccionado)
    return raza, clase


personaje_seleccionado = guardar_actual()


def salir_juego():
    global running
    running = False


def iniciar_juego():
    from historia import jugar
    global running
    while running:
        jugar()


raza_seleccionada, clase_seleccionada = guardar_actual()


if __name__ == '__main__':
    menu_inicial()
    pygame.quit()





