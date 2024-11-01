import random
import os


os.system('cls')

print('-'*70)
print('Biblioteca random')
print('='*70)

print('Número aleatório')
numero_aleatorio = random.random()
print(f'O número gerado foi: {numero_aleatorio}')
print('.'*70)

print('Número aleatório inteiro')
aleatorio_inteiro = random.randint(1, 20)
print(f'O número inteiro gerado foi: {aleatorio_inteiro}')
print('.'*70)

print('Número aleatório decimal no intervalo')
aleatorio_decimal = random.uniform(1, 10)
print(f'O número decimal gerado foi: {aleatorio_decimal}')
print('.'*70)

print('Sorteio em uma lista')
lista = ['Ágata', 'Coly', 'Isis', 'Bia']
nome_sorteado = random.choice(lista)
print(f'Lista: {lista}')
print(f'O nome escolhido foi: {nome_sorteado}')
print('.'*70)