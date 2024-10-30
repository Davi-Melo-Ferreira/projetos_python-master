import os


os.system('cls')

a = float(input('Digite o 1° segmento: '))
b = float(input('Digite o 2° segmento: '))
c =  float(input('Digite o 3° segmento: '))

if a + b > c and a + c > b and b + c > a:
    print('É possível fazer um triângulo')
else:
    print('Não é possível')