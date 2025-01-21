# Crie uma função que receba uma temperatura em fahrenheit e retorne o valor em graus célsius.
import os


os.system('cls')

# definindo a função rarenfait para celsinhos
def farenrait_celso(farenhait):
    celsinhos = (((farenhait - 32) * 5) / 9)
    return celsinhos

farenhait = int(input('Digite a temperatura em farenhait: '))

# invocando função celsinhos
celsinhos = farenrait_celso(farenhait)

print(f'Os {farenhait} graus em farenhait em celsius ficará {celsinhos:.2f} graus celsius.')