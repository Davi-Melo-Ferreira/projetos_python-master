import os
import random

os.system('cls')

for i in range(1, 13):
    funcionarios = [
    "Ana Silva", "João Pereira", "Maria Costa", "Lucas Oliveira", "Beatriz Santos",
    "Felipe Rodrigues", "Juliana Almeida", "Carlos Souza", "Gabriela Martins", "Rafael Carvalho",
    "Mariana Lima", "Pedro Gomes", "Laura Rocha", "Daniel Silva", "Camila Santos",
    "Bruno Costa", "Larissa Pereira", "Samuel Oliveira", "Tânia Ramos", "Igor Carvalho",
    "Renata Alves", "Eduardo Gomes", "Priscila Lima", "Vinícius Rocha", "Letícia Martins"
]
    
    funcionarios1 = funcionarios.copy()
    turno_manha = []
    turno_tarde = []
    turno_noite = []

    for manha in range(1, 9):
        sorteio = random.choice(funcionarios)
        turno_manha.append(sorteio)
        funcionarios.remove(sorteio)

    for tarde in range(1, 10):
        sorteio = random.choice(funcionarios)
        turno_tarde.append(sorteio)
        funcionarios.remove(sorteio)

    for noite in range(1, 9):
        sorteio = random.choice(funcionarios)
        turno_noite.append(sorteio)
        funcionarios.remove(sorteio)

    turno_integral = []
    
    escolha = random.randint(1,2)
    for num in range(1, 3):    
        if escolha == 1:
            turno_integral.append(random.choice(turno_tarde))
            turno_integral.append(random.choice(turno_noite))
        else:
            turno_integral.append(random.choice(turno_manha))
            turno_integral.append(random.choice(turno_tarde))


    print(f'\----- MÊS {i} -----/')
    print('(----- TURNO DA MANHÃ -----)')
    print()
    print(turno_manha)
    print()
    print('(----- TURNO DA TARDE -----)')
    print()
    print(turno_tarde)
    print()
    print('(----- TURNO DA NOITE -----)')
    print()
    print(turno_noite)
    print()
    print('(----- TURNO INTEGRAL -----)')
    print()
    print(turno_integral)
    print()
    print('-'*70)
    print()