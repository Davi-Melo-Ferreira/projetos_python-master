import os

os.system('cls')

titulos = set(['gta', 'gta5', 'hollow kight', 'silksong'])

rockstar_games = set(['gta','gta5'])
teamcherry = set(['hollow knight', 'silksong'])
tema = [rockstar_games, teamcherry]
favorito = 'hollow knight'

cat = [rockstar_games, teamcherry, tema]

for categoria1 in cat:
    for categoria in categoria1:
        if favorito in categoria:
            print('yes')
            break