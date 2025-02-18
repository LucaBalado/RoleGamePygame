import pygame
import sys
from combate import *




#pygame.init()


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



class Historia:
    def __init__(self, juego):
        self.juego = juego
        self.running=True
        self.ubicacion_actual = "bosque"

    def ajustar_texto(self, texto, ancho_max):
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
    
    def cerrar(self):
        self.running=False
        self.juego.running=False

    def dibujar_estado_personaje(self):
        if self.juego.raza == "Orco":
            orco_resized = pygame.transform.scale(orco_img, (100, 100))
            screen.blit(orco_resized, (WIDTH - 120, 20))
        elif self.juego.raza == "Humano":
            humano_resized = pygame.transform.scale(humano_img, (100, 100))
            screen.blit(humano_resized, (WIDTH - 120, 20))
        elif self.juego.raza == "Elfo":
            elfo_resized = pygame.transform.scale(elfo_img, (100, 100))
            screen.blit(elfo_resized, (WIDTH - 120, 20))

    def mostrar_texto(self,texto, x, y, ancho_max):
        y_offset = 0
        for linea in self.ajustar_texto(texto, ancho_max):
            render = font.render(linea, True, BLACK)
            screen.blit(render, (x, y + y_offset))
            y_offset += render.get_height() + 5
            
    def inicio(self):
        self.ubicacion_actual = "bosque"
        self.texto= [
                "Mientras viajan por el camino principal, tu grupo de aventureros ve una columna de humo elevándose desde el bosque cercano.",
                "Algo no parece normal. Podría ser una fogata… o una señal de peligro.",
                "Deciden discutir qué hacer a continuación."
            ]
        self.botones = [
                ("Adentrarse en el bosque", self.adentrarse_bosque),
                ("Volver a la ciudad por ayuda", self.volver_ciudad)
            ]


    def adentrarse_bosque(self):
        self.ubicacion_actual = "bosque"
        self.texto= [
                "Deciden no perder tiempo y avanzan rápidamente hacia la fuente del humo.",
                "A medida que se acercan, el olor a madera quemada llena el aire y el resplandor de las llamas se vuelve visible a través de los árboles.",
                "No tardan en descubrir la fuente del humo…"
            ]
        self.botones= [("Seguir adelante", self.descubrir_fuego)]


    def volver_ciudad(self):
        self.ubicacion_actual = "ciudad"
        self.texto= [
                "Deciden que es más prudente avisar a las autoridades de la ciudad antes de investigar.",
                "Sin embargo, en el camino de regreso, se cruzan con un aldeano herido que tropieza fuera del bosque, pidiendo ayuda.",
                "No pueden ignorarlo y deciden acompañarlo de vuelta a la zona del incendio."
            ]
        self.botones= [("Entrar al bosque", self.descubrir_fuego)]


    def descubrir_fuego(self):
        self.ubicacion_actual = "noche"
        self.texto= [
                "Finalmente, cuando cae la noche, logran llegan al claro donde el humo se eleva. Un campamento ha sido destruido, las tiendas aún arden.",
                "Desde dentro del bosque un grupo de bandidos se acercan y claramente tienen malas intenciones.",
                "¡Rapido! Decide que hacer"
            ]
        self.botones = [("huir", self.huir),
                        ("pelear", self.pelear)]


    def huir(self):
        self.texto = ["huiste.", "Fin de la historia."],
        self.botones = ["Terminar juego",lambda: self.cerrar, print("terminaste el juego")]
    
    def pelear(self):
        global running
        
        combate = Pelea("assets/peleabosque.png", f"/assets/sprites/{self.juego.raza.lower()}-{self.juego.clase.lower()}/neutral.png")
        while running:
            combate.main()




    def dibujar_escena(self):
        screen.blit(papiro_fondo, (0, HEIGHT // 2))
        if self.ubicacion_actual == "bosque":
            screen.blit(bosque_fondo, (0, 0))
        elif self.ubicacion_actual == "noche":
            screen.blit(noche_fondo, (0, 0))
        else:
            screen.blit(ciudad_fondo, (0, 0))
            


        self.mostrar_texto("\n".join(self.texto), 20, HEIGHT // 2 + 20, WIDTH - 40)

        evento = None
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.juego.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                evento = event

        y_boton = HEIGHT - 120
        for i, (texto, accion) in enumerate(self.botones):
            x_boton = 50 + i * 400
            self.juego.boton(x_boton, y_boton, 300, 40, texto, accion, evento)

    def main(self):
            self.running=True
            self.inicio()
            while self.running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.running = False


                screen.fill(WHITE)
            
                self.dibujar_escena()
                self.dibujar_estado_personaje()
                pygame.display.flip()


            pygame.quit()
            sys.exit()



