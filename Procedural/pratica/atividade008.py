import os
import random


os.system('cls')

# Recomendador de Jogos
# Títulos - Todos os jogos
titulos = set([
    "Red Dead Redemption 2", "The Legend of Zelda: Breath of the Wild", "Hollow Knight", 
    "Dark Souls III", "Baldur's Gate 3", "Resident Evil 4", "Elden Ring", "Cyberpunk 2077", 
    "The Witcher 3: Wild Hunt", "Final Fantasy VII Remake", "GTA V", "Dragon Ball Z: Kakarot",
    "Silent Hill 2", "No Man's Sky", "Mass Effect", "Stellaris", "Age of Empires IV",
    "Super Mario Odyssey", "Monster Hunter World"
])

# Temas
anime = set(["Dragon Ball Z: Kakarot", "Naruto Shippuden: Ultimate Ninja Storm 4"])
terror = set(["Resident Evil 4", "Silent Hill 2", "Dead Space"])
ficcao_cientifica = set(["Cyberpunk 2077", "Mass Effect", "No Man's Sky"])
fantasia = set(["The Witcher 3: Wild Hunt", "Elden Ring", "Baldur's Gate 3"])

# Gêneros
acao = set(["Red Dead Redemption 2", "The Legend of Zelda: Breath of the Wild", "GTA V", "Resident Evil 4"])
rpg = set(["Baldur's Gate 3", "Final Fantasy VII Remake", "Elden Ring", "The Witcher 3: Wild Hunt"])
estrategia = set(["Age of Empires IV", "Civilization VI", "Stellaris"])
aventura = set(["Super Mario Odyssey", "Hollow Knight", "The Legend of Zelda: Breath of the Wild"])

# Desenvolvedores
rockstar_games = set(["Red Dead Redemption 2", "GTA V"])
nintendo = set(["The Legend of Zelda: Breath of the Wild", "Super Mario Odyssey"])
capcom = set(["Resident Evil 4", "Monster Hunter World"])

# Séries
red_dead = set(["Red Dead Redemption", "Red Dead Redemption 2"])
legend_of_zelda = set(["Ocarina of Time", "Breath of the Wild", "Tears of the Kingdom"])
baldurs_gate = set(["Baldur's Gate", "Baldur's Gate 2", "Baldur's Gate 3"])

# Conjunto
temas = [anime, terror, ficcao_cientifica, fantasia]
generos = [acao, rpg, estrategia, aventura]
devs = [rockstar_games, nintendo, capcom]
series = [red_dead, legend_of_zelda, baldurs_gate]
conjunto_total = [temas, generos, devs, series]

# Notas de 1 a 5
one = set([])
two = set([])
thr = set([])
fou = set([])
fiv = set([])
notas = [one, two, thr, fou, fiv]
jogos_recomendados = set([])

while True:
    print('Avaliar jogo(1)\n'
        'Remover um Jogo(2)\n'
        'Sair(s)'
    )
    escolha = input('O que você quer fazer?: ').lower()
    if escolha == '1':
        titulo_alt = random.choice(list(titulos))
        print('\nJogo:', titulo_alt)
        nota = int(input('Nota(1-5): '))
        if nota == 1:
            one.add(titulo_alt)
            titulos.discard(titulo_alt)
        elif nota == 2:
            two.add(titulo_alt)
            titulos.discard(titulo_alt)
        elif nota == 3:
            thr.add(titulo_alt)
            titulos.discard(titulo_alt)
        elif nota == 4:
            fou.add(titulo_alt)
            titulos.discard(titulo_alt)
        elif nota == 5:
            fiv.add(titulo_alt)
            titulos.discard(titulo_alt)
        print()
    elif escolha == '2':
        print()
        remover = input('Qual Jogo você quer remover de Notas?: ')
        for cat in notas:
            if remover in cat:
                jogo_removido = cat.discard(remover)
        if remover not in cat:
            print('Jogo foi Removido ou Não Encontrado!\n')
    elif escolha == 's':
        break
    else:
        print('Inválido!\n')

print(f'Seus jogos Favoritos Baseado em sua Avaliação\n'
      f'Nota 1: {list(one)}\n'
      f'Nota 2: {list(two)}\n'
      f'Nota 3: {list(thr)}\n'
      f'Nota 4: {list(fou)}\n'
      f'Nota 5: {list(fiv)}\n'
      )

print('-'*70)
print()

recomendar = set([])

for ind_5 in fiv:
    for ind in conjunto_total:
        for categoria in ind:
            for tit in categoria:
                if ind_5 in categoria:
                    jogos_recomendados.add(tit)
                elif ind_5 in jogos_recomendados:
                    jogos_recomendados.discard(ind_5)

print(f"Recomendações baseadas nos seus jogos favoritos: {fiv}")
print(jogos_recomendados)
print()