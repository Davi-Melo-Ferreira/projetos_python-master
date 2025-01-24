# Crie um programa que peça ao usuário 2 números maiores que 0 e menores que 11.
# Depois mostre um menu com as seguintes operações:
#1. Soma: 
# 2. Subtração : 
# 3. Produto : 
# 4. Divisão : 
# 5. Divisão inteira : 
# 6. Resto da divisão.
# O usuário deverá escolher um número maior ou  igual a 1 e menor ou igual a 6.
# Em seguida, você criará funções que retornem os resultados das operações, imprimindo os resultados na tela.
import os


os.system('cls')


def somar(a, b):
    soma = a + b
    return soma

def subtrair(a, b):
    subtrai = a - b
    return subtrai

def multiplicar(a, b):
    produto = a * b
    return produto

def dividir(a, b):
    divisao = a / b
    return divisao

def dividir_inteiro(a, b):
    divisao_inteira = a // b
    return divisao_inteira

def resto_divisao(a, b):
    resto = a % b
    return resto

while True:
    a = float(input('Digite um valor para "A" (> 0 e < 11): '))
    if a < 0 or a > 11:
        print('Valor inválido.')
        input('Pressione qualquer tecla para continuar...')
        os.system('cls')

    b = float(input('Digite um valor para "B" (> 0 e < 11): '))
    if b < 0 or b > 11:
        print('Valor inválido.')
        input('Pressione qualquer tecla para continuar...')
        os.system('cls')

    else:
        os.system('cls')
        break

print(f'Valores escolhidos {a} e {b}')
print('-' * 70)
print('1 - Soma')
print('2 - Subtração')
print('3 - Produto')
print('4 - Divisão')
print('5 - Divisão Inteira')
print('6 - Resto da divisão')

opcao = input('\nEscolha 1 ao 6: ')

if opcao == '1':
    print(f'A soma de {a} + {b} é: {somar(a, b):.2f}')

if opcao == '2':
    print(f'A subtração de {a} - {b} é: {subtrair(a, b):.2f}')

if opcao == '3':
    print(f'O produto de {a} * {b} é: {multiplicar(a, b):.2f}')

if opcao == '4':
    print(f'A divisão de {a} / {b} é: {dividir(a, b):.2f}')

if opcao == '5':
    print(f'A divisão inteira de {a} // {b} é: {dividir_inteiro(a, b):.2f}')

if opcao == '6':
    print(f'O resto da divisão de {a} % {b} é: {resto_divisao(a, b):.2f}')