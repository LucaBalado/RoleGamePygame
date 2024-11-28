class PersonajeBase:
    def __init__(self, x, y, width=44, height=80):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vida = 0
        self.velocity = 0
        self.fuerza = 0
        self.destreza = 0
        self.habilidades = []
        self.raza = None
        self.clase = None

    def configurar_personaje(self, raza, clase):
       #Configura los atributos del personaje según la raza y la clase.
        self.raza = raza
        self.clase = clase
        self.vida = raza.vida
        self.velocity = raza.velocity
        self.fuerza = raza.fuerza
        self.destreza = raza.destreza
        self.habilidades.extend(clase.habilidades)

    def calcular_dano(self):
        #Calcula el daño usando la clase asignada.
        if self.clase:
            return self.clase.calcular_dano(self.fuerza, self.destreza)
        else:
            return 0

    def mostrar_info(self):
       #Muestra información del personaje.
        return f"Raza: {self.raza.__class__.__name__}, Clase: {self.clase.__class__.__name__}, " \
               f"Vida: {self.vida}, Fuerza: {self.fuerza}, Destreza: {self.destreza}, " \
               f"Habilidades: {', '.join(self.habilidades)}"
