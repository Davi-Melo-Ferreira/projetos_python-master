import os


os.system('cls')


lista = ''
qntd_alunos = int(input(f'Quantos alunos gostaria de inserir?: '))
i = 0
while i < qntd_alunos:
    i += 1
    nome = str(input(f'Diga o nome do {i}º Aluno(a)'))
    lista += nome + ',' + ' '
print(lista)