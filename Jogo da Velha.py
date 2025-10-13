# Jogo da Velha em Python (Tic-Tac-Toe)
# Desenvolvido para dois jogadores - X e O
# Autores: (adicione os nomes do grupo aqui)

# Função para exibir o tabuleiro
def exibir_tabuleiro(tabuleiro):
    print("\n")
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-" * 9)
    print("\n")

# Função para verificar se há um vencedor
def verificar_vencedor(tabuleiro, jogador):
    # Verifica linhas
    for linha in tabuleiro:
        if all(celula == jogador for celula in linha):
            return True
    # Verifica colunas
    for c in range(3):
        if all(tabuleiro[l][c] == jogador for l in range(3)):
            return True
    # Verifica diagonais
    if all(tabuleiro[i][i] == jogador for i in range(3)):
        return True
    if all(tabuleiro[i][2 - i] == jogador for i in range(3)):
        return True
    return False

# Função para verificar empate
def verificar_empate(tabuleiro):
    for linha in tabuleiro:
        if " " in linha:
            return False
    return True

# Função para verificar se a jogada é válida
def jogada_valida(tabuleiro, linha, coluna):
    return 0 <= linha < 3 and 0 <= coluna < 3 and tabuleiro[linha][coluna] == " "

# Função principal do jogo
def jogar():
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
    jogador_atual = "X"

    print("===== JOGO DA VELHA =====")
    print("Jogadores: X e O")
    exibir_tabuleiro(tabuleiro)

    while True:
        print(f"Vez do jogador {jogador_atual}")
        try:
            linha = int(input("Escolha a linha (0, 1, 2): "))
            coluna = int(input("Escolha a coluna (0, 1, 2): "))
        except ValueError:
            print("Entrada invalida! Digite apenas numeros 0, 1 ou 2.")
            continue

        if jogada_valida(tabuleiro, linha, coluna):
            tabuleiro[linha][coluna] = jogador_atual
            exibir_tabuleiro(tabuleiro)

            if verificar_vencedor(tabuleiro, jogador_atual):
                print(f"Jogador {jogador_atual} venceu!")
                break

            if verificar_empate(tabuleiro):
                print("O jogo terminou em empate!")
                break

            jogador_atual = "O" if jogador_atual == "X" else "X"
        else:
            print("Jogada invalida! Escolha outra posicao.")

# Execução
if __name__ == "__main__":
    jogar()
