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

# DEV 1 - ETAPA 2
# Leitura e validacao da linha

valida = False

# Continua solicitando ate receber uma linha valida
while valida == False:

    entrada = input("Digite a linha (1 a 3): ")

    # Compara o texto digitado com 1, 2 e 3
    for n in range(1, 4):

        if entrada == str(n):
            valida = True

if valida == False:
    if entrada == "":
        print("Campo vazio! Informe a linha.")
    else:
        print("Linha invalida! Digite 1, 2 ou 3.")

# Converte somente depois da validacao
# O indice da matriz comeca em zero
linha = int(entrada) - 1

print("Linha escolhida:", linha + 1)

# Leitura e validacao da coluna

valida = False

# Continua solicitando ate receber uma coluna valida
while valida == False:

    entrada = input("Digite a coluna (1 a 3): ")

    # Verifica se a entrada corresponde a 1, 2 ou 3
    for n in range(1, 4):

        if entrada == str(n):
            valida = True

        if valida == False:
         if entrada == "":
          print("Campo vazio! Informe a coluna.")
    else:
        print("Coluna invalida! Digite 1, 2 ou 3.")
# Converte somente depois da validacao
coluna = int(entrada) - 1

print("Posicao selecionada:")
print("Linha:", linha + 1)
print("Coluna:", coluna + 1)
