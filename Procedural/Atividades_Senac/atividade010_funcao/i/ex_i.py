# Faça um programa de perguntas e respostas sobre os estados e capitais brasileiras.
# O programa deverá exibir para o usuário o estado e perguntar qual a sua capital.
# Se o usuário errar a resposta, o programa será finalizado apresentando quantas perguntas estão corretas. 
import os
import random
from modulo_i import exibir_reultado, randomizar
os.system('cls')

# Lista de estados do Brasil
estados_capitais = {
    'Acre': 'Rio Branco',
    'Alagoas': 'Maceió',
    'Amapá': 'Macapá',
    'Amazonas': 'Manaus',
    'Bahia': 'Salvador',
    'Ceará': 'Fortaleza',
    'Espírito Santo': 'Vitória',
    'Goiás': 'Goiânia',
    'Maranhão': 'São Luís',
    'Mato Grosso': 'Cuiabá',
    'Mato Grosso do Sul': 'Campo Grande',
    'Minas Gerais': 'Belo Horizonte',
    'Pará': 'Belém',
    'Paraíba': 'João Pessoa',
    'Paraná': 'Curitiba',
    'Pernambuco': 'Recife',
    'Piauí': 'Teresina',
    'Rio de Janeiro': 'Rio de Janeiro',
    'Rio Grande do Norte': 'Natal',
    'Rio Grande do Sul': 'Porto Alegre',
    'Rondônia': 'Porto Velho',
    'Roraima': 'Boa Vista',
    'Santa Catarina': 'Florianópolis',
    'São Paulo': 'São Paulo',
    'Sergipe': 'Aracaju',
    'Tocantins': 'Palmas'
}

invicto = True
while invicto == True:
    acertos = 0

    estado_capital = randomizar(estados_capitais) #umpacking
    
    for chave, valor in estado_capital.items(): # varredura ou iteração
        pergunta = input(f'Qual a capital de {chave}?: ').lower()
        if pergunta == valor.lower():
            acertos += 1
            print('Parabés, Você acertou!!')
            input('Pressione qualquer tecla para a próxima pergunta...')
            os.system('cls')
        else:
            print('Você Errou!!!')
            input('Pressione qualquer tecla para sair...')
            os.system('cls')
            break # vai finalizar a iteração ou varredura
    invicto = False # irá finalizar o while

qntd_perguntas = len(estado_capital) # atribuir o número de estados presentes no dicionário

if acertos == qntd_perguntas:
    print('Parabéns, Você venceu!!!')
else:
    print('Mais sorte da próxima vez...')

resultado = exibir_reultado(acertos, qntd_perguntas) # invocando a função