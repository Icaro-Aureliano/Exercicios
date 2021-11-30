'''
12.Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.
'''
from numero_random import int_random, float_random

class Aluno:
    def __init__(self, numero = 0, idade = 0, altura = 0):
        self.numero = numero
        self.idade = idade
        self.altura = altura
    
    def numero(self):
        return self.numero

    def idade(self):
        return self.idade

    def altura(self):
        return self.altura

lista_de_alunos =[]
numero_de_alunos = 0
soma_altura = 0
altura_menor_que_a_media = []
numero_aluno = 0

while len(lista_de_alunos) < 30:
    numero_aluno += 1
    lista_de_alunos.append(Aluno(numero_aluno, int_random()[0] + 10, float_random()[0]))

for aluno in lista_de_alunos:
    numero_de_alunos +=1
    soma_altura += aluno.altura

media_altura = soma_altura / numero_de_alunos

for aluno in lista_de_alunos:
    if aluno.idade <= 13 and aluno.altura >= media_altura:
        altura_menor_que_a_media.append(aluno)

print(">>"*10)
print("\n")

print(f"Altura media: {round(media_altura, 2)}\n \
        \n{len(altura_menor_que_a_media)} Alunos de 13 anos com altura maior ou igual a media.\n")

for i in range(0, len(altura_menor_que_a_media)):
    aluno = altura_menor_que_a_media[i]
    print(f"{i}, Numero aluno:{aluno.numero}º, Altura:{aluno.altura}, Idade:{aluno.idade}")

print("\n")
print("<<"*10)