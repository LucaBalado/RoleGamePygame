import pygame
from pjbase import guardar_personaje, razas, clases

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
def cambiar_raza(accion):
    global raza_idx
    raza_idx = (raza_idx + accion) % len(razas)


def cambiar_clase(accion):
    global clase_idx
    clase_idx = (clase_idx + accion) % len(clases)


class Creacion:
    def __init__(self, juego):
        self.juego = juego
        self.running=True

    def main(self):
        while self.running:
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
                    self.juego.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    evento_actual = event


            self.juego.boton(150, 50, 50, 30, "<--", lambda: cambiar_raza(-1), evento_actual)
            self.juego.boton(WIDTH - 200, 50, 50, 30, "-->", lambda: cambiar_raza(1), evento_actual)
            screen.blit(raza_text, (WIDTH // 2 - raza_text.get_width() // 2, 50))


            self.juego.boton(150, HEIGHT - 100, 50, 30, "<--", lambda: cambiar_clase(-1), evento_actual)
            self.juego.boton(WIDTH - 200, HEIGHT - 100, 50, 30, "-->", lambda: cambiar_clase(1), evento_actual)
            screen.blit(clase_text, (WIDTH // 2 - clase_text.get_width() // 2, HEIGHT - 100))


            self.juego.boton(3 * WIDTH // 4 - 100, HEIGHT - 50, 150, 40, "Jugar", lambda: [self.continuar()], evento_actual)


            pygame.display.flip()

    def guardar_actual(self): 
        self.juego.raza = razas[raza_idx]
        self.juego.clase = clases[clase_idx]
        self.juego.personaje_seleccionado = {"raza": self.juego.raza, "clase": self.juego.clase}
        print("Guardado:", self.juego.personaje_seleccionado)
        return self.juego.raza, self.juego.clase

    def continuar(self):
        self.guardar_actual()
        self.running=False