# Importar Biblioteca
import os 

# Limpar Terminal
os.system('cls')

a = 10
b = 5
c = 'José'
d = 'José'

print('-'*70)
print('Condicionais: Operadores Relacionais')
print('-'*70)

# Igualdade (==)

if c == d:
    print('-'*70)
    print(f'{c} é igual a {d}')
    print('-'*70)
else:
    print(f'{c} não é igual a {d}')

# Diferença (!=)
if a != c:
    print('-'*70)
    print(f'{a} é diferente de {c}')
    print('='*70)
else:
    print(f'{a} não é diferente de {c}')

# Maior que (>)
if a > b:
    print('-'*70)
    print(f'{a} é maior que {b}')
    print('='*70)
else:
    print(f'{a} não é maior que {b}')

# Menor que (<)
if a < b:
    print('-'*70)
    print('')
    print('='*70)
else:
    print(f'{a} não é menor que {b}')

# Maior ou igual a (>)
if a >= b:
    print('-'*70)
    print(f'{a} é maior ou igual a {b}')
    print('='*70)
else:
    print(f'{a} não é maior ou igual a {b}')

# Menor ou igual a (<)
if b <= a:
    print('-'*70)
    print(f'{b} é menor ou igual a {a}')
    print('='*70)
else:
    print(f'{b} não é menor ou igual a {a}')

print('Fim do programa')
print('='*70)
print('')