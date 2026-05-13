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

engrenagem_menu = pygame.image.load("engrenagem.png").convert_alpha()
engrenagem_menu = pygame.transform.scale(engrenagem_menu, (50,50))
engrenagem_menu.set_colorkey((255,255,255))

campo = pygame.image.load("campo.png")
campo = pygame.transform.scale(campo,(600,300))


traveEsquerda = pygame.image.load("traveEsquerda.png")
traveEsquerda = pygame.transform.scale(traveEsquerda, (100,200))
traveEsquerda.set_colorkey((255,255,255))

traveDireita = pygame.image.load("traveDireita.png")
traveDireita = pygame.transform.scale(traveDireita, (100,200))
traveDireita.set_colorkey((255,255,255))

bola = pygame.image.load("bola.png")
bola = pygame.transform.scale(bola, (20,25))
bola.set_colorkey((255,255,255))

tamanho_personagens = [300,300]
jogaBrasil = pygame.image.load("jogaBrasil.png")
jogaBrasil = pygame.transform.scale(jogaBrasil, tamanho_personagens)
jogaBrasil.set_colorkey((255,255,255))      #tira o fundo branco
jogaBrasil = jogaBrasil.convert_alpha()

jogaFranca = pygame.image.load("jogaFranca.png")
jogaFranca = pygame.transform.scale(jogaFranca, tamanho_personagens)
jogaFranca.set_colorkey((255,255,255))      #tira o fundo branco
jogaFranca = jogaFranca.convert_alpha()

jogaAlemanha = pygame.image.load("jogaAlemanha.png")
jogaAlemanha = pygame.transform.scale(jogaAlemanha, tamanho_personagens)
jogaAlemanha.set_colorkey((255,255,255))      #tira o fundo branco
jogaAlemanha = jogaAlemanha.convert_alpha()

jogaEspanha = pygame.image.load("jogaEspanha.png")
jogaEspanha = pygame.transform.scale(jogaEspanha, tamanho_personagens)
jogaEspanha.set_colorkey((255,255,255))      #tira o fundo branco
jogaEspanha = jogaEspanha.convert_alpha()

jogaCroacia = pygame.image.load("jogaCroacia.png")
jogaCroacia = pygame.transform.scale(jogaCroacia, tamanho_personagens)
jogaCroacia.set_colorkey((255,255,255))      #tira o fundo branco
jogaCroacia = jogaCroacia.convert_alpha()

jogaArgentina = pygame.image.load("jogaArgentina.png")
jogaArgentina = pygame.transform.scale(jogaArgentina, tamanho_personagens)
jogaArgentina.set_colorkey((255,255,255))      #tira o fundo branco
jogaArgentina = jogaArgentina.convert_alpha()

jogaInglaterra = pygame.image.load("jogaInglaterra.png")
jogaInglaterra = pygame.transform.scale(jogaInglaterra, tamanho_personagens)
jogaInglaterra.set_colorkey((255,255,255))      #tira o fundo branco
jogaInglaterra = jogaInglaterra.convert_alpha()

jogaPortugal = pygame.image.load("jogaPortugal.png")
jogaPortugal = pygame.transform.scale(jogaPortugal, tamanho_personagens)
jogaPortugal.set_colorkey((255,255,255))      #tira o fundo branco
jogaPortugal = jogaPortugal.convert_alpha()

tamanho_bandeira = [200,100]

bandeiraAlemanha = pygame.image.load("bandeiraAlemanha.png")
bandeiraAlemanha = pygame.transform.scale(bandeiraAlemanha,tamanho_bandeira)

bandeiraBrasil = pygame.image.load("bandeiraBrasil.png")
bandeiraBrasil = pygame.transform.scale(bandeiraBrasil,tamanho_bandeira)

bandeiraArgentina = pygame.image.load("bandeiraArgentina.png")
bandeiraArgentina = pygame.transform.scale(bandeiraArgentina,tamanho_bandeira)

bandeiraCroacia = pygame.image.load("bandeiraCroacia.png")
bandeiraCroacia = pygame.transform.scale(bandeiraCroacia,tamanho_bandeira)

bandeiraEspanha = pygame.image.load("bandeiraEspanha.png")
bandeiraEspanha = pygame.transform.scale(bandeiraEspanha,tamanho_bandeira)

bandeiraFranca = pygame.image.load("bandeiraFranca.png")
bandeiraFranca = pygame.transform.scale(bandeiraFranca,tamanho_bandeira)

