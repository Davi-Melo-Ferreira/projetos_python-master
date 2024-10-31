import os


os.system('cls')

custo = int(input('Qual o Custo da Compra?: '))
client_age = int(input('Qual a Idade do Cliente?: '))

if client_age > 60:
    desconto = custo * 0.15
elif client_age <= 60 and client_age >= 18 and custo > 200:
    desconto = custo * 0.10
else:
    desconto = custo * 0.05
valor_final = custo - desconto 

print(f'O valor com o desconto de {desconto} é: {valor_final}')