# Importar Biblioteca
import os


# Limpar Terminal
os.system('cls')

# Variáveis
a = float(1)
b = float(-6)
c = float(5)

# Processamento
delta = (b ** 2) - (4 * a * c)
baskara1 = (-b - (delta ** (1/2))) / (2 * a)
baskara2 = (-b + (delta ** (1/2))) / (2 * a)

# Saída
print(f'O resultado é {baskara1} e {baskara2}.')