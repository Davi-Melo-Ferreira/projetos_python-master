#Crie uma função que cadastre o nome de um aluno(a), a matrícula e a data de nascimento.
#Depois imprima os resultados cadastrados utilizando uma estrutura de repetição for.
import os


os.system('cls')
dicio = {}

def cadastro(dicio):
    nome = input('Digite o Nome do(a) aluno(a): ')
    matricula = input('Digite a Matrícula do(a) aluno(a)(max: 4 dígitos): ')
    nasc = input('Digite a data de nascimento(ex: 24/03/2006): ')
    dicio = {}
    dicio.update({'nome':nome, 'matricula':matricula, 'nascimento': nasc})
    return dicio

# Invocação da função
(dicio) = cadastro(dicio)

for chave, valor in dicio.items():
    print(f'{chave}: {valor}')