import os

os.system('cls')

resposta = input('Namora comigo?: ')
respostam = resposta.lower()

if respostam == 'sim' or respostam == 's':
    print('Obrigado')
elif respostam == 'não' or respostam == 'nao' or respostam == 'n':
    print('AVATETOMANOCU')