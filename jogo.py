# DEV 2 - ETAPA 1
# Controle inicial do jogo

jogador = "X"
venceu = False
empate = False

# Enquanto ninguém vencer e não houver empate
while venceu == False and empate == False:

    # Define o símbolo do jogador atual
    if jogador == "X":
        simbolo = "X"
    else:
        simbolo = "O"

    # Controle para saber se a jogada foi válida
    jogada_valida = False

    # Aqui entra a parte do DEV 1:
    # Mostrar o tabuleiro
    # Receber a posição escolhida
    # Verificar se a posição está livre
    # Atualizar o tabuleiro

    # DEV 2 - ETAPA 2
    # Verificação de vitória nas linhas

    # Verifica as linhas
    for i in range(3):
        if tabuleiro[i][0] == simbolo and tabuleiro[i][1] == simbolo and tabuleiro[i][2] == simbolo:
            venceu = True