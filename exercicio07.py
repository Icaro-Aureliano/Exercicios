'''
7.Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.
'''

from numero_random import int_random

lista = list(map(int,input("Digite 5 numeros >>> ").split()))
# lista = int_random(5)

n1, n2, n3, n4, n5 = lista

soma = 0
multiplicacao = 1
for numero in lista:
    soma += numero
    multiplicacao = multiplicacao * numero

print(f"Soma >> {soma}")
print(f"Multiplicação >> {multiplicacao}")
print(f"Numeros na lista >> {n1} {n2} {n3} {n4} {n5}")
