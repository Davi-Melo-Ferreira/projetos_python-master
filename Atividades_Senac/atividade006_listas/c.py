# Faça um programa que procure na lista numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15] e produza:
# • O intervalo de 1 até 9
# • O intervalo de 8 até 13
# • Os números pares
# • Os números ímpares
# • Os múltiplos de 2, 3 e 4
# • Lista reversa
# • O produto dos intervalos 5-6 por 11-12
import os


os.system('cls')

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# • O intervalo de 1 até 9
print(lista[0:9])

# • O intervalo de 8 até 13
print(lista[8:13])

# • Os números pares
print(lista[2:15:2])

# • Os números ímpares
print(lista[1:15:2])




# • Lista reversa
print(lista[::-1])