# Faça um programa que sorteia os números da Mega Sena e da Lotofácil
import os
import random

os.system('cls')

#mega-sena = 6, loto fácil = 15

print('(----- MEGA-SENA -----)')
lista_megasena = []
for i in range(1, 7):
    lista_megasena.append(random.randint(1, 101))

print('Números escolhidos:')
print(lista_megasena)
print()

print('(----- LOTO-FÁCIL -----)')
lista_loto = []
for j in range(1, 16):
    lista_loto.append(random.randint(1, 101))

print('Números escolhidos:')
print(lista_loto)
print()