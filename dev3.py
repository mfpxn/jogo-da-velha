# PROJETO JOGO DA VELHA - DEV 3
# Gerenciamento geral do jogo

# MATRIZ COMPARTILHADA COM O DEV 1
# Na integracao, os dois devem utilizar esta mesma matriz.

tabuleiro = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

# PLACAR ACUMULADO

vitorias_x = 0
vitorias_o = 0
empates = 0
total_partidas = 0

# ESTATISTICAS DA SESSAO

campeonatos_iniciados = 0
campeonatos_vencidos_x = 0
campeonatos_vencidos_o = 0
campeonatos_empatados = 0

# CONTROLE DO CAMPEONATO MELHOR DE 3

partidas_campeonato = 0
vitorias_campeonato_x = 0
vitorias_campeonato_o = 0
campeonato_ativo = False
campeao = ""

# CONTROLE DA INTEGRACAO

integracao_pronta = True

# CONTROLE DO PROGRAMA

executando = True

while executando == True:

    iniciar_partida = False
    modo_campeonato = False

    print("==============================")
    print("        JOGO DA VELHA")
    print("==============================")
    print("1 - Iniciar partida")
    print("2 - Campeonato Melhor de 3")
    print("3 - Ver placar acumulado")
    print("4 - Ver estatisticas")
    print("5 - Sair")
    print("==============================")

    opcao = input("Escolha uma opcao: ")

    # INICIAR PARTIDA NORMAL

    if opcao == "1":

        modo_campeonato = False
        iniciar_partida = True

    # INICIAR CAMPEONATO

    elif opcao == "2":

        modo_campeonato = True
        iniciar_partida = True

        partidas_campeonato = 0
        vitorias_campeonato_x = 0
        vitorias_campeonato_o = 0
        campeonato_ativo = True
        campeonato_contabilizado = False
        campeao = ""


        print("==============================")
        print(" CAMPEONATO MELHOR DE 3")
        print("==============================")

    # CONSULTAR PLACAR

    elif opcao == "3":

        print("==============================")
        print("      PLACAR ACUMULADO")
        print("==============================")
        print("Vitorias do jogador X: " + str(vitorias_x))
        print("Vitorias do jogador O: " + str(vitorias_o))
        print("Empates: " + str(empates))
        print("------------------------------")
        print("Total de partidas: " + str(total_partidas))
        print("==============================")

    # CONSULTAR ESTATISTICAS

    elif opcao == "4":

        print("==============================")
        print("   ESTATISTICAS DA SESSAO")
        print("==============================")
        print("Total de partidas: " + str(total_partidas))
        print("Vitorias de X: " + str(vitorias_x))
        print("Vitorias de O: " + str(vitorias_o))
        print("Empates: " + str(empates))
        print("------------------------------")
        print("Campeonatos iniciados: " + str(campeonatos_iniciados))
        print("Campeonatos vencidos por X: " + str(campeonatos_vencidos_x))
        print("Campeonatos vencidos por O: " + str(campeonatos_vencidos_o))
        print("Campeonatos empatados: " + str(campeonatos_empatados))
        print("==============================")

    # ENCERRAR PROGRAMA

    elif opcao == "5":

        print("Encerrando o jogo...")
        executando = False

    else:

        print("Opcao invalida! Tente novamente.")

    # GERENCIAMENTO DAS PARTIDAS

    while iniciar_partida == True:

        # REINICIAR TABULEIRO

        for i in range(3):
            for j in range(3):
                tabuleiro[i][j] = " "

        # INICIALIZAR CONTROLE DA PARTIDA

        resultado_partida = ""
        partida_concluida = False
        partida_contabilizada = False

        # VERIFICAR SE A INTEGRACAO ESTA PRONTA

        if integracao_pronta == False:

            print("==============================")
            print("Integracao com DEV 1 e DEV 2")
            print("ainda nao foi concluida.")
            print("A partida sera habilitada")
            print("apos a integracao dos codigos.")
            print("==============================")

            iniciar_partida = False

        else:

            if modo_campeonato == True and campeonato_contabilizado == False:

                campeonatos_iniciados = campeonatos_iniciados + 1
                campeonato_contabilizado = True

            # PONTO DE INTEGRACAO COM DEV 1 E DEV 2
            #
            # O codigo integrado devera:
            # 1. Utilizar a matriz tabuleiro.
            # 2. Exibir e atualizar o tabuleiro.
            # 3. Alternar os jogadores.
            # 4. Verificar vitoria ou empate.
            # 5. Definir resultado_partida como "X", "O" ou "E".
            # 6. Definir partida_concluida = True ao terminar.
            #
            # O bloco de jogo sera inserido aqui.
            # INTEGRACAO DO JOGO - DEV 1 E DEV 2

            jogador = "X"
            jogadas = 0

            while partida_concluida == False:

                # MOSTRAR TABULEIRO

                print("    1   2   3")

                for i in range(3):
                    print("  -------------")
                    print(str(i + 1) + " |", end="")

                    for j in range(3):
                        print(" " + tabuleiro[i][j] + " |", end="")

                    print()

                print("  -------------")
                print("Vez do jogador " + jogador + "!")

                if jogador == "X":
                    simbolo = "X"
                else:
                    simbolo = "O"

                # VALIDAR LINHA

                linha_valida = False

                while linha_valida == False:

                    entrada = input("Digite a linha (1 a 3): ")

                    for n in range(1, 4):
                        if entrada == str(n):
                            linha_valida = True

                    if linha_valida == False:
                        print("Linha invalida! Digite 1, 2 ou 3.")

                linha = int(entrada) - 1

                # VALIDAR COLUNA

                coluna_valida = False

                while coluna_valida == False:

                    entrada = input("Digite a coluna (1 a 3): ")

                    for n in range(1, 4):
                        if entrada == str(n):
                            coluna_valida = True

                    if coluna_valida == False:
                        print("Coluna invalida! Digite 1, 2 ou 3.")

                coluna = int(entrada) - 1

                # VERIFICAR POSICAO

                if tabuleiro[linha][coluna] == " ":

                    tabuleiro[linha][coluna] = simbolo
                    jogadas = jogadas + 1

                    # VERIFICAR VITORIA

                    venceu = False

                    if (tabuleiro[0][0] == simbolo and tabuleiro[0][1] == simbolo and tabuleiro[0][2] == simbolo) or (tabuleiro[1][0] == simbolo and tabuleiro[1][1] == simbolo and tabuleiro[1][2] == simbolo) or (tabuleiro[2][0] == simbolo and tabuleiro[2][1] == simbolo and tabuleiro[2][2] == simbolo) or (tabuleiro[0][0] == simbolo and tabuleiro[1][0] == simbolo and tabuleiro[2][0] == simbolo) or (tabuleiro[0][1] == simbolo and tabuleiro[1][1] == simbolo and tabuleiro[2][1] == simbolo) or (tabuleiro[0][2] == simbolo and tabuleiro[1][2] == simbolo and tabuleiro[2][2] == simbolo) or (tabuleiro[0][0] == simbolo and tabuleiro[1][1] == simbolo and tabuleiro[2][2] == simbolo) or (tabuleiro[0][2] == simbolo and tabuleiro[1][1] == simbolo and tabuleiro[2][0] == simbolo):

                        venceu = True
                        resultado_partida = jogador
                        partida_concluida = True

                    elif jogadas == 9:

                        resultado_partida = "E"
                        partida_concluida = True

                    else:

                        if jogador == "X":
                            jogador = "O"
                        else:
                            jogador = "X"

                else:

                    print("Essa casa ja esta ocupada!")
                    print("Escolha outra posicao.")

            # MOSTRAR TABULEIRO FINAL

            print("    1   2   3")

            for i in range(3):
                print("  -------------")
                print(str(i + 1) + " |", end="")

                for j in range(3):
                    print(" " + tabuleiro[i][j] + " |", end="")

                print()

            print("  -------------")


            # CONTABILIZAR RESULTADO DA PARTIDA

            if partida_concluida == True and partida_contabilizada == False:

                if resultado_partida == "X":

                    vitorias_x = vitorias_x + 1

                elif resultado_partida == "O":

                    vitorias_o = vitorias_o + 1

                elif resultado_partida == "E":

                    empates = empates + 1

                else:

                    print("Resultado de partida invalido.")
                    iniciar_partida = False

                if resultado_partida == "X" or resultado_partida == "O" or resultado_partida == "E":

                    total_partidas = total_partidas + 1
                    partida_contabilizada = True

                    print("==============================")
                    print("      RESULTADO DA PARTIDA")
                    print("==============================")

                    if resultado_partida == "X":
                        print("Jogador X venceu!")

                    elif resultado_partida == "O":
                        print("Jogador O venceu!")

                    else:
                        print("A partida terminou empatada.")

                    # CONTROLE DO CAMPEONATO

                    if modo_campeonato == True:

                        partidas_campeonato = partidas_campeonato + 1

                        if resultado_partida == "X":

                            vitorias_campeonato_x = vitorias_campeonato_x + 1

                        elif resultado_partida == "O":

                            vitorias_campeonato_o = vitorias_campeonato_o + 1

                        print("------------------------------")
                        print("PLACAR DO CAMPEONATO")
                        print("Vitorias de X: " + str(vitorias_campeonato_x))
                        print("Vitorias de O: " + str(vitorias_campeonato_o))
                        print("Partidas realizadas: " + str(partidas_campeonato))
                        print("==============================")

                        # VERIFICAR SE O CAMPEONATO TERMINOU

                        if vitorias_campeonato_x == 2 or vitorias_campeonato_o == 2 or partidas_campeonato == 3:

                            campeonato_ativo = False

                            campeonato_contabilizado = False

                            if vitorias_campeonato_x > vitorias_campeonato_o:

                                campeao = "X"
                                campeonatos_vencidos_x = campeonatos_vencidos_x + 1

                            elif vitorias_campeonato_o > vitorias_campeonato_x:

                                campeao = "O"
                                campeonatos_vencidos_o = campeonatos_vencidos_o + 1

                            else:

                                campeao = "E"
                                campeonatos_empatados = campeonatos_empatados + 1

                            print("==============================")
                            print("    FIM DO CAMPEONATO")
                            print("==============================")

                            if campeao == "X":

                                print("Jogador X venceu o campeonato!")

                            elif campeao == "O":

                                print("Jogador O venceu o campeonato!")

                            else:

                                print("O campeonato terminou empatado!")

                            iniciar_partida = False

                        else:

                            print("Preparando a proxima partida...")
                            iniciar_partida = True

                    # FINALIZAR PARTIDA NORMAL

                    else:

                        jogar_novamente = input("Deseja jogar novamente? (S/N): ")

                        if jogar_novamente == "S" or jogar_novamente == "s":

                            iniciar_partida = True

                        else:

                            iniciar_partida = False

            else:

                print("A partida nao foi finalizada corretamente.")
                print("Verifique a integracao com DEV 2.")
                iniciar_partida = False
