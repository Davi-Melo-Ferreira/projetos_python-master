import os
import math

os.system('cls')


radicando = int(input('Diga um valor: '))

if radicando < 0:
    print('O valor será um número complexo.')
else:
    raiz_quadrada = math.sqrt(radicando)
    cima = math.ceil(raiz_quadrada)
    baixo = math.floor(raiz_quadrada)
    if raiz_quadrada == cima == baixo:
    
     print(f'a raiz quadrada de {radicando} é: {raiz_quadrada}')
    else:
     print(f'A raíz de {radicando} arredondado é {cima} ou {baixo}')