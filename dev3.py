# PROJETO JOGO DA VELHA - DEV 3
# Etapa 1 - Menu principal
# Variaveis do placar acumulado
vitorias_x = 0
vitorias_o = 0
empates = 0
total_partidas = 0

# Variaveis das estatisticas
campeonatos_iniciados = 0
campeonatos_vencidos_x = 0
campeonatos_vencidos_o = 0
campeonatos_empatados = 0

# Variaveis do campeonato Melhor de 3
partidas_campeonato = 0
vitorias_campeonato_x = 0
vitorias_campeonato_o = 0
campeonato_ativo = False
campeao = ""

executando = True

while executando == True:

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

    if opcao == "1":
        print("Opcao de iniciar partida selecionada.")

    elif opcao == "2":
        print("Opcao de campeonato selecionada.")

    elif opcao == "3":
        print("Opcao de placar selecionada.")

    elif opcao == "4":
        print("Opcao de estatisticas selecionada.")

    elif opcao == "5":
        print("Encerrando o jogo...")
        executando = False

    else:
        print("Opcao invalida! Tente novamente.")