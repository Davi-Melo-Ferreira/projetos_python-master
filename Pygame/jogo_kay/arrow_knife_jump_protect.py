import os
import pygame

altura, largura = 600, 1000

tela = pygame.display.set_mode((largura, altura))

branco = (255, 255, 255)

run = True
while run:
    tela.fill((0, 0, 0))
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            run = False

    pygame.draw.rect(tela, (250, 250, 250), (500, 300, 30, 30))
    pygame.display.flip()
os.system('cls')
pygame.quit()
