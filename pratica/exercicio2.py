import os


os.system('cls')

ano = int(input('A quantos anos você trabalha na empresa?: '))
salario = int(input('Quanto você recebe?: '))

if ano >= 3 and ano <= 5:
    bonus = salario * 0.10
elif ano > 5:
    bonus = salario * 0.15
else:
    bonus = salario * 0.05

valor_total = bonus + salario

print(f'Por trabalhar na empresa por {ano} anos, \
seu aumento será de: ${bonus} reais,\
 o que lhe garante um salário de ${valor_total}')