bandeiraInglaterra = pygame.image.load("bandeiraInglaterra.png")
bandeiraInglaterra = pygame.transform.scale(bandeiraInglaterra,tamanho_bandeira)

bandeiraPortugal = pygame.image.load("bandeiraPortugal.png")
bandeiraPortugal = pygame.transform.scale(bandeiraPortugal,tamanho_bandeira)

chaves = pygame.image.load("chaves.png")
chaves = pygame.transform.scale(chaves,(600,300))

times = [["Brasil", jogaBrasil, bandeiraBrasil],["França", jogaFranca, bandeiraFranca],["Alemanha", jogaAlemanha, bandeiraAlemanha],["Espanha", jogaEspanha, bandeiraEspanha],["Croácia", jogaCroacia, bandeiraCroacia],["Argentina", jogaArgentina, bandeiraArgentina],["Inglaterra", jogaInglaterra, bandeiraInglaterra],["Portugal", jogaPortugal, bandeiraPortugal]]
time_escolhido = 0
jogador_escolhido = times[time_escolhido][1]
tela_atual = "selecao"


confrontos = [["Brasil", "Portugal"],["Argentina", "Inglaterra"],["França", "Croácia"],["Alemanha", "Espanha"]]
# ===== Loop principal =====

#posicao do jogador e movimentacao

x_jogador = 50
y_jogador = 160
velocidade = 5
vel_y_jogador = 0
gravidade = 1
no_chao = True
while game:
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYDOWN:
            if tela_atual == "selecao":
                if event.key == pygame.K_RIGHT:
                    time_escolhido = time_escolhido+1
                    if time_escolhido >= len(times):
                        time_escolhido = 0
                elif event.key == pygame.K_LEFT:
                    time_escolhido = time_escolhido - 1
                    if time_escolhido < 0:
                        time_escolhido = 7
                elif event.key == pygame.K_RETURN:
                    jogador_escolhido = times[time_escolhido][1]
                    tela_atual = "chave"
            if tela_atual == "chave":
                window.blit(chaves,(0,0))
                if event.key == pygame.K_SPACE:
                    if times[time_escolhido][0] != "França":
                        adversario_escolhido = jogaFranca
                    else:
                        adversario_escolhido = jogaAlemanha
                    tela_atual = "jogo"
            if tela_atual == "jogo":
                
                if event.key == pygame.K_LEFT:
                    x_jogador = x_jogador - velocidade
                elif event.key == pygame.K_RIGHT:
                    x_jogador = x_jogador + velocidade
                if event.key == pygame.K_SPACE:
                    if no_chao:
                        vel_y_jogador = -15
                        no_chao = False
                    

            
            
            
        
    # ----- Gera saídas

    if tela_atual == "selecao":
        window.fill((30,200,30))
        fonte = pygame.font.SysFont(None, 30)

        nome_time = times[time_escolhido][0]
        imagem_time = times[time_escolhido][1]
        bandeira_time = times[time_escolhido][2]

        texto = fonte.render("Escolha seu time", True, (255, 255, 255))
        instrucao = fonte.render("Use as setas e aperte ENTER", True, (255, 255, 255))
        nome = fonte.render(nome_time, True, (255, 255, 255))

        window.blit(texto, (210, 20))
        window.blit(instrucao, (155, 55))
        window.blit(nome, (260, 90))

        window.blit(bandeira_time, (200, 120))
        window.blit(imagem_time, (400, 10))





    if tela_atual == "jogo":
        
        y_jogador += vel_y_jogador
        vel_y_jogador += gravidade
        if y_jogador >= 160:
            y_jogador = 160
            vel_y_jogador = 0
            no_chao = True
        # campo
        window.blit(campo,(0,0))
        #menu
        window.blit(engrenagem_menu, (0, 0))   #Coloca a imagem

        # jogadores e bola
        jogador_escolhido = pygame.transform.scale(jogador_escolhido, (60,60))
        
        window.blit(jogador_escolhido, (x_jogador, y_jogador))
        #window.blit(oponente, (430, 170))
        window.blit(bola, (285, 190))

    #window.fill((80, 180, 80))  # Preenche com a cor de fundo
    #window.blit(bandeiraArgentina, (0, 0))   #Coloca a imagem
    
    
    pygame.display.update()
pygame.quit()
