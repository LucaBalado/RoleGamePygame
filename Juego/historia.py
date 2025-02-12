import pygame
import sys
from combate import *




pygame.init()


WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Historia Interactiva")


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
DARK_GRAY = (150, 150, 150)


font = pygame.font.Font(None, 24)


running = True


bosque_fondo = pygame.image.load("assets/bosque.png")
bosque_fondo = pygame.transform.scale(bosque_fondo, (WIDTH, HEIGHT // 2))
noche_fondo = pygame.image.load("assets/bosquenoche.png")
noche_fondo = pygame.transform.scale(noche_fondo, (WIDTH, HEIGHT // 2))
ciudad_fondo = pygame.image.load("assets/ciudad.png")
ciudad_fondo = pygame.transform.scale(ciudad_fondo, (WIDTH, HEIGHT // 2))
papiro_fondo = pygame.image.load("assets/papiro.png")
papiro_fondo = pygame.transform.scale(papiro_fondo, (WIDTH, HEIGHT // 2))


orco_img = pygame.image.load("assets/Orcosplashart.png")
humano_img = pygame.image.load("assets/Humanosplashart.png")
elfo_img = pygame.image.load("assets/Elfosplashart.png")


ubicacion_actual = "bosque"


def ajustar_texto(texto, ancho_max):
    palabras = texto.split(' ')
    lineas = []
    linea_actual = ""


    for palabra in palabras:
        prueba_linea = f"{linea_actual} {palabra}".strip()
        if font.size(prueba_linea)[0] > ancho_max:
            lineas.append(linea_actual)
            linea_actual = palabra
        else:
            linea_actual = prueba_linea


    if linea_actual:
        lineas.append(linea_actual)


    return lineas




def salir():
    pygame.quit()
    sys.exit()


def mostrar_menu():
    boton(10, 10, 150, 40, "Salir", salir)




def dibujar_estado_personaje():
    from creadorpj import guardar_actual
   
    raza_actual, _ = guardar_actual()


    if raza_actual == "Orco":
        orco_resized = pygame.transform.scale(orco_img, (100, 100))
        screen.blit(orco_resized, (WIDTH - 120, 20))
    elif raza_actual == "Humano":
        humano_resized = pygame.transform.scale(humano_img, (100, 100))
        screen.blit(humano_resized, (WIDTH - 120, 20))
    elif raza_actual == "Elfo":
        elfo_resized = pygame.transform.scale(elfo_img, (100, 100))
        screen.blit(elfo_resized, (WIDTH - 120, 20))








def mostrar_texto(texto, x, y, ancho_max):
    y_offset = 0
    for linea in ajustar_texto(texto, ancho_max):
        render = font.render(linea, True, BLACK)
        screen.blit(render, (x, y + y_offset))
        y_offset += render.get_height() + 5




def inicio():
    global ubicacion_actual
    ubicacion_actual = "bosque"
    return {
        "texto": [
            "Mientras viajan por el camino principal, tu grupo de aventureros ve una columna de humo elevándose desde el bosque cercano.",
            "Algo no parece normal. Podría ser una fogata… o una señal de peligro.",
            "Deciden discutir qué hacer a continuación."
        ],
        "botones": [
            ("Adentrarse en el bosque", adentrarse_bosque),
            ("Volver a la ciudad por ayuda", volver_ciudad)
        ]
    }


def adentrarse_bosque():
    global ubicacion_actual
    ubicacion_actual = "bosque"
    return {
        "texto": [
            "Deciden no perder tiempo y avanzan rápidamente hacia la fuente del humo.",
            "A medida que se acercan, el olor a madera quemada llena el aire y el resplandor de las llamas se vuelve visible a través de los árboles.",
            "No tardan en descubrir la fuente del humo…"
        ],
        "botones": [("Seguir adelante", descubrir_fuego)]
    }


def volver_ciudad():
    global ubicacion_actual
    ubicacion_actual = "ciudad"
    return {
        "texto": [
            "Deciden que es más prudente avisar a las autoridades de la ciudad antes de investigar.",
            "Sin embargo, en el camino de regreso, se cruzan con un aldeano herido que tropieza fuera del bosque, pidiendo ayuda.",
            "No pueden ignorarlo y deciden acompañarlo de vuelta a la zona del incendio."
        ],
        "botones": [("Entrar al bosque", descubrir_fuego)]
    }


def descubrir_fuego():
    global ubicacion_actual
    ubicacion_actual = "noche"
    return {
        "texto": [
            "Finalmente, cuando cae la noche, logran llegan al claro donde el humo se eleva. Un campamento ha sido destruido, las tiendas aún arden.",
            "Desde dentro del bosque un grupo de bandidos se acercan y claramente tienen malas intenciones.",
            "¡Rapido! Decide que hacer"
        ],
        "botones": [("huir", huir),
                    ("pelear", pelear)]
    }


def huir():
    return {
        "texto": ["huiste.", "Fin de la historia."],
        "botones": []
    }
   
def pelear():
    global running
    while running:
        Combate.main()




def dibujar_escena(escena):
    if ubicacion_actual == "bosque":
        screen.blit(bosque_fondo, (0, 0))
    elif ubicacion_actual == "noche":
        screen.blit(noche_fondo, (0, 0))
    else:
        screen.blit(ciudad_fondo, (0, 0))
    screen.blit(papiro_fondo, (0, HEIGHT // 2))


    mostrar_texto("\n".join(escena["texto"]), 20, HEIGHT // 2 + 20, WIDTH - 40)


    y_boton = HEIGHT - 120
    for i, (texto, accion) in enumerate(escena["botones"]):
        x_boton = 50 + i * 400
        boton(x_boton, y_boton, 300, 40, texto, accion)




def boton(x, y, ancho, alto, texto, accion=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    rect_color = GRAY if x < mouse[0] < x + ancho and y < mouse[1] < y + alto else DARK_GRAY


    pygame.draw.rect(screen, rect_color, (x, y, ancho, alto))
    text = font.render(texto, True, BLACK)
    screen.blit(text, (x + (ancho - text.get_width()) // 2, y + (alto - text.get_height()) // 2))


    if click[0] and x < mouse[0] < x + ancho and y < mouse[1] < y + alto:
        if accion:
            pygame.time.delay(200)
            global escena_actual
            escena_actual = accion()




def jugar():
    global escena_actual
    escena_actual = inicio()


    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        screen.fill(WHITE)
       
        dibujar_escena(escena_actual)
        dibujar_estado_personaje()
        pygame.display.flip()


    pygame.quit()
    sys.exit()




if __name__ == "__main__":
    jugar()



