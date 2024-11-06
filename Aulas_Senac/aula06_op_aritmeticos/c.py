# Biblioteca
import os

# Limpar Terminal
os.system('cls')

# Entrada
aluno = input('Diga o nome do aluno: ')
portugues = float(input('Nota de Português: '))
matematica = float(input('Nota de Matemática: '))
ciencias = float(input('Nota de Ciências: '))
historia = float(input('Noa de Histórias: '))

# Processamento
media = (portugues + matematica + ciencias + historia) / 4

# Saída
print(f'O aluno {aluno} tem uma média de {media}')