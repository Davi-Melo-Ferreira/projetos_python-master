import os
import random

os.system('cls')

import random

# Pac-man pega ou não o power-up
power = input('Pac-man deve pegar o power-up?: ')
resposta = power.lower()

if resposta == 'sim':
    morte = random.randint(1, 2)
    if morte == 1:
        print('Você conseguiu pegar o Power-up!')
    else:
        print('.' * 70)
        print('Você morreu!')
        exit()  # Para o programa imediatamente
    
    # Pac-man tenta comer o fantasma
    eat = input('Pac-man deve tentar comer o fantasma?: ')
    eatm = eat.lower()
    if eatm == 'sim':
        durar_efeito = random.randint(1, 2)
        if durar_efeito == 1:
            print('Você Matou o Fantasma!')
            print('.' * 70)
            print('PARABÉNS, VOCÊ VENCEU!!')
        else:
            print('O efeito passou antes de você comer o fantasma!')
            print('*' * 70)
            
            # Pac-man tenta fugir
            pergunta = input('Correr pela sua vida?: ')
            perguntam = pergunta.lower()
            if perguntam == 'sim':
                morte = random.randint(1, 2)
                if morte == 1:
                    print('Você conseguiu fugir do fantasma')
                    print('PARABÉNS, VOCÊ VENCEU!!')
                else:
                    print('Você morreu')
                    exit()  # Para o programa imediatamente caso Pac-man morra
