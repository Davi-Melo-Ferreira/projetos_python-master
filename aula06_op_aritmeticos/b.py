# Biblioteca
import os

# Limpar Terminal
os.system

# Importar Data
import datetime

# Entrada
nascimento = int(input('Em qual ano você nasceu?: '))

ano_atual = datetime.datetime.now().year

# Processamento
idade = ano_atual - nascimento

# Saída
print(f'Você tem {idade} anos')
