from razas import Humano, Elfo, Orco
from clases import Guerrero, Hechicero
import pygame


razas = {
    "Humano": Humano(),
    "Elfo": Elfo(),
    "Orco": Orco()
}


clases = {
    "Guerrero": Guerrero(),
    "Hechicero": Hechicero()
}


def guardar_personaje(raza, clase):
    elpersonaje = {
        "Raza": raza,
        "Clase": clase
    }




def nuevo_personaje(raza_seleccionada, clase_seleccionada):
    """Crea un personaje combinando raza y clase seleccionadas."""
    if raza_seleccionada not in razas or clase_seleccionada not in clases:
        raise ValueError("Raza o clase seleccionada no válida.")


    raza = razas[raza_seleccionada]
    clase = clases[clase_seleccionada]


    personaje = {
        "nombre": "Nuevo Personaje",
        "raza": raza.nombre,
        "clase": clase.nombre,
        "fuerza": raza.fuerza,
        "sabiduria": raza.sabiduria,
        "destreza": raza.destreza,
        "ca": clase.ca,
        "vida": raza.vida,
        "acciones": clase.accion,
        "acciones_bonus": clase.accionadicional,
        "posicion": 0
    }


    return personaje


if __name__ == "__main__":
    personaje = nuevo_personaje("Elfo", "Guerrero")
    print(personaje)





