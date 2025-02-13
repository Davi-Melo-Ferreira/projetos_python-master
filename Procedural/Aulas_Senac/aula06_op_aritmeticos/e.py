# Biblioteca
import os

# Limpar Terminal
os.system('cls')

# Entrada
valor = int(input('Digite seu valor: '))

# Processo
sucessor = valor + 1
antecessor = valor - 1

# Saída
print(f'O sucessor de {valor} é: {sucessor}')
print(f'e o antecessor de {valor} é: {antecessor}')