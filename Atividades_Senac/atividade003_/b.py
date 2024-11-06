import os
import math

os.system('cls')

valor1 = int(input('Diga um valor: '))
valor2 = int(input('Diga outro valor: '))



if valor2 == 0:
    print('Erro')
else:   
    div = valor1 / valor2
    
    if div % 1 == 0:
        print(div)
    else:
        cima = math.ceil(div)
        baixo = math.floor(div)
        print(f'O valor é {cima} ou {baixo}')