import os

class Livros:
    def __init__(self, titulo, autor, ano_de_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_de_publicacao = ano_de_publicacao
        self.dicionario = {}

    def adicionar_livros(self):
        self.dicionario[len(self.dicionario) + 1] = {
            'Título': self.titulo,
            'Autor': self.autor,
            'Ano de Publicação': self.ano_de_publicacao
            }

    def printar_livros(self):
        for id in cadastro.dicionario.values():
            for chave, valor in id.items():
                print(f'{chave} : {valor}')

# programa Main
run = True
while run:
    titulo = input('Digite o Título do Livro: ')
    autor = input('Digite o Autor do Livro: ')
    ano_de_publicacao = input('Digite o Ano de Publicação do Livro: ')
    
    # criando objeto
    cadastro = Livros(titulo, autor, ano_de_publicacao)
    
    # aplicando método
    cadastro.adicionar_livros()
    
    opcao = input('Deseja continuar? (s/n): ').lower()
    if opcao == 'n':
        run = False
    elif opcao != 's':
        input('INVÁLIDO.... Pressione qualquer tecla para continuar')
    
    run = False

os.system('cls')
cadastro.printar_livros()