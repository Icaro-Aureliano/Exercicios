'''
8.Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.
'''
from numero_random import int_random, float_random

class Pessoa:
    def __init__(self, id, idade, altura):
        self.id = id
        self.idade = idade
        self.altura = altura

    def altura(self):
        return self.altura

    def idade(self):
        return self.idade

lista_pessoa = []
lista_altura = []
lista_idade = []

while len(lista_pessoa) < 5:
    lista_pessoa.append(Pessoa(int_random(), int_random()[0] + 10, float_random()[0]))

for pessoa in lista_pessoa: 
    lista_altura.append(pessoa.altura)
    lista_idade.append(pessoa.idade)

print("*** Idade e altura normais ***")

for i in range(0, len(lista_pessoa)):
    print(f"{i + 1}º -- Idade: {lista_idade[i]} --- Altura: {lista_altura[i]} ")

print("\n")

print("*** Idade e altura inversas ***")


for i in range(0, len(lista_pessoa)):
    i += 1
    print(f"{i}º -- Idade: {lista_idade[-i]} --- Altura: {lista_altura[-i]}")