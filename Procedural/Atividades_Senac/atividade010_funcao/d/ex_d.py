# Crie uma função que receba uma temperatura em fahrenheit e retorne o valor em graus célsius.
import os

from modulo_d import farenrait_em_celso
os.system('cls')

farenhait = int(input('Digite a temperatura em farenhait: '))

# invocando função celsius
celsius = farenrait_em_celso(farenhait)

print(f'Os {farenhait} graus em farenhait em celsius ficará {celsius}° graus celsius.')