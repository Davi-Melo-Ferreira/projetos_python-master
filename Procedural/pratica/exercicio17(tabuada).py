import os


os.system('cls')

for i in range(1, 11):
    for j in range(1, 11):
        mult = i * j
        if 1 == j:
            print('\n')
        print(f'{i} x {j} = {mult}', end=' | ')
    print()
print('\n')