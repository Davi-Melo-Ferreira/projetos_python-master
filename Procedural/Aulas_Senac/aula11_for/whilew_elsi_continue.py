import os


os.system('cls')

print('-'*70)
print('ESTRUTURA DE CINTROLE WHILE ELSE CONTINUE')
print('-'*70)

print()

contador = 0

while (contador <= 10):
    
    contador += 1
    
    if (contador % 2 == 0):
        continue
    print(f'Contador = {contador}')
else:
    print(f'Bloco do while...else: contador em {contador}')
    
print('-'*70)
print('FIM DO PROGRAMA')
print()