# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame

pygame.init()

# ----- Gera tela principal
window = pygame.display.set_mode((600, 300))
pygame.display.set_caption('Jogo do Pedro, Nicolas e Eduardo')

# ----- Inicia estruturas de dados
game = True

# ----- Personagesns e objetos

bola = pygame.image.load("bola.png")
bola = pygame.transform.scale(bola, (90,100))
bola.set_colorkey((255,255,255))

tamanho_personagens = [300,300]
jogaBrasil = pygame.image.load("jogaBrasil.png")
jogaBrasil = pygame.transform.scale(jogaBrasil, tamanho_personagens)
jogaBrasil.set_colorkey((255,255,255))      #tira o fundo branco

jogaFranca = pygame.image.load("jogaFranca.png")
jogaFranca = pygame.transform.scale(jogaFranca, tamanho_personagens)
jogaFranca.set_colorkey((255,255,255))      #tira o fundo branco

jogaAlemanha = pygame.image.load("jogaAlemanha.png")
jogaAlemanha = pygame.transform.scale(jogaAlemanha, tamanho_personagens)
jogaAlemanha.set_colorkey((255,255,255))      #tira o fundo branco

jogaEspanha = pygame.image.load("jogaEspanha.png")
jogaEspanha = pygame.transform.scale(jogaEspanha, tamanho_personagens)
jogaEspanha.set_colorkey((255,255,255))      #tira o fundo branco

jogaCroacia = pygame.image.load("jogaCroacia.png")
jogaCroacia = pygame.transform.scale(jogaCroacia, tamanho_personagens)
jogaCroacia.set_colorkey((255,255,255))      #tira o fundo branco

jogaArgentina = pygame.image.load("jogaArgentina.png")
jogaArgentina = pygame.transform.scale(jogaArgentina, tamanho_personagens)
jogaArgentina.set_colorkey((255,255,255))      #tira o fundo branco

jogaInglaterra = pygame.image.load("jogaInglaterra.png")
jogaInglaterra = pygame.transform.scale(jogaInglaterra, tamanho_personagens)
jogaInglaterra.set_colorkey((255,255,255))      #tira o fundo branco

jogaPortugal = pygame.image.load("jogaPortugal.png")
jogaPortugal = pygame.transform.scale(jogaPortugal, tamanho_personagens)
jogaPortugal.set_colorkey((255,255,255))      #tira o fundo branco



# ===== Loop principal =====
while game:
    
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False
    
    # ----- Gera saídas
    window.fill((80, 180, 80))  # Preenche com a cor de fundo
    window.blit(bola, (0, 0))   #Coloca a imagem
    
    # ----- Atualiza estado do,  jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados
