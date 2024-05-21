import pygame
from personagens import*
import random
#iniciando a tela
pygame.__init__
tela = pygame.display.set_mode((1000,700))
v1 = True
#carregando o mapa
FUNDO = pygame.image.load("imagens/imagem_1.jpg")
FUNDO = pygame.transform.scale(FUNDO,(1000,700))
CHAO = pygame.image.load("imagens/imagem_2.jpg")
CHAO = pygame.transform.scale(CHAO,(1000,100))
#carregando o personagem
TALON = personagem("imagens/imagem_talon.jpg",75,50,400,450)
ESPADA1 = personagem("imagens/1223459_orig.jpg",125,75,250,150)
ESPADA2 = personagem("imagens/1223459_orig.jpg",125,75,300,100)
ESPADA3 = personagem("imagens/1223459_orig.jpg",125,75,450,50)

#mantendo a tela
while v1:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            v1 = False
    tempo = 0

#movimentação
    TALON.movimento(pygame.K_a, pygame.K_d)
    ESPADA1.espada1() and ESPADA1.fantasma()
    ESPADA2.espada2() and ESPADA2.fantasma()
    ESPADA3.espada2() and ESPADA2.fantasma()
#colisão
    if TALON.hitbox.overlap(ESPADA1.hitbox,(ESPADA1.posicao_X-TALON.posicao_X,(ESPADA1.posicao_Y - TALON.posicao_Y))):
        TALON.posicao_Y = 450
        TALON.posicao_X = 400
        ESPADA1.posicao_X = random.randint(0,400)
        ESPADA1.posicao_Y = random.randint(0,100)
        ESPADA2.posicao_X = random.randint(0,400)
        ESPADA2.posicao_Y = random.randint(0,100)
        ESPADA3.posicao_X = random.randint(0,400)
        ESPADA3.posicao_Y = random.randint(0,100)
        

    if TALON.hitbox.overlap(ESPADA2.hitbox,(ESPADA2.posicao_X-TALON.posicao_X,(ESPADA2.posicao_Y - TALON.posicao_Y))):
        TALON.posicao_Y = 450
        TALON.posicao_X = 400
        ESPADA1.posicao_X = random.randint(0,400)
        ESPADA1.posicao_Y = random.randint(0,100)
        ESPADA2.posicao_X = random.randint(0,400)
        ESPADA2.posicao_Y = random.randint(0,100)
        ESPADA3.posicao_X = random.randint(0,400)
        ESPADA3.posicao_Y = random.randint(0,100)
        
    
    if TALON.hitbox.overlap(ESPADA3.hitbox,(ESPADA3.posicao_X-TALON.posicao_X,(ESPADA3.posicao_Y - TALON.posicao_Y))):
        TALON.posicao_Y = 450
        TALON.posicao_X = 400
        ESPADA1.posicao_X = random.randint(0,400)
        ESPADA1.posicao_Y = random.randint(0,100)
        ESPADA2.posicao_X = random.randint(0,400)
        ESPADA2.posicao_Y = random.randint(0,100)
        ESPADA3.posicao_X = random.randint(0,400)
        ESPADA3.posicao_Y = random.randint(0,100)
        
    #pontuação e perdeu o game
    if tempo >= 0:
        if tempo == 5:
            TALON.pontuacão += 0.1

        print(TALON.pontuacão)
    if TALON.hitbox.overlap(ESPADA3.hitbox,(ESPADA3.posicao_X-TALON.posicao_X,(ESPADA3.posicao_Y - TALON.posicao_Y))):
        TALON.pontuacão = 0
    if TALON.hitbox.overlap(ESPADA2.hitbox,(ESPADA2.posicao_X-TALON.posicao_X,(ESPADA2.posicao_Y - TALON.posicao_Y))):
        TALON.pontuacão = 0
    if TALON.hitbox.overlap(ESPADA1.hitbox,(ESPADA1.posicao_X-TALON.posicao_X,(ESPADA1.posicao_Y - TALON.posicao_Y))):
        TALON.pontuacão = 0
    #pontuacao_jogo = pontuacao.render(f"Pontuação do jogador:{TALON.pontuacão}",True(0,0,0))
    
#carregamdo imagens no jogo
    tela.blit(FUNDO,(0,0))
    tela.blit(CHAO,(0,500))
    TALON.desenhar(tela)
    ESPADA1.desenhar(tela)
    ESPADA2.desenhar(tela)
    ESPADA3.desenhar(tela)
    #atualizando o jogo para cada auteração feita
    pygame.display.update()