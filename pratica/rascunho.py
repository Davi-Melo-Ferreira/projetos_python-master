import os


os.system('cls')

# Crie a lista [1, 2, 3, 5, 6] e depois insira o valor que está faltando na posição correta.

lista = [1, 2, 3, 5, 6]
lista.insert(3, 4)
print(lista)
print()

# Crie uma lista com 5 números inteiros. Depois imprima a soma desses valores.
lista = [1, 2, 3, 4, 5]
soma = 0
for i in lista:
    soma += i
print(soma)
print()

#Faça um programa que procure na lista numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15] e produza:
# • O intervalo de 1 até 9
# • O intervalo de 8 até 13
# • Os números pares
# • Os números ímpares
# • Os múltiplos de 2, 3 e 4
# • Lista reversa
# • O produto dos intervalos 5-6 por 11-12

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

print('Intervalo de 1 a 9:')
print(lista[0:9])
print()

print('Intervalo de 8 a 13:')
print(lista[7:13])
print()

print('Números pares:')
print(lista[1:15:2])
print()

print('Números ímpares:')
print(lista[0:15:2])
print()

mult = []
for i in lista:
    if i % 2 == 0 or i % 3 == 0 or i % 4 == 0:
        mult.append(i)
print(mult)

print('Lista reversa:')
print(lista[::-1])
print()

for i in lista[4: 6]:
    for j in lista[10:12]:
        mult = i * j
        print(f'{i} x {j} = {mult}')
# Faça um programa que preencha uma lista com as notas de 4 alunos, depois imprima a média.
