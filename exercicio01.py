"""
1.Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.
"""

lista = []
while len(lista) < 5:
    try:
        numero = int(input("Insira um numero >> "))
        lista.append(numero)
    except ValueError:
        print("Coloque um numero valido")
        continue
    
for numero in lista:
    print(numero)

print(lista)