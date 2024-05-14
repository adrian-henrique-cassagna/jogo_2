import pygame
import random
class personagem:
        def __init__(self,arquivo_imagem,largura,altura,x_inicial,y_inicial):

                self.imagem = pygame.image.load(arquivo_imagem)

                self.largura = largura
                self.altura = altura

                self.imagem = pygame.transform.scale(self.imagem,(self.largura,self.altura))

                self.posicao_X = x_inicial
                self.posicao_Y = y_inicial

                self.hitbox = pygame.mask.from_surface(self.imagem)

                self.hitbox = pygame.mask.from_surface(self.imagem)
                
        def desenhar(self,tela):
                tela.blit(self.imagem,(self.posicao_X,self.posicao_Y))


        def movimento(self,esquerda,direita):
                teclas = pygame.key.get_pressed()

                if teclas[esquerda]:
                        if self.posicao_X > 0:
                                self.posicao_X -= 1

                if teclas[direita]:
                        if self.posicao_X < 1000-self.largura:
                                self.posicao_X += 1
                
                if self.posicao_X > 1000:
                        self.posicao_X = 1000

                if self.posicao_X <= 0:
                        self.posicao_X = 0
        

        def fantasma(self):
                velocidade = random.randint(0,1)
                self.posicao_X = self.posicao_X + velocidade
                if self.posicao_X > 1000:
                        self.posicao_X = 0

        def espada1(self):
                Velocidade = random.randint(0,1)
                self.posicao_Y = self.posicao_Y + Velocidade
                if self.posicao_Y > 1000:
                        self.posicao_Y += 100

                velocidade = random.randint(0,1)
                self.posicao_X = self.posicao_X + velocidade
                if self.posicao_X > 1000:
                        self.posicao_X = 0

                if self.posicao_Y > 700:
                        self.posicao_Y = random.randint(0,1)
                        self.posicao_X = random.randint(0,1000)

        def espada2(self):
                Velocidade = random.randint(0,1)
                self.posicao_Y = self.posicao_Y + Velocidade
                if self.posicao_Y > 1000:
                        self.posicao_Y += 100

                velocidade = random.randint(0,1)
                self.posicao_X = self.posicao_X - velocidade
                if self.posicao_X > 1000:
                        self.posicao_X = 0

                if self.posicao_Y > 700:
                        self.posicao_Y = random.randint(0,110)
                        self.posicao_X = random.randint(0,1000)
        

        
                        