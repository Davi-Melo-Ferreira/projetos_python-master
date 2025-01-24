# Crie uma função que receba uma temperatura em fahrenheit e retorne o valor em graus célsius.
import os


os.system('cls')

# definindo a função rarenfait para celsius
def farenrait_em_celso(farenhait):
    celsius = (((farenhait - 32) * 5) / 9)
    return celsius

farenhait = int(input('Digite a temperatura em farenhait: '))

# invocando função celsius
celsius = farenrait_em_celso(farenhait)

print(f'Os {farenhait} graus em farenhait em celsius ficará {celsius:.2f} graus celsius.')