import os
import random

os.system('cls')

# Recomendador de Jogos
# Títulos - Todos os jogos
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
temas = [anime, terror, ficcao_cientifica, fantasia]

# Gêneros
acao = set(["Red Dead Redemption 2", "The Legend of Zelda: Breath of the Wild", "GTA V", "Resident Evil 4"])
rpg = set(["Baldur's Gate 3", "Final Fantasy VII Remake", "Elden Ring", "The Witcher 3: Wild Hunt"])
estrategia = set(["Age of Empires IV", "Civilization VI", "Stellaris"])
aventura = set(["Super Mario Odyssey", "Hollow Knight", "The Legend of Zelda: Breath of the Wild"])
generos = [acao, rpg, estrategia, aventura]

# Desenvolvedores
rockstar_games = set(["Red Dead Redemption 2", "GTA V"])
nintendo = set(["The Legend of Zelda: Breath of the Wild", "Super Mario Odyssey"])
team_cherry = set(["Hollow Knight"])
larian_studios = set(["Baldur's Gate 3"])
capcom = set(["Resident Evil 4", "Monster Hunter World"])
devs = [rockstar_games, nintendo, team_cherry, larian_studios, capcom]

# Séries
red_dead = set(["Red Dead Redemption", "Red Dead Redemption 2"])
legend_of_zelda = set(["Ocarina of Time", "Breath of the Wild", "Tears of the Kingdom"])
baldurs_gate = set(["Baldur's Gate", "Baldur's Gate 2", "Baldur's Gate 3"])
series = [red_dead, legend_of_zelda, baldurs_gate]

categ = [temas, generos, devs, series]

