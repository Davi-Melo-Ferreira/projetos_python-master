import os


os.system('cls')

# alunos = int(input('Digite o número de alunos: '))

# lista = []
# for i in range(1, alunos + 1):

#     nome = input('Diga seu nome: ')
#     lista.append(nome)
# print(lista)

for i in range(1, 4):
    lista = []
    nome = input('Diga seu nome: ').lower()
    peso = float(input('peso: '))
    idade = int(input('Idade: '))
    altura = float(input('Altura: '))
    lista_total = [nome,[peso, idade, altura]]
    lista.append(lista_total)

# if 'a' in lista_total:
#     nome_ind = nome.count(nome)
#     print(f'O nome {nome} está no índice da lista_total : {nome_ind}')
#     print(lista_total[nome_ind])