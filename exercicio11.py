'''
11.Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.
'''

from numero_random import int_random

vetor01 = int_random(10)
vetor02 = int_random(10)
vetor03 = int_random(10)

vetores = []

print(vetor01)
print(vetor02)
i = 0 
while len(vetores) < 30:
    # vetores.extend(lista)
    vetores.append(vetor01[i])
    vetores.append(vetor02[i])
    vetores.append(vetor03[i])
    i += 1 

print("\n")
print("="*20,"Lista com todos os numeros usados.","="*20)
print(vetores)
print(len(vetores))
