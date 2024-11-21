import os


os.system('cls')

lista_numeros = [100, 200]

entrada = input('Digite números separados por espaço: ')

numeros = entrada.split()

pares = []

for numero in numeros:
    
    numero_aux = int(numero)
    
    if numero_aux % 2 == 0:
        
        pares.append(numero_aux)
print('-'*70)
print(f'Lista gerada: {pares}')
print('-'*70)

lista_numeros.extend(pares)

print(f'Números pares adicionados á lista: {lista_numeros}')
