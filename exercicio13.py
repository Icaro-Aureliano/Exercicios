'''
13.Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).
'''
from numero_random import float_random

class Ranking():
    def __init__(self, id, nome, temperatura):
        self.id = id
        self.nome = nome
        self.temperatura = temperatura

    def __str__(self):
        return f"{self.id}--{self.nome}--{self.temperatura}"

meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "desembro"]
temperatura_meses = []
soma_temperatura = 0 

print("\n")
print("<>"*10,"Meses e suas temperaturas!!", "<>"*10)

for i in range(0,len(meses)):
    mes = meses[i].title()
    temperatura = float_random()[0]
    soma_temperatura += temperatura
    ranking = Ranking(i + 1, mes, temperatura)
    temperatura_meses.append(ranking)
    print(ranking)
    
media_temperatura = round(soma_temperatura / len(meses),2)

print("<>"*34)
print("\n")

print(f"Media >> {media_temperatura}")
print("\n")
print("<>"*5,"Meses com temperatura acima da media ","<>"*5)
for mes in temperatura_meses:
    if mes.temperatura >= media_temperatura:
        print(mes)
