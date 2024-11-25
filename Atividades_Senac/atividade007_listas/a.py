#Faça um programa que leia um número indeterminado de notas (pressione ‘s’ ou ‘0’ para sair). 
# Após esta entrada de dados, faça o seguinte:
# • Mostre a quantidade de notas que foram lidas.
# • Exiba todas as notas na ordem em que foram informadas.
# • Exiba todas as notas na ordem inversa à que foram informadas, uma abaixo da outra.
# • Calcule e mostre a soma das notas.
# • Calcule e mostre a média das notas.
import os


os.system('cls')

# imprimir números aleatórios em uma lista
lista = []
while True:
    resp = input('Digite um número ou digite: (s-0) para sair: ')
    if resp == 's' or resp == '0':
        break
    else:
        num = int(resp)
        lista.append(num)

print('Os números impressos foram:')
print(lista)
print('-'*70)

# quantidade de notas que foram lidas
print('A quantidade de notas que foram lidas foram:')
print(len(lista))
print('-'*70)

# todas as notas na ordem inversa à que foram informadas, uma abaixo da outra
print('as notas na ordem inversa à que foram informadas, uma abaixo da outra:')
ind = len(lista)
for i in lista:
    ind -= 1
    print(lista[ind])
print('-'*70)

# Calcule e mostre a soma das notas
soma = int(0)
for nota in lista:
    soma += nota
print('a soma das notas:')
print(soma)
print('-'*70)

# Calcule e mostre a média das notas.
media = soma/len(lista)
print('a média das notas:')
print(media)
print('-'*70)