import os


os.system('cls')

print('-'*70)
print('ESTRUTURA DE DADOS: LISTAS [ ]')
print('='*70)

lista_inteiros = [1, 2, 3, 4]
lista_vogais = ['a', 'e', 'i', 'o', 'u']
lista_nomes = ['John', 'Jane', 'Carol']
lista_heterogenea = ['John', 80, 1.90, 'AB']
lista_dentro_lista = [['a', 'e', 'i', 'o', 'u'], ['a', 'e', 'i', 'o', 'u']]

print(f'Lista de números: {lista_inteiros}')
print(f'Lista de vogais: {lista_vogais}')
print(f'Lista de nomes: {lista_nomes}')
print(f'Lista misturada: {lista_heterogenea}')
print(f'Lista de lista: {lista_dentro_lista}')

lista_num_indice0 = lista_inteiros[0]
lista_vogais_indice1 = lista_vogais[1]
lista_nomes_indice2 = lista_nomes[2]
lista_heterogenea_indice3 = lista_heterogenea[3]
lista_num_indice1 = lista_dentro_lista[1]

print('-'*70)
print('Acessando os elementos de uma lista')
print('='*70)
print(f'Lista de números: {lista_num_indice0}')
print(f'Lista de vogais: {lista_vogais_indice1}')
print(f'Lista de nomes: {lista_nomes_indice2}')
print(f'Lista misturada: {lista_heterogenea_indice3}')
print(f'Lista de lista: {lista_num_indice1}')

print('-'*70)
print('Fim do programa!')
print('='*70)