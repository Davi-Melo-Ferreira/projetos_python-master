# Importar
import os

# Limpar Terminal
os.system('cls')

print()
print('OPERADORES ARITMÉTICOS')
print()

# Entrada de Dados
print('--- SOMA')
print('-'*70)
parcela_1 = float(input('1ª parcela: '))
parcela_2 = float(input('2ª parcela: '))

print()
print('--- SUBTRAÇÃO')
print('-'*70)
minuendo = float(input('Minuendo: '))
subtraendo = float(input('Subtraindo: '))

print()
print('--- PRODUTO')
print('-'*70)
multiplicando = float(input('Multiplicando: '))
multiplicador = float(input('Multiplicador: '))

print()
print('--- DIVISÃO')
print('-'*70)
dividendo = float(input('dividendo'))
divisor = float(input('divisor: '))

print()
print('--- RAIZ QUADRADA')
print('-'*70)
radicando_quadrado = float(input('Raíz quadrada: '))

print()
print('--- RAIZ CÚBICA')
print('-'*70)
radicando_cubica = float(input('Raíz cúbica: '))

# Procesamento
soma = parcela_1 + parcela_2
diferenca = minuendo - subtraendo
produto = multiplicando * multiplicador
quociente = dividendo / divisor
raiz_quadrada = radicando_quadrado **(1/2)
raiz_cubo = radicando_cubica **(1/3)

# Saída
print('='*70)
print('RESULTADOS')
print('-'*70)
print(f'A soma de {parcela_1} + {parcela_2} é: {soma}')
print(f'A subtração de {minuendo} - {subtraendo} é: {diferenca}')
print(f'A multiplicação de {multiplicando} x {multiplicador} é: {produto}')
print(f'A divisão de {dividendo} ÷ {divisor} é: {quociente}')
print(f'A raiz quadrada de {radicando_quadrado} é: {raiz_quadrada}')
print(f'A raiz cubica de {radicando_cubica} é: {raiz_cubo}')








