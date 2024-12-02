import os
import random

os.system('cls')

titulos = set([
    "Red Dead Redemption 2", "The Legend of Zelda: Breath of the Wild", "Hollow Knight", 
    "Dark Souls III", "Baldur's Gate 3", "Resident Evil 4", "Elden Ring", "Cyberpunk 2077", 
    "The Witcher 3: Wild Hunt", "Final Fantasy VII Remake", "GTA V", "Dragon Ball Z: Kakarot",
    "Silent Hill 2", "No Man's Sky", "Mass Effect", "Stellaris", "Age of Empires IV",
    "Super Mario Odyssey", "Monster Hunter World"
])


# Listas para Notas
one = set()
two = set()
thr = set()
fou = set()
fiv = set()

while True:
    print('Avaliar jogo(1)\n'
        'Sair(s)'
    )
    escolha = (input('O que você quer fazer? (1-s): '))
    if escolha == '1':
        titulo_alt = random.choice(list(titulos))
        print('\nJogo:', titulo_alt)
        nota = int(input('Nota(1-5): '))
        if nota == 1:
            one.add(titulo_alt)
            titulos.remove(titulo_alt)
        elif nota == 2:
            two.add(titulo_alt)
            titulos.remove(titulo_alt)
        elif nota == 3:
            thr.add(titulo_alt)
            titulos.remove(titulo_alt)
        elif nota == 4:
            fou.add(titulo_alt)
            titulos.remove(titulo_alt)
        elif nota == 5:
            fiv.add(titulo_alt)
            titulos.remove(titulo_alt)
        print()

    if escolha == 's':
        break
print(f'Seus jogos Favoritos Baseado em sua Avaliação\n'
      f'Nota 1: {list(one)}\n'
      f'Nota 2: {list(two)}\n'
      f'Nota 3: {list(thr)}\n'
      f'Nota 4: {list(fou)}\n'
      f'Nota 5: {list(fiv)}\n'
      )

print('-'*70)
print()

for categoria in tema:
    if favorito in categoria:
        print('yes')
        break