import os

os.system('cls')


ano = int(input('Digite um ano: '))

if ano % 4 == 0 or ano % 100 != 0:
    print(f'O ano {ano} bissexto')
elif ano <= 0:
    print(f'Ano {ano}? ta tirando né')
else:
    print(f'O ano {ano} não é bissexto')
