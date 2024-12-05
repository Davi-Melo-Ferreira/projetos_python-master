import os

os.system('cls')

loja1 = set(['arroz', 'feijão', 'açúcar', 'óleo'])
loja2 =  set(['açúcar', 'óleo', 'farinha', 'macarrão'])
inter = loja1 & loja2
i = 0

print('Produtos que são vendidos nas duas lojas:')
for char in inter:
    i += 1
    print(f'{i}º:', char)