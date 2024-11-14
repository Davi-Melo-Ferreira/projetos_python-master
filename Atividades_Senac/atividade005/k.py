# Crie um programa que pede que o usuário digite um nome ou uma frase, verifique se esse conteúdo digitado é um palíndromo ou não, exibindo em tela esse resultado.
import os


os.system('cls')

for c in range(1, 100):
    palavra = input('Diga uma frase/palavra: ').lower().replace(' ','')
    if palavra[::-1] == palavra:
        print(f'A {palavra =} é um palíndromo')
        break
    else:
        print(f'A {palavra =} não é um palíndromo')
print('FIM')