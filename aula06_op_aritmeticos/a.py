#Biblioteca
import os

# Limpar Terminal
os.system('cls')

# Entrada
valor_1 = float(input('1º valor: '))
valor_2 = float(input('2º valor: '))
valor_3 = float(input('3º valor: '))

# Processamento
soma = valor_1 + valor_2 + valor_3
multiplicacao = valor_1 * valor_2 * valor_3

# Saída Interpolada
print(f'o valor somado de {valor_1} + {valor_2} + {valor_3} é: {soma}')
print(f'o valor multiplicado de {valor_1} x {valor_2} x {valor_3} é: {multiplicacao}')