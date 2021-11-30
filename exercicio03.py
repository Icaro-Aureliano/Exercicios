"""
3.Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
"""

lista = []
contador = 0
soma = 0 

while len(lista) < 4:
    try:
        contador += 1
        numero = int(input(f"{contador}º Nota >> "))
        lista.append(numero)
    except:
        print("Coloque uma nota valida")
        continue


for numero in lista:
    soma += numero

media = soma / 4
print(f"Media >> {media}")