
# DEV 2 - ETAPA 1
# Controle inicial do jogo

jogador = "X"
venceu = False
empate = False
partida_concluida = False

# Enquanto a partida nao for concluida
while partida_concluida == False:

    # Define o simbolo do jogador atual
    if jogador == "X":
        simbolo = "X"
    else:
        simbolo = "O"

    # Aqui entra a parte do DEV 1:
    # Mostrar o tabuleiro
    # Receber a posicao escolhida
    # Verificar se a posicao esta livre
    # Atualizar o tabuleiro

    # DEV 2 - ETAPA 2
    # Verifica as linhas
    for i in range(3):
        if tabuleiro[i][0] == simbolo and tabuleiro[i][1] == simbolo and tabuleiro[i][2] == simbolo:
            venceu = True

    # Verifica as colunas
    for i in range(3):
        if tabuleiro[0][i] == simbolo and tabuleiro[1][i] == simbolo and tabuleiro[2][i] == simbolo:
            venceu = True

    # Verifica a diagonal principal
    if tabuleiro[0][0] == simbolo and tabuleiro[1][1] == simbolo and tabuleiro[2][2] == simbolo:
        venceu = True

    # Verifica a diagonal secundaria
    if tabuleiro[0][2] == simbolo and tabuleiro[1][1] == simbolo and tabuleiro[2][0] == simbolo:
        venceu = True

    # DEV 2 - ETAPA 3
    # Verifica se houve empate

    if venceu == False:

        casas_vazias = 0

        for i in range(3):
            for j in range(3):
                if tabuleiro[i][j] == " ":
                    casas_vazias = casas_vazias + 1

        if casas_vazias == 0:
            empate = True

    # DEV 2 - ETAPA 4
    # Define o resultado da partida

    if venceu == True:
        resultado_partida = simbolo
        partida_concluida = True

    elif empate == True:
        resultado_partida = "E"
        partida_concluida = True

    # Alterna o jogador para a proxima rodada
    else:
        if jogador == "X":
            jogador = "O"
        else:
            jogador = "X"