# DEV 1 - Jogo da Velha (UNINASSAU)
# Responsabilidades: criar e mostrar o tabuleiro,
# ler e validar uma jogada.

# Matriz 3x3, declarada linha por linha.
tabuleiro = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

# SOMENTE PARA TESTAR O DEV 1.
# Na integracao final, retirar esta linha:
# o DEV 2 definira o simbolo.
simbolo = "X"

# Exibe os numeros das colunas e percorre
# a matriz com dois for.
print("    1   2   3")

for i in range(3):
    print("  -------------")
    print(str(i + 1) + " |", end="")

    for j in range(3):
        print(" " + tabuleiro[i][j] + " |", end="")

    print()

print("  -------------")

# A jogada so termina quando a linha
# e a coluna forem validas e a casa vazia.
jogada_concluida = False

while jogada_concluida == False:

    print("Vez do jogador " + simbolo + "!")

    # Validacao da linha.
    valida = False

    while valida == False:
        entrada = input("Digite a linha (1 a 3): ")

        for n in range(1, 4):
            if entrada == str(n):
                valida = True

        if valida == False:
            print("Linha invalida! Digite 1, 2 ou 3.")

    # Converte apenas depois da validacao.
    linha = int(entrada) - 1

    # Validacao da coluna.
    valida = False

    while valida == False:
        entrada = input("Digite a coluna (1 a 3): ")

        for n in range(1, 4):
            if entrada == str(n):
                valida = True

        if valida == False:
            print("Coluna invalida! Digite 1, 2 ou 3.")

    # Converte apenas depois da validacao.
    coluna = int(entrada) - 1

    # Verifica se a posicao esta vazia.
    if tabuleiro[linha][coluna] == " ":

        tabuleiro[linha][coluna] = simbolo
        jogada_concluida = True

        print("Jogada realizada!")

    else:
        print("Essa casa ja esta ocupada.")
        print("Escolha outra posicao.")

# Mostra o tabuleiro atualizado.
print("    1   2   3")

for i in range(3):
    print("  -------------")
    print(str(i + 1) + " |", end="")

    for j in range(3):
        print(" " + tabuleiro[i][j] + " |", end="")

    print()

print("  -------------")
