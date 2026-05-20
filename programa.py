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
rodada_chaves = 1
# ===== Loop principal =====

#variaveis iniciais


x_jogador = 50
y_jogador = 160
velocidade = 5
vel_y_jogador = 0
no_chao = True

x_oponente = 450
y_oponente = 160
vel_oponente = 2

bola_no_chao = False
x_bola = 285
y_bola = 50
vel_x_bola = 0
vel_y_bola = 0
gravidade_bola = 0.3
tempo_bola_no_ar = 0

contador_jogador = 0
contador_oponente = 0

clock = pygame.time.Clock()

mostrar_gol = 0
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
                if event.key == pygame.K_SPACE:
                    if times[time_escolhido][0] != "França":
                        adversario_escolhido = jogaFranca
                    else:
                        adversario_escolhido = jogaAlemanha
                    tela_atual = "jogo"
                    primeira = 1
            
            if tela_atual == "jogo":
                
                if event.key == pygame.K_LEFT:
                    velocidade = - 3
                elif event.key == pygame.K_RIGHT:
                    velocidade = 3
                if event.key == pygame.K_SPACE:
                    if no_chao:
                        vel_y_jogador = -20
                        no_chao = False
        
        if event.type == pygame.KEYUP:
            if tela_atual == "jogo":
                if event.key == pygame.K_LEFT:
                    velocidade = 0
                elif event.key == pygame.K_RIGHT:
                    velocidade =  0
                    

            
            
            
        
    # ----- Gera saídas
    if tela_atual == "chave":
        
        window.blit(chaves, (0, 0))

        fonte = pygame.font.SysFont(None, 20)

        # posições baseadas na SUA imagem
        posicoes = [
            (10, 260),   # Brasil
            (85, 260),  # Portugal

            (155, 260),  # Argentina
            (230, 260),  # Inglaterra

            (310, 260),  # França
            (385, 260),  # Croácia

            (455, 260),  # Alemanha
            (535, 260),  # Espanha
        ]
        bandeiraBrasil = pygame.transform.scale(bandeiraBrasil, (60,30))
        bandeiraPortugal = pygame.transform.scale(bandeiraPortugal, (60,30))
        bandeiraArgentina = pygame.transform.scale(bandeiraArgentina, (60,30))
        bandeiraInglaterra = pygame.transform.scale(bandeiraInglaterra, (60,30))
        bandeiraFranca = pygame.transform.scale(bandeiraFranca, (60,30))
        bandeiraCroacia = pygame.transform.scale(bandeiraCroacia, (60,30))
        bandeiraAlemanha = pygame.transform.scale(bandeiraAlemanha, (60,30))
        bandeiraEspanha = pygame.transform.scale(bandeiraEspanha, (60,30))
        
        bandeiras_times = {
            "Brasil": bandeiraBrasil,
            "Portugal": bandeiraPortugal,
            "Argentina": bandeiraArgentina,
            "Inglaterra": bandeiraInglaterra,
            "França": bandeiraFranca,
            "Croácia": bandeiraCroacia,
            "Alemanha": bandeiraAlemanha,
            "Espanha": bandeiraEspanha}
        bandeira_jogador = times[time_escolhido][2]
        time_jogador = times[time_escolhido][0]

        bandeira_jogador = pygame.transform.scale(bandeira_jogador, (60, 30)) 
        bandeiras = [
            bandeiraBrasil, bandeiraPortugal,
            bandeiraArgentina, bandeiraInglaterra,
            bandeiraFranca, bandeiraCroacia,
            bandeiraAlemanha, bandeiraEspanha]

        for i in range(len(bandeiras)):
            window.blit(bandeiras[i], posicoes[i])
        if rodada_chaves >= 2:
            time_jogador = times[time_escolhido][0]

            semifinalistas = ["Brasil", "Argentina", "França", "Alemanha"]

            if time_jogador in ["Brasil", "Portugal"]:
                semifinalistas[0] = time_jogador

            elif time_jogador in ["Argentina", "Inglaterra"]:
                semifinalistas[1] = time_jogador

            elif time_jogador in ["França", "Croácia"]:
                semifinalistas[2] = time_jogador

            elif time_jogador in ["Alemanha", "Espanha"]:
                semifinalistas[3] = time_jogador

            pos_semis = [
                (50, 140),
                (192, 140),
                (348, 140),
                (491, 140)
            ]

            for i in range(4):
                nome = semifinalistas[i]
                bandeira = pygame.transform.scale(bandeiras_times[nome], (60, 30))
                window.blit(bandeira, pos_semis[i])
            if rodada_chaves >= 3:
                if time_jogador in ["Brasil","Argentina"]:
                    window.blit(bandeira_jogador, (225,17))
                    window.blit(bandeiraFranca, (310,17))
                else:
                    window.blit(bandeiraBrasil, (225,17))
                    window.blit(bandeira_jogador, (310,17))
                
            
        


        
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
        # descobrir confronto do jogador
        time_jogador_nome = times[time_escolhido][0]

        for confronto in confrontos:
            if time_jogador_nome in confronto:
                if confronto[0] == time_jogador_nome:
                    nome_adversario = confronto[1]
                else:
                    nome_adversario = confronto[0]

        # pegar imagem do adversário
        for time in times:
            if time[0] == nome_adversario:
                oponente = time[1]
        fonte = pygame.font.SysFont(None, 80)
        if x_bola >= 550 or x_bola <50:
            mostrar_gol = 1
        print(vel_y_bola)
        if vel_y_bola > 0:
            tempo_bola_no_ar += 1
        vel_y_bola += gravidade_bola
        x_bola = x_bola + vel_x_bola
        y_bola = y_bola + vel_y_bola
        # oponente segue a bola
        if x_oponente < x_bola:
            x_oponente += vel_oponente
        elif x_oponente > x_bola:
            x_oponente -= vel_oponente
        if abs(x_jogador - x_bola) <= 30 and abs(y_jogador - y_bola) <= 40:
            tempo_bola_no_ar = 4
            vel_x_bola = velocidade*1.5 #empurra pra direita
            vel_y_bola = -1 #levanta a bolabola += vel_x_bola
            

        # chão
        if y_bola >= 190:
            y_bola = 190
            bola_no_chao = True
        if bola_no_chao:
            vel_y_bola = - tempo_bola_no_ar * gravidade_bola*0.9 #quica

            
            tempo_bola_no_ar = 0
            bola_no_chao = False
        
        
        
        if primeira == 1:
            contador_jogador = 0
            contador_oponente = 0
            x_bola = 285
            y_bola = 50
            x_jogador = 50
            y_jogador = 160
            vel_y_jogador = 0
            gravidade = 0.8
            no_chao = True
            x_oponente = 450
            y_oponente = 160

            primeira = 0
            velocidade = 0
        y_jogador += vel_y_jogador
        vel_y_jogador = gravidade
        if y_jogador >= 160:
            y_jogador = 160
            vel_y_jogador = 0
            no_chao = True
        if x_jogador <= 0:
            x_jogador = 0
        if x_jogador >= 540:
            x_jogador = 540
        x_jogador = x_jogador + velocidade
        # campo
        
        window.blit(campo,(0,0))
        
        
        #menu
        window.blit(engrenagem_menu, (0, 0))   #Coloca a imagem

        # jogadores e bola
        jogador_escolhido = pygame.transform.scale(jogador_escolhido, (60,60))
        
        window.blit(jogador_escolhido, (x_jogador, y_jogador))
        #window.blit(oponente, (430, 170))
        window.blit(bola, (x_bola, y_bola))
        adversario_escolhido = pygame.transform.scale(adversario_escolhido, (60,60))
        window.blit(adversario_escolhido, (x_oponente, y_oponente))
    #window.fill((80, 180, 80))  # Preenche com a cor de fundo
    #window.blit(bandeiraArgentina, (0, 0))   #Coloca a imagem
        placar_texto = fonte.render(f"{contador_jogador} x {contador_oponente}", True, (255,255,255))
        if mostrar_gol == 1:
                
                texto = fonte.render("GOOOL!", True, (255, 255, 0))
                window.blit(texto, (200, 100))
                pygame.time.delay(500)
                if x_bola > 300:
                    contador_jogador += 1
                else: 
                    contador_oponente +=1
                x_bola = 285
                y_bola = 50
                vel_x_bola = 0
                
                x_jogador = 50
                y_jogador = 160

                x_oponente = 450
                y_oponente = 160
                
                mostrar_gol = 0
                placar_texto = fonte.render(f"{contador_jogador} x {contador_oponente}", True, (255,255,255))
        if contador_oponente == 3 or contador_jogador == 3:
            if contador_jogador == 3:
                rodada_chaves = rodada_chaves + 1
                tela_atual = "chave"
                
            else:
                window.fill((200,0,0))
                placar_texto = fonte.render("PERDEU", True, (255,255,255))
        
        window.blit(placar_texto, (250, 10))
    clock.tick(60) #FPS
    pygame.display.update()
pygame.quit()
