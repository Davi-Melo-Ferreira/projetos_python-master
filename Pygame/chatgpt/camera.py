import pygame

# Inicialização
pygame.init()

# Configurações da tela
LARGURA, ALTURA = 500, 500
tela = pygame.display.set_mode((LARGURA, ALTURA))

# Definição de cores
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)
AZUL = (0, 0, 255)

# Criando um retângulo (jogador)
player = pygame.Rect(250, 250, 50, 50)

# Criando um fundo maior (como se fosse um mundo grande)
mundo_largura, mundo_altura = 1000, 1000
fundo = pygame.Surface((mundo_largura, mundo_altura))
fundo.fill(AZUL)  # Fundo azul para diferenciar

# Variáveis de controle
velocidade = 5
offset_x, offset_y = 0, 0  # Deslocamento da "câmera"

# Loop principal do jogo
rodando = True
while rodando:
    pygame.time.delay(30)

    # Captura eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # Movimento do jogador
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        player.x -= velocidade
    if teclas[pygame.K_RIGHT]:
        player.x += velocidade
    if teclas[pygame.K_UP]:
        player.y -= velocidade
    if teclas[pygame.K_DOWN]:
        player.y += velocidade

    # Atualizando a câmera (centralizando o jogador)
    offset_x = player.x - LARGURA // 2
    offset_y = player.y - ALTURA // 2

    # Limpa a tela
    tela.fill(BRANCO)

    # Desenha o fundo deslocado
    tela.blit(fundo, (-offset_x, -offset_y))

    # Desenha o jogador deslocado
    pygame.draw.rect(tela, VERMELHO, (player.x - offset_x, player.y - offset_y, player.width, player.height))

    # Atualiza a tela
    pygame.display.flip()

pygame.quit()
