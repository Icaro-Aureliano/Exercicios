import random

def int_random(valor=1):
    if valor != 1:
        numeros = []  
        while len(numeros) < valor:
            numero = round(random.random()*10)
            numero = numero
            numeros.append(numero)
        return numeros
    else:
        numero = round(random.random()*10)
        return numero

def float_random(valor=1):
    if valor != 1:
        numeros = []
        while len(numeros) < valor:
            numero = random.triangular(1,2)
            numero = round(numero, 2)
            if len(str(numero)) == 4:
                numeros.append(numero)
        return numeros
    else:
        numeros = random.triangular(1,2)
    return numeros

def din_random():
    numero = int_random() * 1000
    return round(numero, 2)