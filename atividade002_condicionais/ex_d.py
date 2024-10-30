import os


os.system('cls')

salario_atual = float(input('Diga seu Salário Atual: '))

salario_novo1 = salario_atual * 0.05 + salario_atual
salario_novo2 = salario_atual * 0.10 + salario_atual

if salario_atual >= 1500:
    print(f'Seu novo salário com 5% de aumento é: {salario_novo1}')
elif salario_atual <= 0:
    print('Arrumar um trampo tu n quer né')
else: 
    print(f'Seu novo salário com 10% de aumento é: {salario_novo2}')

