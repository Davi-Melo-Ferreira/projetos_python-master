# Faça um programa que sorteia os números da Mega Sena e da Lotofácil
import os
import random

os.system('cls')

#mega-sena = 6, loto fácil = 15

print('(----- MEGA-SENA -----)')
listam = []
for i in range(1, 7):
    listam.append(random.randint(1, 101))

print('Números escolhidos:')
print(listam)
print()

print('(----- LOTO-FÁCIL -----)')
lista_loto = []
for j in range(1, 16):
    lista_loto.append(random.randint(1, 101))

print('Números escolhidos:')
print(lista_loto)
print()