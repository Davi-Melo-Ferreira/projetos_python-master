import os


os.system('cls')


lista_alunos = ''
qntd_alunos = int(input(f'Quantos alunos gostaria de inserir?: '))

for i in range(0, qntd_alunos):
    nome = input(f'Diga o nome do(a) {i+1}º Aluno(a): ')
    lista_alunos += ''.join(nome)
print(f'Alunos: {lista_alunos}')