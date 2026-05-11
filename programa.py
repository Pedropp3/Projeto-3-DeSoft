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
traveEsquerda = pygame.image.load("traveEsquerda.png")
traveEsquerda = pygame.transform.scale(traveEsquerda, (100,200))
traveEsquerda.set_colorkey((255,255,255))

traveDireita = pygame.image.load("traveDireita.png")
traveDireita = pygame.transform.scale(traveDireita, (100,200))
traveDireita.set_colorkey((255,255,255))

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


times = [["Brasil", jogaBrasil, bandeiraBrasil],["França", jogaFranca, bandeiraFranca],["Alemanha", jogaAlemanha, bandeiraAlemanha],["Espanha", jogaEspanha, bandeiraEspanha],["Croácia", jogaCroacia, bandeiraCroacia],["Argentina", jogaArgentina, bandeiraArgentina],["Inglaterra", jogaInglaterra, bandeiraInglaterra],["Portugal", jogaPortugal, bandeiraPortugal]]
time_escolhido = 0
jogador_escolhido = times[time_escolhido][1]
tela_atual = "selecao"
# ===== Loop principal =====

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
                    tela_atual = "jogo"
        
    # ----- Gera saídas

    if tela_atual == "selecao":
        window.fill((0,255,0))
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


    #window.fill((80, 180, 80))  # Preenche com a cor de fundo
    #window.blit(bandeiraArgentina, (0, 0))   #Coloca a imagem
    

    pygame.display.update()
pygame.quit()
