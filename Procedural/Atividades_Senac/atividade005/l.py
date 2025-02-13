#Faça um programa que verifique se o usuário e senha estão inseridos em um banco de dados (fake). O usuário só terá acesso se digitar os dados corretos e, assim, sair do laço.
import os


os.system('cls')

usuario_c = input('Digite seu nome de usuário: ')
senha_c = input('Digite sua senha de usuário: ')

print()
print('faça o login:')
for loop in range(1, 3 + 1):
    usuario = input('Digite seu nome de usuário: ')
    senha = input('Digite sua senha de usuário: ')
    if usuario != usuario_c:
        print('Usuário Inválido')
    elif senha != senha_c:
        print('Usuário Inválido')
    else:
        print('Login realizado com Sucesso!')
        break
        
    