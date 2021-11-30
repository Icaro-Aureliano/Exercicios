'''
6.Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.
'''
from numero_random import int_random# nela vc passa o numero de notas que vc quer que gere

class Aluno:
    def __init__(self, numero=0, n1=0, n2=0, n3=0, n4=0):
        self.numero = numero
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3
        self.n4 = n4
        self.media = (self.n1 + self.n2 + self.n3 + self.n4) / 4

    def media(self):
         return (self.n1 + self.n2 + self.n3 + self.n4) / 4

    def __str__(self):
        return f"Numero: {self.numero}\nNotas: {self.n1}, {self.n2}, {self.n3}, {self.n4}\nMedia: {self.media}"
         
lista_alunos = []
passaram = []
numero = 0 

while len(lista_alunos) < 10:
    numero += 1
    n1, n2, n3, n4 = int_random(4)
    lista_alunos.append(Aluno(numero, n1, n2 , n3, n4))

for aluno in lista_alunos:
    # print(aluno)
    if aluno.media >= 7:
       passaram.append(aluno)
    
print(f"De {len(lista_alunos)}, os alunos que passaram foram:")
for aluno in passaram:
    print(f"Aluno de numero: {aluno.numero}")
    
print(f"Alunos com a media maior que 7: {len(passaram)}")
