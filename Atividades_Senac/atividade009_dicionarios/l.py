
# lista com:
#titulo
#genero
#duração
#classificação indicativa

#adicionar
#remover
#alterar informações
#gerar relatório

#listar os filmes ordenados por título, e gerar um relatório que indique quantos filmes têm duração superior a 2 horas e quantos tem classificação indicativa 'Livre'.
import os

filmes = {}
while True:
    os.system('cls')
    print("\nMenu de Opções:")
    print("1. Cadastrar um novo filme")
    print("2. Alterar um filme")
    print("3. Remover um filme")
    print("4. Gerar relatório")


    opcao = input("\nEscolha uma opção (1, 2, 3, 4): ")

    if opcao == '1':
        id_novo = len(filmes) + 1
        titulo = input('Digite o Título do filme: ')
        nome = input('Digite o nome do filme: ')
    if opcao == '2':

    if opcao == '3':

    if opcao == '4':
