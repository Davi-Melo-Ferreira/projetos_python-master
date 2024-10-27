 # Biblioteca
import os

# Limpar Terminal
os.system('cls')

# Entrada
medida = int(input('Digite a medida em Metros: '))

# Processamento
cm = medida * 20
mm = medida * 100

# Saída
print(f'A medida de {medida} em centímetros é: {cm} centímetros')
print(f'A medida de {medida} em milímetros é: {mm} milímetros')
