import os


os.system('cls')

valor1 = int(input('Diga um valor: '))
valor2 = int(input('Diga outro valor: '))
valor3 = int(input('Diga mais um valor: '))

if valor1 == valor2 and valor3:
    print(f'Ambos os valores são iguais')
elif valor1 > valor2 and valor2 > valor3:
    print(f'{valor1} é o maior \
e o {valor3} é o menor')
