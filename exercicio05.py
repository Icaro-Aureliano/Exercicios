'''
5.Faça um Programa que leia 20 números inteiros e armazene-os num vetor. 
Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. 
Imprima os três vetores.
'''

lista_tudo = []
lista_impar = []
lista_par = []

while len(lista_tudo) < 10:
    numero = int(input("Insira um numero >> "))
    lista_tudo.append(numero)

for numero in lista_tudo:
    resultado = numero % 2
    if resultado != 0:
        lista_impar.append(numero)
    else:
        lista_par.append(numero)

print(f"Impares >> {lista_impar}\nPares >> {lista_par}\nTodos os numeros >> {lista_tudo}")