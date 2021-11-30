'''
14.Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?"
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
'''
from numero_random import int_random

class Pessoa:
    def __init__(self, nome, idade, indole = "inocente"):
        self.nome = nome
        self.indole = indole
        self.idade = idade

    def checar_indole(self,indice):
        if indice == 0:
            self.indole == "inocente"
        elif indice == 1:
            self.indole = "suspeito(a)"
        elif indice == 2 or indice == 3:
            self.indole = "cumplice"
        elif indice == 4:
            self.indole = "assassino(a)"
        else:
            self.indole ="inocente"


    def __str__(self):
        return f"{self.nome}--{self.idade}--{self.indole}"

contador = 0
pessoas = []
registro = {}
arquivo_registro = open("registro_pessoas.txt", "a")

while True:
    try:
        nome = input("Qual seu nome??\n>> ").title()
        if not nome.isdigit():
            idade = int_random()[0]
            pessoa = Pessoa(nome,idade)
            relatorio = [
                input("Telefonou para a vítima?\n>> ").upper(), 
                input("Esteve no local do crime?\n>> ").upper(), 
                input("Mora perto da vitima?\n>> ").upper(), 
                input("Devia para a vitima?\n>> ").upper(), 
                input("Já trabalhou com a vitima?\n>> ").upper()
                ]
            for pergunta in relatorio:
                for i in range(0, len(relatorio)):
                    if relatorio[i] == pergunta and pergunta[0] == "S" :
                        pessoa.checar_indole(i)

            registro[f"{pessoa.nome}"] = pessoa.indole
            ver_registro = input("Quer ver seus registros? >> ").upper()
            if ver_registro == "S":
                print(registro)
            
            continua = input("Quer continuar??").upper()
            if continua == "S":
                continue
            else:
                raise KeyboardInterrupt
        else:
            raise
    except KeyboardInterrupt:
            print("parando programa...")
            break
    except:
        print("Por favor informe seu nome")
        continue
