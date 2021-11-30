'''
10.Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.
'''

from numero_random import int_random

vetor01 = int_random(10)
vetor02 = int_random(10)
vetores = []

print(vetor01)
print(vetor02)
i = 0 
while i < 10:
    # vetores.extend(lista)
    vetores.append(vetor01[i])
    vetores.append(vetor02[i])
    i += 1 

print(vetores)