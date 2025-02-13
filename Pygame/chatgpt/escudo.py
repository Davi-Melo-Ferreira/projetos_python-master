# import pygame
# import math
# from pygame.locals import *

# pygame.init()

# # Definições da tela
# largura, altura = 1000, 600
# tela = pygame.display.set_mode((largura, altura))
# pygame.display.set_caption('Projeto_Teste')

# # Definições do player (quadrado)
# x, y = 400, 250
# velocidade = 5
# tamanho = 50

# clock = pygame.time.Clock()

# rodando = True
# while rodando:
#     tela.fill((0, 0, 0))
    
#     for evento in pygame.event.get():
#         if evento.type == pygame.QUIT:  # Fecha a tela se clicar no X da janela
#             rodando = False
    
#     # Movimento do player
#     teclas = pygame.key.get_pressed()
#     if teclas[pygame.K_a]:
#         x -= velocidade
#     if teclas[pygame.K_d]:
#         x += velocidade
#     if teclas[pygame.K_w]:
#         y -= velocidade
#     if teclas[pygame.K_s]:
#         y += velocidade
    
#     # Pega posição do mouse
#     mouse_x, mouse_y = pygame.mouse.get_pos()
    
#     # Calcula a direção do mouse em relação ao player
#     angulo = math.atan2(mouse_y - y, mouse_x - x)
    
#     # Define a distância do objeto grudado ao player
#     distancia = 40  # Ajuste conforme necessário

#     # Calcula a posição do objeto grudado
#     obj_x = x + tamanho // 2 + distancia * math.cos(angulo)
#     obj_y = y + tamanho // 2 + distancia * math.sin(angulo)

#     # Desenha o player (quadrado)
#     pygame.draw.rect(tela, (0, 250, 0), (x, y, tamanho, tamanho))

#     # Desenha o objeto grudado (círculo)
#     pygame.draw.circle(tela, (250, 0, 0), (int(obj_x), int(obj_y)), 10)

#     pygame.display.update()
#     clock.tick(60)  # Limita a 60 FPS

# pygame.quit()

import pygame
import math
from pygame.locals import *

pygame.init()

# Definições da tela
largura, altura = 1000, 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Projeto_Teste')

# Definições do player (quadrado)
x, y = 400, 250
velocidade = 5
tamanho = 50

clock = pygame.time.Clock()

rodando = True
while rodando:
    tela.fill((0, 0, 0))
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:  # Fecha a tela se clicar no X da janela
            rodando = False
    
    # Movimento do player
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_a]:
        x -= velocidade
    if teclas[pygame.K_d]:
        x += velocidade
    if teclas[pygame.K_w]:
        y -= velocidade
    if teclas[pygame.K_s]:
        y += velocidade
    
    # Pega posição do mouse
    mouse_x, mouse_y = pygame.mouse.get_pos()
    
    # Calcula a direção do mouse em relação ao player
    angulo = math.atan2(mouse_y - y, mouse_x - x)
    
    # Define a distância do objeto grudado ao player
    distancia = 50  # Ajuste conforme necessário.

    # Calcula a posição do objeto grudado
    obj_x = x + tamanho // 2 + distancia * math.cos(angulo)
    obj_y = y + tamanho // 2 + distancia * math.sin(angulo)

    # Calcula o ângulo em graus para rotacionar o retângulo
    angulo_graus = math.degrees(angulo)

    # Desenha o player (quadrado)
    pygame.draw.rect(tela, (0, 250, 0), (x, y, tamanho, tamanho))

    # Desenha o retângulo com rotação
    # O retângulo terá 20x50 de tamanho e girará de acordo com o ângulo
    retangulo = pygame.Surface((20, 50))
    retangulo.fill((250, 0, 0))  # Cor do retângulo
    retangulo.set_colorkey((0, 0, 0))  # Define transparência para fundo

    # Rotaciona o retângulo baseado no ângulo
    retangulo = pygame.transform.rotate(retangulo, -angulo_graus)

    # Pega o retângulo rotacionado
    retangulo_rect = retangulo.get_rect()

    # Ajusta a posição do retângulo para o ponto calculado
    retangulo_rect.center = (obj_x, obj_y)

    # Desenha o retângulo na tela
    tela.blit(retangulo, retangulo_rect)

    pygame.display.update()
    clock.tick(60)  # Limita a 60 FPS

pygame.quit()
