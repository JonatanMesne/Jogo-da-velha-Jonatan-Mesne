#jogo da velha

placeholder = " "       #variável para preencher a matriz antes do jogo

def MostrarTabela(matriz):
    print("\n  1   2   3")
    for i in range(len(matriz)):
        print(f"{i + 1} {matriz[i][0]} | {matriz[i][1]} | {matriz[i][2]}")

def VerificarVitoria(matriz):
    MostrarTabela(tabela)
    for i in range(len(matriz)):
        if matriz[i][0] == matriz[i][1] == matriz[i][2] != placeholder:
            return True

    for i in range(len(matriz)):
        if matriz[0][i] == matriz[1][i] == matriz[2][i] != placeholder:
            return True

    if matriz[0][0] == matriz[1][1] == matriz[2][2] != placeholder:
        return True
    if matriz[0][2] == matriz[1][1] == matriz[2][0] != placeholder:
        return True
    return False


tabela = [[placeholder for _ in range(3)] for _ in range(3)]

#MostrarTabela(tabela)

jogador = True
vezes = 0

MostrarTabela(tabela)

while True:
    if vezes == 9:
        print("\n Empate!!! :(")
        break
    if jogador:
        print("\nJogador 1 (X):")
        linha = int(input("Escolha a linha (1-3): "))
        coluna = int(input("Escolha a coluna (1-3): "))

        if linha > 3 or linha < 1 or coluna > 3 or coluna < 1:  #conferir se o número de colunas ou linhas está dentro do permitido
            print("Célula inválida. Tente de novo!\n")
            continue

        if tabela[linha - 1][coluna - 1] != placeholder:
            print("Célula ja ocupada. Tente de novo!\n")
            continue

        tabela[linha - 1][coluna - 1] = "X"

        jogador = False
        vezes += 1
        if VerificarVitoria(tabela):
            print("\nJogador 1 (X) venceu!!! :)")
            break
    else:
        print("\nJogador 2 (O)")
        linha = int(input("Escolha a linha (1-3): "))
        coluna = int(input("Escolha a coluna (1-3): "))

        if linha > 3 or linha < 1 or coluna > 3 or coluna < 1:  #conferir se o número de colunas ou linhas está dentro do permitido
            print("Célula inválida. Tente de novo!\n")
            continue

        if tabela[linha - 1][coluna - 1] != placeholder:
            print("Célula ja ocupada. Tente de novo!\n")
            continue

        tabela[linha - 1][coluna - 1] = "O"

        jogador = True
        vezes += 1
        if VerificarVitoria(tabela):
            print("\nJogador 2 (O) venceu!!! :)")
            break