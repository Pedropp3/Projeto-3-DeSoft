# ===== Inicialização =====
# ----- Importa e inicia pacotes

import pygame


pygame.init()

# ----- Gera tela principal
window = pygame.display.set_mode((600, 300))
pygame.display.set_caption('Jogo do Pedro, Nicolas e Eduardo')

# ----- Inicia estruturas de dados
game = True
pygame.mixer.init()

# ----- Personagesns e objetos

pygame.mixer.music.load('estadio.wav')
pygame.mixer.music.set_volume(0.4)
chute_som = pygame.mixer.Sound('chute.mp3')
gol_som = pygame.mixer.Sound('gol.mp3')
vaia_som = pygame.mixer.Sound('vaia.mp3')



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
bola = bola.convert_alpha()



bola2 = pygame.image.load("bola2.png")
bola2 = pygame.transform.scale(bola2, (20,25))
bola2.set_colorkey((255,255,255))
bola2 = bola2.convert_alpha()

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

jogaBrasil2 = pygame.image.load("jogaBrasil2.png")
jogaBrasil2 = pygame.transform.scale(jogaBrasil2, tamanho_personagens)
jogaBrasil2.set_colorkey((255,255,255))      #tira o fundo branco
jogaBrasil2 = jogaBrasil2.convert_alpha()

jogaFranca2 = pygame.image.load("jogaFranca2.png")
jogaFranca2 = pygame.transform.scale(jogaFranca2, tamanho_personagens)
jogaFranca2.set_colorkey((255,255,255))      #tira o fundo branco
jogaFranca2 = jogaFranca2.convert_alpha()

jogaAlemanha2 = pygame.image.load("jogaAlemanha2.png")
jogaAlemanha2 = pygame.transform.scale(jogaAlemanha2, tamanho_personagens)
jogaAlemanha2.set_colorkey((255,255,255))      #tira o fundo branco
jogaAlemanha2 = jogaAlemanha2.convert_alpha()

jogaEspanha2 = pygame.image.load("jogaEspanha2.png")
jogaEspanha2 = pygame.transform.scale(jogaEspanha2, tamanho_personagens)
jogaEspanha2.set_colorkey((255,255,255))      #tira o fundo branco
jogaEspanha2 = jogaEspanha2.convert_alpha()

jogaCroacia2 = pygame.image.load("jogaCroacia2.png")
jogaCroacia2 = pygame.transform.scale(jogaCroacia2, tamanho_personagens)
jogaCroacia2.set_colorkey((255,255,255))      #tira o fundo branco
jogaCroacia2 = jogaCroacia2.convert_alpha()

jogaArgentina2 = pygame.image.load("jogaArgentina2.png")
jogaArgentina2 = pygame.transform.scale(jogaArgentina2, tamanho_personagens)
jogaArgentina2.set_colorkey((255,255,255))      #tira o fundo branco
jogaArgentina2 = jogaArgentina2.convert_alpha()

jogaInglaterra2 = pygame.image.load("jogaInglaterra2.png")
jogaInglaterra2 = pygame.transform.scale(jogaInglaterra2, tamanho_personagens)
jogaInglaterra2.set_colorkey((255,255,255))      #tira o fundo branco
jogaInglaterra2 = jogaInglaterra2.convert_alpha()

jogaPortugal2 = pygame.image.load("jogaPortugal2.png")
jogaPortugal2 = pygame.transform.scale(jogaPortugal2, tamanho_personagens)
jogaPortugal2.set_colorkey((255,255,255))      #tira o fundo branco
jogaPortugal2 = jogaPortugal2.convert_alpha()

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

telavitoria = pygame.image.load("vitoria.png")
telavitoria = pygame.transform.scale(telavitoria,(600,300))

chaves = pygame.image.load("chaves.png")
chaves = pygame.transform.scale(chaves,(600,300))

teladerrota = pygame.image.load("derrota.png")
teladerrota = pygame.transform.scale(teladerrota,(600,300))

# [nome do time, imagem do jogador, bandeira, imagem do jogador em movimento]
times = [["Brasil", jogaBrasil, bandeiraBrasil, jogaBrasil2],["França", jogaFranca, bandeiraFranca, jogaFranca2],["Alemanha", jogaAlemanha, bandeiraAlemanha, jogaAlemanha2],["Espanha", jogaEspanha, bandeiraEspanha, jogaEspanha2],["Croácia", jogaCroacia, bandeiraCroacia, jogaCroacia2],["Argentina", jogaArgentina, bandeiraArgentina, jogaArgentina2],["Inglaterra", jogaInglaterra, bandeiraInglaterra, jogaInglaterra2],["Portugal", jogaPortugal, bandeiraPortugal, jogaPortugal2]]
time_escolhido = 0
jogador_escolhido = times[time_escolhido][1]
jogador_escolhido2 = times[time_escolhido][3]
adversario_escolhido = pygame.transform.scale(jogaFranca, (60, 60))
adversario_escolhido2 = pygame.transform.scale(jogaFranca2, (60, 60))
tela_atual = "selecao"


