# Faça um algoritmo que imprima a frase "estou em looping" e, em seguida, solicite ao usuário digitar uma letra.
# Caso a letra seja o “f" finalize a aplicação. Do contrário, imprima novamente a mesma frase até que o caractere “f" seja digitado.
import os


os.system('cls')

for c in range(1, 100):
    frase = print('Estou em Looping')
    pergunta = (input('Digite uma letra[f-finalizar]: ')).lower()
    
    if pergunta == 'f':
        print('Loop terminou!')
        break
    