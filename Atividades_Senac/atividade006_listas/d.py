# Faça um programa que preencha uma lista com as notas de 4 alunos, depois imprima a média.
import os


os.system('cls')

lista_nome = []
lista_nota = []

for i in range(1, 5):
    nome = input('Digite o nome do aluno: ')
    lista_nome.append(nome)
    nota = int(input(f'Digite a nota do aluno {nome}: '))
    lista_nota.append(nota)

media = nota/4

print(f'A média é {media}')