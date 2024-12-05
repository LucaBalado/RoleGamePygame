import random
from clases import *
"""
habilildades que me faltan:
Circulo de defensa
Curación"
"Bendecir Jugador
"""

def dado(caras):
    return random.randint(1, caras)

def aumentar_armadura(Guerrero):
    aumento_defensa = dado(6)
    Guerrero.ca += aumento_defensa
    return f"El Guerrero aumenta su defensa en {aumento_defensa}, su CA ahora es {Guerrero.ca}"

def aumentar_armadura(Hechicero):
    aumento_defensa = dado(6)
    Hechicero.ca += aumento_defensa
    return f"El Hechicero aumenta su defensa en {aumento_defensa}, su CA ahora es {Hechicero.ca}"

def ataque_normal(Guerrero):
    cd = 11
    dado = dado(20)

    if dado >= cd and dado < 20:

        daño = dado(6)
        return f"El Guerrero realiza un ataque normal (CD: {cd}). Tirada: {dado}. Daño: {daño}."
    elif dado == 20:
        daño = dañoCritico
        dañoCritico = dado(6)+dado(6)
        return f"El ataque normal del Guerrero fue critico: tirada: {dado} natural. Daño: {dañoCritico}."
    else:
        return f"El Guerrero falla el ataque normal (CD: {cd}). Tirada: {dado}. El ataque no tiene efecto."


def ataque_doble(Guerrero):
    cd = 15
    dado = dado(20)

    if dado >= cd and dado < 20:
        daño = dado(12)
        return f"El Guerrero realiza un ataque doble (CD: {cd}). Tirada: {dado}. Daño: {daño}."
    elif dado == 20:
        daño = dañoCritico
        dañoCritico= dado(12)+dado(12)
        return f"El ataque doble del Guerrero fue critico: tirada: {dado} natural. Daño: {dañoCritico}."
    else:
        return f"El Guerrero falla el ataque doble (CD: {cd}). Tirada: {dado}. El ataque no tiene efecto."
    

def bola_fuego(Hechicero):
    cd = 12
    dado = dado(20)

    if dado >= cd and dado < 20:
        daño = dado(12)
        return f"El Hechicero casteó una bola de fuego (CD: {cd}). Tirada: {dado}. Daño: {daño}."
    elif dado == 20:
        daño = dañoCritico
        dañoCritico= dado(12)+dado(12)
        return f"La Bola de fuego del Hechicero fue critico: tirada: {dado} natural. Daño: {dañoCritico}."
    else:
        return f"El Hechicero falla el ataque(CD: {cd}). Tirada: {dado}. El ataque no tiene efecto."