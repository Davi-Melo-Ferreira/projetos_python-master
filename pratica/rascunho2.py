import os
import random

os.system('cls')

funcionarios = [
    "Ana Silva", "João Pereira", "Maria Costa", "Lucas Oliveira", "Beatriz Santos",
    "Felipe Rodrigues", "Juliana Almeida", "Carlos Souza", "Gabriela Martins", "Rafael Carvalho",
    "Mariana Lima", "Pedro Gomes", "Laura Rocha", "Daniel Silva", "Camila Santos",
    "Bruno Costa", "Larissa Pereira", "Samuel Oliveira", "Tânia Ramos", "Igor Carvalho",
    "Renata Alves", "Eduardo Gomes", "Priscila Lima", "Vinícius Rocha", "Letícia Martins"
]

funcionarios1 = funcionarios.copy()

turno_vazio = []
turno_manha = []
turno_tarde = []
turno_noite = []
turnos = [turno_manha, turno_tarde, turno_noite]

for manha in range(0, 8):
    sorteio = random.choice(funcionarios)
    turno_manha.append(sorteio)
    funcionarios.remove(sorteio)
print('turno manhã:', turno_manha)
print()


for tarde in range(0, 9):
    sorteio = random.choice(funcionarios)
    turno_tarde.append(sorteio)
    funcionarios.remove(sorteio)
print('turno tarde:', turno_tarde)
print()

for noite in range(0, 8):
    sorteio = random.choice(funcionarios)
    turno_noite.append(sorteio)
    funcionarios.remove(sorteio)
print('turno noite:', turno_noite)
print()

turno_integral = []
for i in range(0, 2):
    turno_integral.append(random.choice(turno_noite))
    turno_integral.append(random.choice(turno_tarde))
print('turno integral:', turno_integral)
print()

for i in range(1, 13):
    print(f'MÊS {i}')
    turno_noite.insert(0, turno_vazio)
    turno_tarde.insert(0, turno_noite)
    turno_manha.insert(0, turno_tarde)
    turno_vazio.insert(0, turno_manha)
    print('-'*70)