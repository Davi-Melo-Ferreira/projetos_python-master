# Faça um programa que procure na lista numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15] e produza:
import os


os.system('cls')

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# • O intervalo de 1 até 9
print('O intervalo de 1 até 9:')
print(lista[0:9])
print('-'*70)
print()

# • O intervalo de 8 até 13
print('O intervalo de 8 até 13:')
print(lista[7:13])
print('-'*70)
print()

# • Os números pares
print('Os números pares:')
print(lista[2:15:2])
print('-'*70)
print()

# • Os números ímpares
print('Os números ímpares:')
print(lista[1:15:2])
print('-'*70)
print()

# • Os múltiplos de 2, 3 e 4
print('Os múltiplos de 2, 3 e 4:')
for i in lista:
    if i % 2 == 0 and i % 3 == 0 and i % 4 == 0:
        print(i)
print()

# • Lista reversa
print('Lista reversa:')
print(lista[::-1])
print('-'*70)
print()

# • O produto dos intervalos 5-6 por 11-12
print('O produto dos intervalos 5-6 por 11-12:')
print()
for i in lista[4:6]:
    for j in lista[10:12]:
        mult = i * j
        print(f'{i}x{j} = {mult}', end=' ')
    print('\n')