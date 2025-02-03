import pygame

pygame.init()

# definindo tamanho de tela
largura, altura = 1000, 600
tela = pygame.display.set_mode((largura, altura))

# Definindo o título da janela
pygame.display.set_caption('Thiago abaitolado...')

rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: # Fecha a tela se clicar no x da janela
            rodando = False