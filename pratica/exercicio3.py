import os


os.system('cls')

dist = float(input('Diga a distância da viagem em km: '))
vel = float(input('Diga a velocidade média do veículo: '))

if vel > 100:
    valor = dist * 0.75
else:
    valor = dist * 0.50

print(f'O valor da viagem é de: R${valor}')