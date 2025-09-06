# Inicializa um tabuleiro de xadrez 8x8 com casas vazias representadas por '[ ]'
tabuleiro = [['[ ]' for _ in range(8)] for _ in range(8)]

# Define as peças brancas na ordem inicial do xadrez (torre, cavalo, bispo, rainha, rei, bispo, cavalo, torre)
pecas_brancas = ['tor', 'cav', 'bis', 'rai', 'rei', 'bis', 'cav', 'tor']
# Define as peças pretas na mesma ordem
pecas_pretas = ['tor', 'cav', 'bis', 'rai', 'rei', 'bis', 'cav', 'tor']

# Coloca as peças pretas na primeira linha (índice 0) do tabuleiro
tabuleiro[0] = pecas_pretas
# Coloca as peças brancas na última linha (índice 7) do tabuleiro
tabuleiro[7] = pecas_brancas

# Coloca os peões pretos na segunda linha (índice 1) do tabuleiro
tabuleiro[1] = ['pea' for _ in range(8)]
# Coloca os peões brancos na penúltima linha (índice 6) do tabuleiro
tabuleiro[6] = ['pea' for _ in range(8)]

# Itera sobre cada linha do tabuleiro
for linha in tabuleiro:
    # Imprime a linha, unindo os elementos com um espaço para melhor visualização
    print(' '.join(linha))