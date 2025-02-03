import pygame

pygame.init()

# definindo tamanho de tela
largura, altura = 1000, 600
tela = pygame.display.set_mode((largura, altura))

# Definindo o título da janela
pygame.display.set_caption('Projeto_Teste')

# Definindo objeto player
x, y = 200, 150
velocidade = 5
tamanho = 50

clock = pygame.time.Clock()

rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: # Fecha a tela se clicar no x da janela
            rodando = False
    
        teclas = pygame.key.get_pressed()
        if teclas == pygame.K_LEFT:
            x -= 1
        if teclas == pygame.K_RIGHT:
            x += 1
        if teclas == pygame.K_UP:
            y -= 1
        if teclas == pygame.K_DOWN:
            y += 1
            
        
        pygame.draw.rect(tela, (0, 255, 0), (x, y, tamanho, tamanho))

        pygame.display.update()
        clock.tick(30)  # Limita a 30 FPS
pygame.quit()