# Crie uma função que receba uma lista de números.
# Depois retorne duas listas com os números pares, os números ímpares,
#a quantidade de números pares e a quantidade de números ímpares.
import os


def parimpar(lista):
    
    lista_par = []
    lista_impar = []
    for i in lista:
        if i % 2 == 0:
            lista_par.append(i)
        else:
            lista_impar.append(i)
    return lista_par, lista_impar

opcao = 's'
lista = []

while opcao == 's':
    os.system('cls')
    
    numero = int(input('Digite um número para uma lista: '))
    lista.append(numero)
    opcao = input('Deseja continuar?(s/n): ').lower()

(lista_par, lista_impar) = parimpar(lista)

os.system('cls')
print(f'Números Ímpares: {lista_impar}')
print(f'Quantidade de Números Ímpares: {len(lista_impar)}')
print(f'\nQuantidade de Números Pares: {len(lista_par)}')
print(f'Números Pares: {lista_par}')