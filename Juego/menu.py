import pygame

WIDTH, HEIGHT = 800, 600


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Inicio")


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
DARK_GRAY = (150, 150, 150)


font = pygame.font.Font(None, 36)

class Menu:
    def __init__(self, juego):
        self.juego = juego

    def continuar(self):
        self.running = False
    def cerrar(self):
        self.running=False
        self.juego.running=False

    def main(self):
        self.running=True
        while self.running:
            screen.fill(WHITE)
            title_text = font.render("Menú Principal", True, BLACK)
            screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, HEIGHT // 4))


            evento_actual = None
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.juego.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    evento_actual = event
        
            self.juego.boton(WIDTH // 2 - 100, HEIGHT // 2 - 50, 200, 50, "Iniciar", lambda: self.continuar(), evento_actual)
            self.juego.boton(WIDTH // 2 - 100, HEIGHT // 2 + 50, 200, 50, "Salir", lambda:self.cerrar(), evento_actual)

            pygame.display.flip()