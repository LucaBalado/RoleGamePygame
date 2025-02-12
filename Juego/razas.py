class RazaBase:
    def __init__(self, nombre, vida, velocity, fuerza, destreza, sabiduria):
        self.nombre = nombre
        self.vida = vida
        self.velocity = velocity
        self.fuerza = fuerza
        self.destreza = destreza
        self.sabiduria = sabiduria


class Humano(RazaBase):
    def __init__(self):
        super().__init__("Humano", 20, 7, 0, 1, 0)




class Elfo(RazaBase):
    def __init__(self):
        super().__init__("Elfo", 15, 5, -1, 0, 1)




class Orco(RazaBase):
    def __init__(self):
        super().__init__("Orco", 25, 3, 1, 0, -1)