confrontos = [["Brasil", "Portugal"],["Argentina", "Inglaterra"],["França", "Croácia"],["Alemanha", "Espanha"]]


# Rodada 1 = quartas de final
# Rodada 2 = semifinal
# Rodada 3 = final
def escolher_nome_adversario(time_jogador_nome, rodada):
    if rodada == 1:
        for confronto in confrontos:
            if time_jogador_nome in confronto:
                if confronto[0] == time_jogador_nome:
                    return confronto[1]
                else:
                    return confronto[0]

    elif rodada == 2:
        if time_jogador_nome in ["Brasil", "Portugal"]:
            return "Argentina"
        elif time_jogador_nome in ["Argentina", "Inglaterra"]:
            return "Brasil"
        elif time_jogador_nome in ["França", "Croácia"]:
            return "Alemanha"
        elif time_jogador_nome in ["Alemanha", "Espanha"]:
            return "França"

    elif rodada == 3:
        if time_jogador_nome in ["Brasil", "Portugal", "Argentina", "Inglaterra"]:
            return "França"
        else:
            return "Brasil"

    return "França"


def pegar_imagens_time(nome_time):
    for time in times:
        if time[0] == nome_time:
            img1 = pygame.transform.scale(time[1], (60, 60))
            img2 = pygame.transform.scale(time[3], (60, 60))
            return img1, img2
    return pygame.transform.scale(jogaFranca, (60, 60)), pygame.transform.scale(jogaFranca2, (60, 60))


rodada_chaves = 1
menu_aberto = False
volume = 0.5
# ===== Loop principal =====

#variaveis iniciais
gravidade = 0.7

x_jogador = 50
y_jogador = 160
velocidade = 5
vel_y_jogador = 0
no_chao = True

x_oponente = 450
y_oponente = 160
vel_oponente = 2
no_chao_oponente = True
vel_y_oponente = 0


bola_no_chao = False
x_bola = 285
y_bola = 50
vel_x_bola = 0
vel_y_bola = 0
gravidade_bola = 0.3
tempo_bola_no_ar = 0

contador_jogador = 0
contador_oponente = 0

perdeu = 0

clock = pygame.time.Clock()
contagem = 0 #para o som da torcida e mudanca de aparencia

