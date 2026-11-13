
# DEV 1 - Jogo da Velha
# ETAPA 1: Criacao e exibicao do tabuleiro

tabuleiro = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

# Apenas para teste independente do DEV 1.
# Na integracao, o DEV 2 definira o simbolo.
simbolo = "X"

print("Tabuleiro 3x3 criado.")
print("    1   2   3")

# Percorre as linhas e colunas com for aninhado
for i in range(3):
    print("  -------------")
    print(str(i + 1) + " |", end="")

    for j in range(3):
        print(" " + tabuleiro[i][j] + " |", end="")

    print()

print("  -------------")


# ETAPA 2: Leitura e validacao das entradas
# ETAPA 3: Impedir casas ocupadas e atualizar a matriz

jogada_concluida = False

# Repete ate conseguir realizar uma jogada valida
while jogada_concluida == False:

    # Validacao da linha
    valida = False

    while valida == False:
        entrada = input("Digite a linha (1 a 3): ")

        for n in range(1, 4):
            if entrada == str(n):
                valida = True

        if valida == False:
            if entrada == "":
                print("Campo vazio! Informe a linha.")
            else:
                print("Linha invalida! Digite 1, 2 ou 3.")

    # Converte apenas depois da validacao
    linha = int(entrada) - 1

    # Validacao da coluna
    valida = False

    while valida == False:
        entrada = input("Digite a coluna (1 a 3): ")

        for n in range(1, 4):
            if entrada == str(n):
                valida = True

        if valida == False:
            if entrada == "":
                print("Campo vazio! Informe a coluna.")
            else:
                print("Coluna invalida! Digite 1, 2 ou 3.")

    # Converte apenas depois da validacao
    coluna = int(entrada) - 1

    # Verifica se a casa esta vazia
    # Este bloco precisa ficar DENTRO do while
    if tabuleiro[linha][coluna] == " ":
        tabuleiro[linha][coluna] = simbolo
        jogada_concluida = True
        print("Jogada realizada!")
    else:
        print("Casa ocupada! Escolha outra posicao.")


# Atualizar a exibicao depois da jogada
print("    1   2   3")

for i in range(3):
    print("  -------------")
    print(str(i + 1) + " |", end="")

    for j in range(3):
        print(" " + tabuleiro[i][j] + " |", end="")

    print()

print("  -------------")
