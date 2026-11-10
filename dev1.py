# DEV 1 - Jogo da Velha
# ETAPA 1: Criacao do tabuleiro

# Matriz com tres linhas e tres colunas
tabuleiro = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

print("Tabuleiro 3x3 criado.")

# Exibe os numeros das colunas
print("    1   2   3")

# O primeiro for percorre as linhas
for i in range(3):
    print("  -------------")
    print(str(i + 1) + " |", end="")

    # O segundo for percorre as colunas
    for j in range(3):
        print(" " + tabuleiro[i][j] + " |", end="")

    print()

print("  -------------")
