"""
4.Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.
"""

from typing import DefaultDict
lista = DefaultDict(int)

palavra = input(f"Uma palavra >> ")
vogais_quantia = 0
consoantes_quantia = 0

vogal = "aeiou"
for letra in palavra:
    if letra in vogal:
        vogais_quantia += 1
    else:
        consoantes_quantia += 1
print(f"Vogais {vogais_quantia}, Consoantes {consoantes_quantia}")

