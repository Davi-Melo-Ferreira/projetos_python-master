# Crie uma função que verifica se uma aluno(a) está cadastrado ou não em um dicionário.
# Se estiver cadastrado, imprima o nome desse aluno e o resto dos seus dados.
# O dicionário deverá conter nome, matrícula e a data de nascimento do aluno.
import os


os.system('cls')
cadastro = {}

opcao = 's'
while opcao == 's':
    id = len(cadastro) + 1
    nome = input('Digite o Nome do(a) aluno(a): ')
    matricula = input('Digite a Matrícula do(a) aluno(a)(max: 4 dígitos): ')
    nasc = input('Digite a data de nascimento(ex: 24/03/2006): ')
    
    cadastro[id] = {
        'nome':nome,
        'matrícula':matricula,
        'nascimento':nasc
    }
    opcao = input('Deseja continuar?(s/n): ').lower()

for id, dicionario in cadastro.items():
    print(id,':\n')
    for chave, valor in dicionario.items():
        print(f'{chave} : {valor}')