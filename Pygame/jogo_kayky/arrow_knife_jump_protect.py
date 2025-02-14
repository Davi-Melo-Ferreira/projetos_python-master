import os
import pygame

altura, largura = 600, 1000

tela = pygame.display.set_mode((largura, altura))

run = True
while run:
    tela.fill((0, 0, 0))
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            run = False

os.system('cls')
pygame.quit()
