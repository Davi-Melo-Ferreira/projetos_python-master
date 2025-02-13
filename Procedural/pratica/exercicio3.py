import random
import os


os.system('cls')

# Como fazer para entenderem como responder
print('.'*70)
print('Por Favor, Digite as respostas múltiplas separando-as com espaço')
print(
    'Exemplo: Se você precisa digitar três números inteiros, '
    'escreva assim: '
    '1.1 2.2 3.3'
)

entendeu = input('Você Entendeu?: ')

# Transformar entendeu de M para m
entendeum = entendeu.lower()

# Verifica se a pessoa entendeu ou não
if entendeum == 'sim':
    print('Ótimo, vamos começar então!')
else:
    print('Que pena... boa sorte se virando então!')
print('='*70)
print('')

# Entrada de Dados
resposta1 = (input('Diga três nomes: ')).split()
resposta2 = [int(num) for num in input('Diga três números inteiros: ').split()]
resposta3 = [float(num) for num in input('Diga três números não inteiros: ').split()]

# Transformar resposta1 de M para m
resposta1_m = [nome.lower() for nome in resposta1]

resposta1m_aleatorio = random.choice(resposta1)
resposta2_aleatorio = random.choice(resposta2)
resposta3_aleatorio = random.choice(resposta3)

print('.'*70)
print('Agora irei escolher aleatoriamente um número ou nome de cada pergunta')
print('')
print(f'O nome escolhido aleatoriamente foi: {resposta1m_aleatorio}')
print(f'O número inteiro escolhido aleatoriamente foi: {resposta2_aleatorio}')
print(f'O número não inteiro escolhido aleatoriamente foi: {resposta3_aleatorio}')