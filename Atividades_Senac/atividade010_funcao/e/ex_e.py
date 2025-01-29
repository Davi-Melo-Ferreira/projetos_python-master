# Crie uma função que receba a altura e peso de uma pessoa.
# Depois retorne o seu IMC.
import os

from modulo_e import calcular_imc
os.system('cls')

# Entrada
altura = float(input('Digite sua altura: '))
peso = float(input('Digite o seu peso: '))

# Invocação da função
imc = calcular_imc(altura, peso)

# Saída interpretada
print(f'Seu Índice de Massa Corporal é: {imc:.2f}')