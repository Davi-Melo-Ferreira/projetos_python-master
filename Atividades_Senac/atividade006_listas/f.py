# Faça um programa que leia 5 nomes, depois imprima estes nomes com seus respectivos índices.
import os


os.system('cls')
lista = ['Davi', 'Thiago', 'Kayky', 'Francisco', 'Nicolas']
# 4, 6, 5, 9, 7
for i in range(0, 5):
    print(f'Nome: {lista[i]} | índice: {len(lista[i])}\n')