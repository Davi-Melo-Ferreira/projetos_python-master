# Evolua o programa anterior para um código que pergunte ao usuário qual o intervalo que ele deseja ver  impresso.
import os


os.system('cls')

intervalo = int(input('Diga um número inteiro para o intervalo: '))
print()

for c in range(0, 50 + 1, intervalo):
    print(c, end=' | ')

print('FIM')