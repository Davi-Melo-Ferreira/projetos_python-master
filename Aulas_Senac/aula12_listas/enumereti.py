import os

os.system('cls')

print('-' * 70)
print('SAÍDA COM FOR... ENUMERATE()')
print('-' * 70)

soma = 0

# Criando uma lista
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Percorrendo a lista com o enumerate()
# O comando enumerate adiciona um índice para cada valor de nossa lista
# Start opcional, para não começar no índice 0
# enumerate(listaNumeros, start = 1)
for indice, numero in enumerate(lista_numeros):
    soma += numero  # soma os números
    print(f'Indice: {indice} = Número: {numero}')

print('-' * 70)
print(f'A soma de todos os números é: {soma}')
print('Fim do programa!')
print('-' * 70)
