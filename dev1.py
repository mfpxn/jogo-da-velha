
# DEV 1 - Jogo da Velha
# ETAPA 1: Criacao e exibicao do tabuleiro

# Matriz 3x3 declarada explicitamente
tabuleiro = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

print("Tabuleiro 3x3 criado.")

# Exibicao do tabuleiro com for aninhado
print("    1   2   3")

for i in range(3):
    print("  -------------")
    print(str(i + 1) + " |", end="")

    for j in range(3):
        print(" " + tabuleiro[i][j] + " |", end="")

    print()

print("  -------------")


# ETAPA 2: Leitura e validacao das entradas
# ETAPA 3: Verificacao de casas ocupadas

jogada_concluida = False

# Repete a escolha enquanto a casa nao estiver livre
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

    # Conversao apos validar
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

    # Conversao apos validar
    coluna = int(entrada) - 1

    # Verifica se a casa esta disponivel
    if tabuleiro[linha][coluna] == " ":
        jogada_concluida = True
        print("Casa disponivel! Jogada aceita.")

    else:
        print("Casa ocupada! Escolha outra posicao.")
