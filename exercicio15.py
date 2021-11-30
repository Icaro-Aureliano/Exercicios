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

class Valores:
    def __init__(self, lista = []):
        self.lista = lista

    def ordem_dos_valores(self):
        return self.lista

    def ordem_inversa_dos_valores(self):
        ordem_normal = self.ordem_dos_valores()
        ordem_inversa = []
        for i in range(0, len(ordem_normal)):
            i += 1
            ordem_inversa.append(ordem_normal[-i])
        return ordem_normal

    def string_ordem_inversa(self):
        ordem_inversa = ""
        for i in range(0, len(self.lista)):
            ordem_inversa += f"{self.lista[i]} "
        return ordem_inversa

    def soma_valores(self):
        soma = 0 
        for numero in self.lista:
            soma += numero
        return soma

    def media_valores(self): 
        try:
            numero_de_valores = len(self.lista)
            return self.soma_valores() / numero_de_valores

        except TypeError:
            return 0
        
        except ZeroDivisionError:
            return 0

    def numeros_iguais_media(self):
        media = self.media_valores()
        return self.helper("igual", media)

    def numeros_acima_media(self):
        media = self.media_valores()
        return self.helper("maior", media)

    def numeros_abaixo_media(self):
        media = self.media_valores()
        return self.helper("menor", media)

    def numeros_abaixo_7(self):
        return self.helper("menor", 7)

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

numeros = Valores(numeros_digitados)

print(f"Numeros na ordem normal → {numeros.ordem_dos_valores()}")

print("↓ Ordem inversa, um abaixo do outro ↓")
lista = numeros.ordem_inversa_dos_valores()
mensagem = ""

for i in range(0, len(lista)):
    mensagem += f"{lista[i]}\n"
print(mensagem)

print(f"A soma dos numeros → {numeros.soma_valores()}")

print(f"A media de todos os numeros → {numeros.media_valores()}")

print(f"Numeros acima da media → {numeros.numeros_acima_media()}")

print(f"Numeros iguais a media → {numeros.numeros_iguais_media()}")

print(f"Numeros abaixo da media → {numeros.numeros_abaixo_media()}")

print(f"Numeros abaixo de 7 → {numeros.numeros_abaixo_7()}")

print("Nenhum valor inserido")

print("✨ Obrigado pelo teste volte sempre :) ✨")