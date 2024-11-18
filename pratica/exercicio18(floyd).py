import os 


os.system('cls')

cont = 0
for i in range(1, 5):
    for j in range(i):
        cont += 1
        print(cont, end=" ")
    print()