import os


os.system('cls')

print('-'*70)
print('ESTRUTURA DE DADOS: LISTAS [ ]')
print('='*70)

lista_mista = ['a', 'b,', 3, 'John', 'e', 500, 'g', 'h']

lista_fatiada1 = lista_mista[0]
lista_fatiada2 = lista_mista[0:]
lista_fatiada3 = lista_mista[0:7]
lista_fatiada4 = lista_mista[0:7:2]
lista_fatiada5 = lista_mista[::-1]

print(f'Fatiando uma Lista: {lista_fatiada1}\n')
print(f'Fatiando uma Lista: {lista_fatiada2}\n')
print(f'Fatiando uma Lista: {lista_fatiada3}\n')
print(f'Fatiando uma Lista: {lista_fatiada4}\n')
print(f'Fatiando uma Lista: {lista_fatiada5}')

print('-'*70)
print('Fim do programa')
print('='*70)
