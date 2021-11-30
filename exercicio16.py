'''
16.Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com base em comissões. O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana. Por exemplo, um vendedor que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000, ou seja, um total de $470. Escreva um programa (usando um array de contadores) que determine quantos vendedores receberam salários nos seguintes intervalos de valores:
$200 - $299
$300 - $399
$400 - $499
$500 - $599
$600 - $699
$700 - $799
$800 - $899
$900 - $999
$1000 em diante
Desafio: Crie ma fórmula para chegar na posição da lista a partir do salário, sem fazer vários ifs aninhados.
'''
import json
from numero_random import din_random, int_random

class Vendedor:
    def __init__(self, nome):
        self.nome = nome

    def venda_bruta(self):
        return din_random() * 1000

    def comissao(self):
        return ((self.venda_bruta * 9) // 100) + 200

lista_de_vendedores = []
arquivo_nomes = open("nomes.txt", "r")
nomes = arquivo_nomes.read()
nomes_prontos = nomes.replace(" ", "_")
lista_de_nomes = ['Agatha Santos','Samuel da Cruz','Pietro Lopes','Bruna Almeida','Ana Beatriz Souza','Isabella Nascimento','Noah da Mota','Maria Clara Nogueira','Fernando Barbosa','Alice Aragão','Paulo Correia','Bryan Teixeira','Mirella Vieira','Lavínia Carvalho','Alice Caldeira','Danilo Pinto','João Vitor Duarte','Gustavo Porto','Antônio Cardoso','Augusto Nunes']

indice_nome = 0
comissao_min_max = [200,299, 300,399, 400,499, 500,599, 600,699, 700,799, 800,899, 900,999, 1000,1099]
dict_registro = {}
increment = 0 

while len(lista_de_vendedores) < len(lista_de_nomes):
    nome = lista_de_nomes[indice_nome].title()
    vendedor = Vendedor(nome)
    lista_de_vendedores.append(vendedor)
    indice_nome += 1

for i in range(0, len(comissao_min_max)):
    i + increment
    if i != len(comissao_min_max) -1:
        maior = comissao_min_max[i + 1]
    else:
        maior = comissao_min_max[i]
    menor = comissao_min_max[i]
    
    for vendedor in lista_de_vendedores:
        dicio_aux = {}
        dict_vendedor = {}
        vendedor_comissao = vendedor.comissao()
        vendedor_idade = vendedor.idade
        if vendedor_comissao >= menor and vendedor_comissao <= maior:
            dados = {"Comissão":vendedor_comissao,"idade":vendedor_idade}
            dict_vendedor[f"{vendedor.nome}"] = dados
            definicao_chave = f"{menor} a {maior}"
            try:
                chave = dict_registro[definicao_chave]
                if chave:
                    dicio_aux = chave
                    dicio_aux[f"{vendedor.nome}"] = dados
            except KeyError:
                dict_registro[definicao_chave] = dict_vendedor
    increment += 2

print("\n VENDEDORES E SUAS COMISSÕES \n")

for vendedor in lista_de_vendedores:
    print(f"Nome >> {vendedor.nome}, Sua comissao >> {'%.2f' % vendedor.comissao()}")

print("\n CLASSIFICAÇÃO \n")

# print(dict_registro)
for chave in dict_registro.keys():
    print(f"{chave} = {dict_registro[chave]}")
print("\n")