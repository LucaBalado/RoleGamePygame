import razas
class Guerrero:
    def __init__(self):
        self.name= "Guerrero"
        self.ca = 14
        self.accion = ["Ataque Normal", "Ataque Doble"]
        self.accionadicional = ["Circulo de Defensa", "Aumentar Armadura"]

    def realizar_accion(self, accion_idx):
        if accion_idx == 0:
            return "El Guerrero realiza un ataque doble"
        elif accion_idx == 1:
            return "El Guerrero realiza otro ataque doble"
        else:
            return "Acción no válida"

    def realizar_accion_bonus(self, bonus_idx):
        if bonus_idx == 0:
            return "El Guerrero aumenta su defensa"
        elif bonus_idx == 1:
            return "El Guerrero se prepara para resistir más daño"
        else:
            return "Acción bonus no válida"


class Hechicero:
    def __init__(self):
        self.name="Hechicero"
        self.ca=10
        self.accion = ["Curación", "Bola de Fuego"]
        self.accionadicional = ["Aumentar Armadura", "Bendecir Jugador"]

    def realizar_accion(self, accion_idx):
        if accion_idx == 0:
            return "El Hechicero lanza una cura"
        elif accion_idx == 1:
            return "El Hechicero lanza un ataque de fuego"
        else:
            return "Acción no válida"

    def realizar_accion_bonus(self, bonus_idx):
        if bonus_idx == 0:
            return "El Hechicero aumenta su defensa"
        elif bonus_idx == 1:
            return "El Hechicero buffea a su equipo"
        else:
            return "Acción bonus no válida"
