# Crie uma função que receba uma lista de números.
# Depois retorne duas listas com os números pares, os números ímpares,
#a quantidade de números pares e a quantidade de números ímpares.
import os

from modulo_a import verificar_paridade, quantidades


opcao = 's'
lista = []

while opcao == 's':
    os.system('cls')
    
    numero = int(input('Digite um número para uma lista: '))
    lista.append(numero)
    opcao = input('Deseja continuar?(s/n): ').lower()

(lista_par, lista_impar) = verificar_paridade(lista)

qntd_par, qntd_impar = quantidades(lista_par, lista_impar)

os.system('cls')
print(f'Números Ímpares: {lista_impar}')
print(f'Quantidade de Números Ímpares: {qntd_impar}')
print(f'\nQuantidade de Números Pares: {qntd_par}')
print(f'Números Pares: {lista_par}')