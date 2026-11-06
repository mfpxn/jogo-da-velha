# ==========================================
# DEV 2 - ETAPA 1
# CONTROLE DOS JOGADORES
# ==========================================

# Define quem começa a partida
jogador = "X"

# Variáveis de controle do jogo
venceu = False
empate = False

# Enquanto não existir vencedor ou empate, o jogo continua
while venceu == False and empate == False:

    # Define o símbolo do jogador atual
    if jogador == "X":
        simbolo = "X"
    else:
        simbolo = "O"

    # Indica que ainda não foi realizada uma jogada válida
    jogada_valida = False

    # ==========================================
    # ESPAÇO PARA O CÓDIGO DO DEV 1
    # O DEV 1 deverá:
    # 1. Solicitar a jogada.
    # 2. Validar a posição.
    # 3. Atualizar o tabuleiro.
    # 4. Alterar jogada_valida para True
    #    somente se a jogada for válida.
    # ==========================================
