class RazaBase:
    def __init__(self, vida, velocity, fuerza, destreza):
        self.vida = vida
        self.velocity = velocity
        self.fuerza = fuerza
        self.destreza = destreza


class Humano(RazaBase):
    def __init__(self):
        self.name = "Humano"
        super().__init__(vida=20, velocity=7, fuerza=0, destreza=0)


class Elfo(RazaBase):
    def __init__(self):
        self.name = "Elfo"
        super().__init__(vida=15, velocity=5, fuerza=-1, destreza=1)


class Orco(RazaBase):
    def __init__(self):
        self.name= "Orco"
        super().__init__(vida=25, velocity=3, fuerza=1, destreza=-1)
