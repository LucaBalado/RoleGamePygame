import pygame


ANCHO, ALTO = 1250, 700
TAMANIO_CUADRILLA = 32
COLOR_CUADRILLA = (200, 200, 200)


PORCENTAJE_OCUPACION = 0.7


class Escenario:
    def __init__(self, fondo_path):
        pygame.init()
        self.screen = pygame.display.set_mode((ANCHO, ALTO))
        pygame.display.set_caption("Campo de Batalla")
        self.fondo = pygame.image.load(fondo_path)
        self.fondo = pygame.transform.scale(self.fondo, (ANCHO, ALTO))


        self.cuadras = []
        self.offset_x = 0
        self.offset_y = 0


    def crear_cuadrillas(self):
        """Crea las cuadrillas en el centro, omitiendo la primera fila."""
        filas = int((ALTO * PORCENTAJE_OCUPACION) // TAMANIO_CUADRILLA)
        columnas = int((ANCHO * PORCENTAJE_OCUPACION) // TAMANIO_CUADRILLA)


        self.offset_x = (ANCHO - (columnas * TAMANIO_CUADRILLA)) // 2
        self.offset_y = (ALTO - (filas * TAMANIO_CUADRILLA)) // 2


        for y in range(1, filas):
            for x in range(columnas):
                self.cuadras.append((
                    self.offset_x + x * TAMANIO_CUADRILLA,
                    self.offset_y + y * TAMANIO_CUADRILLA
                ))


    def dibujar_escenario(self):
        """Dibuja el fondo y las cuadrillas."""
        self.screen.blit(self.fondo, (0, 0))


        for cuad in self.cuadras:
            pygame.draw.rect(self.screen, COLOR_CUADRILLA,
                             (*cuad, TAMANIO_CUADRILLA, TAMANIO_CUADRILLA), 1)


    def iniciar_escenario(self):
        """Inicia el bucle principal del escenario."""
        self.crear_cuadrillas()


        corriendo = True
        while corriendo:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    corriendo = False


            self.dibujar_escenario()
            pygame.display.flip()


        pygame.quit()




if __name__ == "__main__":
    escenario = Escenario("assets/peleabosque.png")
    escenario.iniciar_escenario()





