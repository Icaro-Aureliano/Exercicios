'''
15.Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:
Mostre a quantidade de valores que foram lidos;
Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
Calcule e mostre a soma dos valores;
Calcule e mostre a média dos valores;
Calcule e mostre a quantidade de valores acima da média calculada;
Calcule e mostre a quantidade de valores abaixo de sete;
Encerre o programa com uma mensagem;
'''

# import pdb
class Numeros:
    def __init__(self, lista = []):
        self.lista = lista

    def ordem_normal(self):
        msg_normal= ""
        for item in self.lista:
            msg_normal += f"{item} "
        return msg_normal

    def ordem_inversa(self):
        # msg_inversa = ""
        msg_normal = self.ordem_normal()
        lista = msg_normal.split()
        for i in range(0, len(lista)):
            i += 1
            print(lista[-i])
        #msg_inversa += f"{lista[-i]} "
        # return msg_inversa

    def soma_valores(self):
        soma = 0 
        for numero in self.lista:
            soma += numero
        return soma

    def media_valores(self):
        numeros = len(self.lista)
        try:
            return self.soma_valores() / numeros
        except:
            return 0

    def numeros_iguais_media(self):
        media = self.media_valores()
        return self.helper("igual", media)

    def numeros_abaixo_media(self):
        media = self.media_valores()
        return self.helper("menor", media)

    def numeros_abaixo_7(self):
        return self.helper("menor", 7)

    def numeros_acima_media(self):
        media = self.media_valores()
        return self.helper("maior", media)

    def helper(self, sinal, media):
        lista_result = []
        for numero in self.lista:
            if sinal == "igual":
                if numero == media:
                    lista_result.append(numero)

            if sinal == "maior":
                if numero > media:
                    lista_result.append(numero)
            
            if sinal == "menor":
                if numero < media:
                    lista_result.append(numero)
        
        return lista_result


numeros_digitados = []

while True:
    try:
        print("Para encerrar -1")
        numero = int(input("Insira um numero >> "))
        if numero != -1:
            numeros_digitados.append(numero)

        else:
            break
    except KeyboardInterrupt:
        print("Parando programa...")
        break
    except:
        print("Porfavor insira um numero valido")
        continue

# pdb.set_trace()
numeros = Numeros(numeros_digitados)

print(f"Numeros na ordem normal → {numeros.ordem_normal()}")

print("↓ Ordem inversa, um abaixo do outro ↓")
numeros.ordem_inversa()

print(f"A soma dos numeros → {numeros.soma_valores()}")

print(f"A media de todos os numeros → {numeros.media_valores()}")

print(f"Numeros acima da media → {numeros.numeros_acima_media()}")

print(f"Numeros iguais a media → {numeros.numeros_iguais_media()}")

print(f"Numeros abaixo da media → {numeros.numeros_abaixo_media()}")
print(f"Numeros abaixo de 7 → {numeros.numeros_abaixo_7()}")

print("Nenhum valor inserido")

print("✨ Obrigado pelo teste volte sempre :) ✨")


