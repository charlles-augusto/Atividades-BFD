tabuleiro = [['[ ]' for _ in range(8)] for _ in range(8)]

pecas_brancas = ['tor', 'cav', 'bis', 'rai', 'rei', 'bis', 'cav', 'tor']
pecas_pretas = ['tor', 'cav', 'bis', 'rai', 'rei', 'bis', 'cav', 'tor']

tabuleiro[0] = pecas_pretas
tabuleiro[7] = pecas_brancas

tabuleiro[1] = ['pea' for _ in range(8)]
tabuleiro[6] = ['pea' for _ in range(8)]

for linha in tabuleiro:
    print(' '.join(linha))