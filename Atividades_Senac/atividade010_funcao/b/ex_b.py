#Crie uma função que cadastre o nome de um aluno(a), a matrícula e a data de nascimento.
#Depois imprima os resultados cadastrados utilizando uma estrutura de repetição for.
import os

from modulo_b import cadastro
os.system('cls')

dicionario = {}

nome = input('Digite o Nome do(a) aluno(a): ')
matricula = input('Digite a Matrícula do(a) aluno(a)(max: 4 dígitos): ')
nasc = input('Digite a data de nascimento(ex: 24/03/2006): ')

os.system('cls')

# Invocação da função
matriculado = cadastro(nome, matricula, nasc, dicionario)

for chave, valor in matriculado.items():
    print(f'{chave}: {valor}')