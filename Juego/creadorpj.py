import pygame
import sys

# Configuración inicial de Pygame
pygame.init()

# Dimensiones de la pantalla
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("El Destino del Reino")

# Colores y fuentes
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
font = pygame.font.Font(None, 36)

# Cargar imágenes
bosque_imagen = pygame.image.load("assets/bosque.png")  # Imagen del bosque
papiro_imagen = pygame.image.load("assets/papiro.png")  # Imagen del papiro
splashart_humano = pygame.image.load("assets/Orco-Splashart.png")  # Imagen de splashart para Humano
splashart_elfo = pygame.image.load("assets/Orco-Splashart.png")  # Imagen de splashart para Elfo
splashart_orco = pygame.image.load("assets/Orco-Splashart.png")  # Imagen de splashart para Orco

# Escalar las imágenes para que no sean demasiado grandes
splashart_humano = pygame.transform.scale(splashart_humano, (100, 100))  # Tamaño pequeño para el splashart
splashart_elfo = pygame.transform.scale(splashart_elfo, (100, 100))  # Tamaño pequeño para el splashart
splashart_orco = pygame.transform.scale(splashart_orco, (100, 100))  # Tamaño pequeño para el splashart

# Información de vida y XP para cada raza
vida = 100
xp = 0

# Función para dividir el texto largo en varias líneas
def dividir_texto(texto, ancho_maximo):
    lineas = []
    palabras = texto.split(" ")
    linea_actual = ""
    
    for palabra in palabras:
        # Verifica si agregar la palabra a la línea actual excede el ancho máximo
        if font.size(linea_actual + palabra)[0] <= ancho_maximo:
            linea_actual += palabra + " "
        else:
            # Si excede el ancho máximo, agrega la línea y comienza una nueva línea
            lineas.append(linea_actual)
            linea_actual = palabra + " "
    
    # Asegurarse de agregar la última línea
    if linea_actual:
        lineas.append(linea_actual)
    
    return lineas

# Función para dibujar un botón
def dibujar_boton(x, y, ancho, alto, texto, color_base=(150, 150, 150), color_hover=(200, 200, 200)):
    mouse_pos = pygame.mouse.get_pos()
    color_boton = color_hover if (x < mouse_pos[0] < x + ancho and y < mouse_pos[1] < y + alto) else color_base
    
    # Dibujar el botón
    pygame.draw.rect(screen, color_boton, (x, y, ancho, alto))
    text = font.render(texto, True, BLACK)
    screen.blit(text, (x + (ancho - text.get_width()) // 2, y + (alto - text.get_height()) // 2))

# Función para mostrar la pantalla dividida con texto en el papiro
def mostrar_historia_con_imagen(texto):
    # Llenar la pantalla con blanco
    screen.fill(WHITE)

    # Mostrar la imagen del bosque en la mitad superior
    screen.blit(bosque_imagen, (0, 0))  # Bosque en la mitad superior

    # Mostrar la imagen del papiro en la mitad inferior
    screen.blit(papiro_imagen, (0, HEIGHT // 2))  # Papiro en la mitad inferior

    # Dividir el texto largo en líneas para que se ajuste dentro del papiro
    lineas = dividir_texto(texto, WIDTH - 40)  # 40px de margen
    y_offset = HEIGHT // 2 + 20  # Comienza a mostrar el texto en la parte inferior

    # Dibujar las líneas de texto dentro del papiro
    for linea in lineas:
        story_text = font.render(linea, True, BLACK)
        screen.blit(story_text, (20, y_offset))  # 20px de margen
        y_offset += story_text.get_height() + 5  # Espaciado entre líneas

    pygame.display.flip()

# Función para mostrar la información del personaje (splashart, vida, xp)
def mostrar_info_personaje(raza_seleccionada):
    # Mostrar el splashart de la raza seleccionada
    if raza_seleccionada == "Humano":
        screen.blit(splashart_humano, (20, 20))
    elif raza_seleccionada == "Elfo":
        screen.blit(splashart_elfo, (20, 20))
    elif raza_seleccionada == "Orco":
        screen.blit(splashart_orco, (20, 20))
    
    # Mostrar vida y XP
    vida_texto = font.render(f"Vida: {vida}", True, BLACK)
    screen.blit(vida_texto, (20, 130))  # Mostrar vida debajo del splashart
    
    xp_texto = font.render(f"XP: {xp}", True, BLACK)
    screen.blit(xp_texto, (20, 170))  # Mostrar XP debajo de la vida

# Función para gestionar el flujo de la historia
def iniciar_juego():
    raza_seleccionada = "Humano"  # Esto puede ser dinámico, dependiendo de la selección del jugador
    running = True
    while running:
        for event in pygame.event.get():
            # Cerrar el juego si el usuario hace clic en la X de la ventana
            if event.type == pygame.QUIT:
                running = False
            
            # Comprobar si se hace clic en las opciones
            if event.type == pygame.MOUSEBUTTONDOWN:
                if WIDTH // 4 - 100 < event.pos[0] < WIDTH // 4 + 50 and HEIGHT - 80 < event.pos[1] < HEIGHT - 40:
                    print("Elegiste Combate")
                    # Aquí puedes agregar la lógica para iniciar el combate
                    # Por ejemplo, importando y ejecutando el archivo combate.py
                if 3 * WIDTH // 4 - 100 < event.pos[0] < 3 * WIDTH // 4 + 50 and HEIGHT - 80 < event.pos[1] < HEIGHT - 40:
                    print("Elegiste Explorar")
                    # Aquí puedes agregar la lógica para explorar el mundo

        # Texto para mostrar dentro del papiro
        texto_historia = "Has llegado al Bosque Prohibido. El aire se siente denso y el peligro acecha en cada sombra. ¿Qué harás?"

        # Mostrar la historia con las imágenes de fondo
        mostrar_historia_con_imagen(texto_historia)

        # Mostrar la información del personaje (splashart, vida, XP)
        mostrar_info_personaje(raza_seleccionada)

        # Mostrar las opciones dentro del papiro
        dibujar_boton(WIDTH // 4 - 100, HEIGHT - 80, 150, 40, "Combate")
        dibujar_boton(3 * WIDTH // 4 - 100, HEIGHT - 80, 150, 40, "Explorar")

        pygame.display.flip()

# Iniciar el juego
iniciar_juego()

pygame.quit()
