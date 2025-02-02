import pygame
import sys

# Inicializa o Pygame
pygame.init()

# Configurações da tela
largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Meu Primeiro Jogo")

# Cores
preto = (0, 0, 0)
branco = (255, 255, 255)
vermelho = (255, 0, 0)

# Variáveis do círculo
x, y = largura // 2, altura // 2
velocidade = 5

# Loop principal
while True:
    # Processa eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Movimenta o círculo com as teclas
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_UP]:
        y -= velocidade
    if teclas[pygame.K_DOWN]:
        y += velocidade
    if teclas[pygame.K_LEFT]:
        x -= velocidade
    if teclas[pygame.K_RIGHT]:
        x += velocidade

    # Atualiza a tela
    tela.fill(preto)
    pygame.draw.circle(tela, vermelho, (x, y), 30)
    pygame.display.flip()

    # Controla a taxa de quadros
    pygame.time.Clock().tick(60)