mostrar_gol = 0
while game:
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            print(mouse_pos)
            # tamanho da engrenagem 
            if mouse_pos[0] <= 50 and mouse_pos[1] <= 50:
                menu_aberto =  True
            if 200 <= mouse_pos[0] <= 210:
                if 150 <= mouse_pos[1] <= 180:
                    volume = volume+0.1
            if 290 < mouse_pos[0] <= 310:
                if 150 <= mouse_pos[1] <= 180:
                    volume = volume-0.1
            
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYDOWN:
            if menu_aberto:
                if event.key == pygame.K_ESCAPE:
                    menu_aberto = False
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
                    jogador_escolhido2 = times[time_escolhido][3]
                    tela_atual = "chave"
                    
            if tela_atual == "chave":
                pygame.time.delay(1000)
                if event.key == pygame.K_SPACE:
                    time_jogador_nome = times[time_escolhido][0]
                    nome_adversario = escolher_nome_adversario(time_jogador_nome, rodada_chaves)
                    adversario_escolhido, adversario_escolhido2 = pegar_imagens_time(nome_adversario)

                    if rodada_chaves < 4:
                        tela_atual = "jogo"
                        primeira = 1
                    else:
                        tela_atual = "vitoria"

            
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
        if rodada_chaves < 4:
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
                    
        else:
            tela_atual = "vitoria"
        

    
        
    if tela_atual == "selecao" and not menu_aberto:
      
        

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
        pygame.time.delay(1000)

    contagem=contagem+1
    if contagem%120 == 0 and tela_atual == "jogo":
        if not menu_aberto:
            pygame.mixer.music.play()
        



    if perdeu == 1:
        pygame.time.delay(2000)
        game = False
        continue

    
    if tela_atual == "jogo" and rodada_chaves < 4 and not menu_aberto:
        
        
        if rodada_chaves == 1:
            vel_oponente = 1
        elif rodada_chaves == 2:
            vel_oponente = 1.5
        elif rodada_chaves == 3:
            vel_oponente = 2
        
        # descobrir confronto do jogador
        time_jogador_nome = times[time_escolhido][0]

        for confronto in confrontos:
            if time_jogador_nome in confronto:
                if confronto[0] == time_jogador_nome:
                    nome_adversario = confronto[1]
                else:
                    nome_adversario = confronto[0]

   
        


        if x_bola >= 550 and y_bola > 130:
            mostrar_gol = 1

        elif x_bola <50 and y_bola > 130:
            mostrar_gol = 1
            

        if y_bola <=130 and x_bola >= 550:
            vel_x_bola = -5
            tempo_bola_no_ar = 0
        elif y_bola <=130 and x_bola <= 50:
            vel_x_bola = 5
            tempo_bola_no_ar = 0


        #gravifade oponente
        vel_y_oponente = gravidade
        y_oponente += vel_y_oponente


        

        
        print(y_jogador)
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

        # Se o jogador ou oponente encostar na bola, a bola é chutada para cima para o lado.
        if abs(x_oponente - x_bola) < 30 and no_chao_oponente:
            if y_oponente > y_bola:
                y_oponente += -20
                no_chao_oponente = False
        if y_oponente >= 160:
            y_oponente = 160
            vel_y_oponente = 0
            no_chao_oponente = True
        if abs(x_jogador - x_bola) <= 30:
            if abs(y_jogador - y_bola) <= 10:
                tempo_bola_no_ar = 4
                vel_x_bola = 5 #empurra pra direita
                vel_y_bola = -4 #levanta a bolabola 
                chute_som.play()
            elif y_bola - y_jogador < 30 and y_bola > y_jogador:
                tempo_bola_no_ar = 4
                vel_x_bola = 5 #empurra pra direita
                vel_y_bola = -4 #levanta a bolabola 
                chute_som.play()
        if abs(x_oponente - x_bola) <= 30:
            if abs(y_oponente - y_bola) <= 10:
                tempo_bola_no_ar = 4
                vel_x_bola = -5 #empurra pra esquerda
                vel_y_bola = -4 #levanta a bolabola 
                chute_som.play()
            elif y_bola - y_oponente < 30 and y_bola > y_oponente:
                tempo_bola_no_ar = 4
                vel_x_bola = -5 #empurra pra direita
                vel_y_bola = -4 #levanta a bolabola
                chute_som.play()

        
            

        # chão
        if y_bola >= 190:
            y_bola = 190
            bola_no_chao = True
        if bola_no_chao:
            vel_y_bola = - tempo_bola_no_ar * gravidade_bola*0.9 #quica

            
            tempo_bola_no_ar = 0
            bola_no_chao = False
        
        
        
        if primeira == 1:

            fonte = pygame.font.SysFont(None, 80)
            contador_jogador = 0
            contador_oponente = 0
            x_bola = 285
            y_bola = 50
            x_jogador = 50
            y_jogador = 160
            vel_y_jogador = 0
            
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
        jogador_img1 = pygame.transform.scale(jogador_escolhido, (60, 60))
        jogador_img2 = pygame.transform.scale(jogador_escolhido2, (60, 60))


        # Alterna entre duas imagens para simular movimento dos jogadores e da bola.
        frame_animacao = (contagem // 15) % 2

        if frame_animacao == 0:
            window.blit(jogador_img1, (x_jogador, y_jogador))
            window.blit(adversario_escolhido, (x_oponente, y_oponente))
            window.blit(bola, (x_bola, y_bola))
        else:
            window.blit(jogador_img2, (x_jogador, y_jogador))
            window.blit(adversario_escolhido2, (x_oponente, y_oponente))
            window.blit(bola2, (x_bola, y_bola))


        #window.blit(oponente, (430, 170))





    #window.fill((80, 180, 80))   Preenche com a cor de fundo
    #window.blit(bandeiraArgentina, (0, 0))   Coloca a imagem
        placar_texto = fonte.render(f"{contador_jogador} x {contador_oponente}", True, (255,255,255))
        if mostrar_gol == 1:
                
                texto = fonte.render("GOOOL!", True, (255, 255, 0))
                window.blit(texto, (200, 100))
                pygame.time.delay(100)
                if x_bola > 300:
                    contador_jogador += 1
                    pygame.mixer.stop()
                    gol_som.play()
                else: 
                    contador_oponente +=1
                    pygame.mixer.stop()
                    vaia_som.play()
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
                window.blit(teladerrota,(0,0))
                perdeu = 1
        if perdeu == 0:
            window.blit(placar_texto, (250, 10))
    if menu_aberto:
        overlay = pygame.Surface((600,300))
        overlay.set_alpha(180)
        overlay.fill((0,0,0))
        window.blit(overlay, (0,0))
        fonte = pygame.font.SysFont("arial", 30)
        window.blit(fonte.render("MENU", True, (255,255,255)), (250, 40))
        window.blit(fonte.render(f"Volume: {int(volume*100)}%", True, (255,255,255)), (200, 100))
        window.blit(fonte.render(f"+            -", True, (255,255,255)), (200, 150))
        window.blit(fonte.render("Sair (ESC)", True, (255,255,255)), (200, 200))

        if volume < 0:
            volume = 0
        if volume > 1:
            volume = 1

        pygame.mixer.music.set_volume(volume)
        gol_som.set_volume(volume)
        vaia_som.set_volume(volume)
        chute_som.set_volume(volume)
           
        
    if tela_atual == "vitoria":
        window.blit(telavitoria,(0,0))
        
    clock.tick(60) #FPS
    pygame.display.update()
pygame.quit()
