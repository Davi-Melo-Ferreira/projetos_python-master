# Crie uma função que verifica se uma aluno(a) está cadastrado ou não em um dicionário.
# Se estiver cadastrado, imprima o nome desse aluno e o resto dos seus dados.
# O dicionário deverá conter nome, matrícula e a data de nascimento do aluno.
import os

from modulo_c import cadastrar

os.system('cls')
cadastro = {}

opcao = 's'
while opcao == 's': # loop infinito até opcao == 'n'
    id = len(cadastro) + 1  # linha 21 a 24: entrada
    nome = input('Digite o Nome do(a) aluno(a): ')
    matricula = input('Digite a Matrícula do(a) aluno(a)(max: 4 dígitos): ')
    nascimento = input('Digite a data de nascimento(ex: 24/03/2006): ')
    
    # invocando a função
    cadastramento = cadastrar(id, nome, matricula, nascimento, cadastro)    

    opcao = input('Deseja continuar?(s/n): ').lower()
    
    os.system('cls')

for id_chave, dicionario in cadastro.items():
    print(id_chave,'ª Matrícula:')
    
    for chave, valor in dicionario.items():
        print(f'{chave} : {valor}')