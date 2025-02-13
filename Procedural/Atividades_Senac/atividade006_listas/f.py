# Faça um programa que leia 5 nomes, depois imprima estes nomes com seus respectivos índices.
import os


os.system('cls')

lista = []
cont = 0
while True:
    cont += 1
    resp = input(f'Digite o {cont}º nome: ')
    lista.append(resp)
    if cont > 5:
        break


for i in range(0, 5):
    print(f'Nome: {lista[i]} | Quantidade de índices: {len(lista[i])}\n')

nome = input('Qual nome você quer?: ').lower()

for ind in range(len(lista)):
    if nome in lista[ind]:
        print(f'O nome {nome} está no índice {ind}')