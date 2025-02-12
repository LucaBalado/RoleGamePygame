import pygame

class Estructura:
    def __init__(self):
        self.running=True
        #esto se setea desde el creadorpj
        self.personaje_seleccionado = None
        self.raza = None
        self.clase = None

    def boton(self, x, y, ancho, alto, texto, accion=None, evento=None):
        mouse = pygame.mouse.get_pos()
        rect_color = GRAY if (x < mouse[0] < x + ancho and y < mouse[1] < y + alto) else DARK_GRAY
        pygame.draw.rect(screen, rect_color, (x, y, ancho, alto))
        text = font.render(texto, True, BLACK)
        screen.blit(text, (x + (ancho - text.get_width()) // 2, y + (alto - text.get_height()) // 2))

        if evento and evento.type == pygame.MOUSEBUTTONDOWN:
            if x < evento.pos[0] < x + ancho and y < evento.pos[1] < y + alto:
                if accion:
                    print(f"Accion boton: {accion}")
                    accion()

    def salir_juego(self):
        self.running = False
    

def main():
    juego = Estructura()
    from menu import Menu
    m = Menu(juego)
    m.main()
    if juego.running:
        from creadorpj import Creacion
        cr=Creacion(juego)
        cr.main()
        from historia import Historia
        h= Historia (juego)
        h.main()
        print("historia")
        print("combate")
        #import historia
    


if __name__ == '__main__':
    pygame.init()
    WIDTH, HEIGHT = 800, 600


    screen = pygame.display.set_mode((WIDTH, HEIGHT))


    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GRAY = (200, 200, 200)
    DARK_GRAY = (150, 150, 150)


    font = pygame.font.Font(None, 36)

    
    main()
    pygame.quit()