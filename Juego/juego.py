import pygame
import click

WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
DARK_GRAY = (150, 150, 150)


class Estructura:
    def __init__(self):
        self.running=True
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


@click.command()
@click.argument("escenario")
def main(escenario):
    """Función principal del juego con selección de escenario."""
    pygame.init()
    global screen, font
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    font = pygame.font.Font(None, 36)

    print(f"Escenario seleccionado: {escenario}")

    juego = Estructura()

    if escenario == "pelea" and juego.running:
        from combate import Pelea
        p = Pelea(juego)
        p.main()
    else:
        from menu import Menu
        m = Menu(juego)
        m.main()

        if juego.running:
            from creadorpj import Creacion
            c = Creacion(juego)
            c.main()
            
            from historia import Historia
            h = Historia(juego)
            h.main()

            print("Historia completada")
            print("Iniciando combate...")

            if juego.running:
                from combate import Pelea
                p = Pelea(juego)
                p.main()

    pygame.quit()


if __name__ == '__main__':
    main()
