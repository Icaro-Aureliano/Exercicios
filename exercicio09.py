'''
9.Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.
'''

from numero_random import int_random

lista = int_random(10)
numero_ao_quadrado = []

result = 0
for numero in lista:
    numero_ao_quadrado.append(numero**2)
    result += numero**2

print(f"Numeros >> {lista}")
print(f"Numeros ao quadrado >> {numero_ao_quadrado}")
print(f"Soma dos numeros >> {result}")