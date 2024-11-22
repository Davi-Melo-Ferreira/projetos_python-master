import os


os.system('cls')

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

for i in lista:
    if i % 2 == 0:
        if i % 3 == 0:
            if i % 4 == 0:
                print(i)