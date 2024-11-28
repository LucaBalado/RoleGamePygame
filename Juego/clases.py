class Clase:
    def __init__(self, habilidades=None):
        if habilidades is None:
            habilidades = []
        self.habilidades = habilidades

    def calcular_dano(self, fuerza, destreza):
        # Implementa el cálculo de daño en la clase base si es necesario
        return fuerza + destreza

class Guerrero(Clase):
    def __init__(self):
        super().__init__(habilidades=["Golpe pesado", "Defensa alta"])

    def calcular_dano(self, fuerza, destreza):
        return fuerza * 2 + destreza  # El Guerrero tiene más fuerza

class Hechicero(Clase):
    def __init__(self):
        super().__init__(habilidades=["Lanzar hechizo", "Control de energía"])

    def calcular_dano(self, fuerza, destreza):
        return fuerza + destreza * 2  # El Hechicero tiene más destreza
