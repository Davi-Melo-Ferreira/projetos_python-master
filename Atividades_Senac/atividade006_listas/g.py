# Ler uma lista com 10 números, depois apresente o maior e o menor número da lista
import os


os.system('cls')

ent = (input('Números: '))
numeros_str = ent.split()

numeros = []
for num in numeros_str:
    numeros.append(int(num))
print(numeros)

asc = numeros.sort()
print(f'O menor número da lista é: {numeros[0]}')
numeros.reverse()
print(f'O maior número da lista é: {numeros[0]}')