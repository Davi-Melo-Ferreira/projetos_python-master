import os


os.system('cls')

a = int(input('Diga um valor: '))
b = int(input('Diga outro valor: '))
c = int(input('Diga mais um valor: '))

if a == b == c:
    print(f'Todos possuem o mesmo valor')
else:
    if a > b and a > c: # Processamento (Condicional Maior que)
        print(f' O valor {a} é o maior')
    elif b > c:
        print(f' O valor {b} é o maior')
    else:
        print(f' O valor {c} é o maior')

    if a < b and a < c: # Processamento (Condicional Menor que)
        print(f' O valor {a} é o menor')
    elif b < c:
        print(f' O valor {b} é o menor')
    else:
        print(f' O valor {c} é o menor')