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
    resposta = input('Digite um número ou digite: (s-0) para sair: ').lower().replace(' ','')
    if resposta == 's' or resposta == '0':
        print('Saindo...')
        break
    elif not resposta.isnumeric():
        print('Número inválido')
    else:
        num = int(resposta)
        lista.append(num)
if lista == []:
    print('Lista vazia!')
    exit()

print('Os números impressos foram:')
print(lista)
print('-'*70)

# quantidade de notas que foram lidas
print('A quantidade de notas que foram lidas foram:')
print(len(lista))
print('-'*70)

# todas as notas na ordem inversa à que foram informadas, uma abaixo da outra
print('as notas na ordem inversa à que foram informadas, uma abaixo da outra:')
for i in lista[::-1]:
    print(i)
print('-'*70)

# Calcule e mostre a soma das notas
soma = 0
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