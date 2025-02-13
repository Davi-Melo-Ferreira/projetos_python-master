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

from operacionais import somar, subtrair, multiplicar, dividir
from operacionais import dividir_inteiro, resto_divisao
 
os.system('cls')

while True:
    a = int(input('Digite um valor para "A" (> 0 e < 11): '))
    if a < 0 or a > 11:
        print('Valor inválido.')
        input('Pressione qualquer tecla para continuar...')
        os.system('cls')

    b = int(input('Digite um valor para "B" (> 0 e < 11): '))
    if b < 0 or b > 11:
        print('Valor inválido.')
        input('Pressione qualquer tecla para continuar...')
        os.system('cls')

    else:
        os.system('cls')
        break

adicao = somar(a, b)
subtracao = subtrair(a, b)
multiplicacao = multiplicar(a, b)
divisao = dividir(a, b)
divisao_inteira = dividir_inteiro(a, b)
divisao_resto = resto_divisao(a, b)

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
    print(f'A soma de {a} + {b} é: {adicao:.2f}')

if opcao == '2':
    print(f'A subtração de {a} - {b} é: {subtracao:.2f}')

if opcao == '3':
    print(f'O produto de {a} * {b} é: {multiplicacao:.2f}')

if opcao == '4':
    print(f'A divisão de {a} / {b} é: {divisao:.2f}')

if opcao == '5':
    print(f'A divisão inteira de {a} // {b} é: {divisao_inteira:.2f}')

if opcao == '6':
    print(f'O resto da divisão de {a} % {b} é: {divisao_resto:.2f}')