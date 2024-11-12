import os


os.system('cls')

print('-'*70)
print('ESTRUTURA DE CONTROLE WHILE ELSE')
print('='*70)
print()

print()

contador = 1

while contador < 7:
    print('Contador é:', contador)
    contador += 1
    
    if contador == 4:
        print(f'Contador chegou em {contador}. Break no While!')
    break

else:
    print('While Finalizado')
    print()