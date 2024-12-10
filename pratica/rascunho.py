import os


os.system('cls')

meu_dicionario = {'azul':'1','amarelo':'2','rosa':'3','roxo':'12'}
dicionario = list(meu_dicionario.copy())

alph = 'abcdefghijklmnopqrstuvwxyz'

for char in alph:
        num = 0
        for elemento in dicionario:
            if char in elemento[0]:
                num += 1
        if num == 0:
            continue
        else:
            print(char, '=', num)