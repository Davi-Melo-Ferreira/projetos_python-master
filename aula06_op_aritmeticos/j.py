# Biblioteca
import os

# Limpar Terminal
os.system('cls')

#Entrada
base = int(input('Diga a Base do Retângulo: '))
altura = int(input('Diga a Altura do Retângulo: '))

# Processo
perimetro = base * 2 + altura * 2

# Saída
print(f' O Perímetro do Retângulo de base {base} \
e altura {altura} é: {perimetro}') 