import os


os.system('cls')

distancia = int(input('Diga a distância da viagem em km: '))

if distancia <= 200:
    imposto = distancia * 0.70
    print(f'O valor da passagem é de ${imposto}')
else:
    imposto = distancia * 0.40
    print(f'O valor da passagem é de ${imposto}')
    