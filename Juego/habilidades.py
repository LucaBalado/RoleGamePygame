import random
from clases import *
from creadorpj import clase_seleccionada, raza_seleccionada


def dado(caras):
    return random.randint(1, caras)


def aumentar_armadura(personaje):
    aumento_defensa = dado(6)
    personaje['ca'] += aumento_defensa
    return (f"{personaje['nombre']} ({personaje['clase']}) aumenta su defensa en {aumento_defensa}. "
            f"CA actual: {personaje['ca']}.")


def ataque_normal(personaje):
    cd = 12
    tirada = dado(20) + personaje.fuerza


    if tirada >= cd and tirada < 20:
        daño = dado(8) + personaje.fuerza
        return (f"{personaje['nombre']} realiza un ataque normal (CD: {cd}). "
                f"Tirada: {tirada}. Daño: {daño}.")
    elif tirada == 20:
        daño_critico = dado(8) + dado(8) + personaje.fuerza
        return (f"El ataque normal de {personaje['nombre']} fue crítico: "
                f"tirada: {tirada} natural. Daño: {daño_critico}.")
    else:
        return (f"{personaje['nombre']} falla el ataque normal (CD: {cd}). "
                f"Tirada: {tirada}. El ataque no tiene efecto.")


def ataque_doble(personaje):
    cd = 15
    tirada = dado(20) + personaje.fuerza


    if tirada >= cd and tirada < 20:
        daño = dado(12) + personaje.fuerza
        return (f"{personaje['nombre']} realiza un ataque doble (CD: {cd}). "
                f"Tirada: {tirada}. Daño: {daño}.")
    elif tirada == 20:
        daño_critico = dado(12) + dado(12) + personaje.fuerza
        return (f"El ataque doble de {personaje['nombre']} fue crítico: "
                f"tirada: {tirada} natural. Daño: {daño_critico}.")
    else:
        return (f"{personaje['nombre']} falla el ataque doble (CD: {cd}). "
                f"Tirada: {tirada}. El ataque no tiene efecto.")


def bola_fuego(personaje):
    cd = 15
    tirada = dado(20) + personaje.sabiduria


    if tirada >= cd and tirada < 20:
        daño = dado(12) + personaje.sabiduria
        return (f"{personaje['nombre']} casteó una bola de fuego (CD: {cd}). "
                f"Tirada: {tirada}. Daño: {daño}.")
    elif tirada == 20:
        daño_critico = dado(12) + dado(12) + personaje.sabiduria
        return (f"La Bola de fuego de {personaje['nombre']} fue crítico: "
                f"tirada: {tirada} natural. Daño: {daño_critico}.")
    else:
        return (f"{personaje['nombre']} falla el ataque (CD: {cd}). "
                f"Tirada: {tirada}. El ataque no tiene efecto.")


def tiro_con_arco(personaje):
    cd = 10
    tirada = dado(20) + personaje.sabiduria


    if tirada >= cd and tirada < 20:
        daño = dado(6) + personaje.destreza
        return (f"{personaje['nombre']} Disparo una flecha: {cd}). "
                f"Tirada: {tirada}. Daño: {daño}.")
    elif tirada == 20:
        daño_critico = dado(6) + dado(6) + personaje.destreza
        return (f"El impacto de la flecha de {personaje['nombre']} fue crítico: "
                f"tirada: {tirada} natural. Daño: {daño_critico}.")
    else:
        return (f"{personaje['nombre']} falla el ataque (CD: {cd}). "
                f"Tirada: {tirada}. El ataque no tiene efecto.")


def circulo_defensa(jugador1, jugador2):
    aumento1 = dado(4)
    aumento2 = dado(4)
    jugador1['ca'] += aumento1
    jugador2['ca'] += aumento2
    return (f"Se activa Círculo de Defensa. {jugador1['nombre']} aumenta su CA en {aumento1} (CA actual: {jugador1['ca']}). "
            f"{jugador2['nombre']} aumenta su CA en {aumento2} (CA actual: {jugador2['ca']}).")


def curacion(jugador):
    puntos_cura = dado(4) + dado(4)
    jugador['vida'] += puntos_cura
    return (f"{jugador['nombre']} se cura {puntos_cura} puntos de vida. Vida actual: {jugador['vida']}.")





