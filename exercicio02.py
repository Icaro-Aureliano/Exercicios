"""
2.Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
"""

lista = []
while len(lista) < 10:
    try:
        numero = int(input("Insira um numero >> "))
        lista.append(numero)
    except ValueError:
        print("Coloque um nuemro valido")
        continue
    
print("\n<<< Lista normal >>>")

for i in  range(len(lista)):
   
    print(f"{i + 1}º numero >> {lista[i]}")

print("\n>>> Lista invertida <<<")

for i in range(len(lista)):
    i += 1
    print(f"{i}º numero >> {lista[-i]}")
    # print(i, lista[-i])

print(lista)