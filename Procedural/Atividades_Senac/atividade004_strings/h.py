import os


os.system('cls')

nome = input('Diga o nome do aluno: ')
nomem = nome.lower()
quantidade = nomem.count('o')
contar = nomem.find('o')
contar_ultimo = nomem.rfind('o')
#print(f'O nome tem {quantidade} índices')
print(f'A letra "o" aparece {quantidade} vezes')
print(f'O primeiro "o" aparece no índice {contar}')
print(f'O último "o" aparece no índice {contar_ultimo}')