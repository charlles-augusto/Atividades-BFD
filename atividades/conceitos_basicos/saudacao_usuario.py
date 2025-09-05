# Script: saudacao_usuario.py
# Descrição: Demonstra o conceito de funções básicas em Python
# Objetivo: Criar uma função que recebe um nome e exibe uma saudação personalizada

# Define uma função chamada 'saudacao' que recebe um parâmetro 'nome'
# Parâmetro: nome (string) - o nome da pessoa a ser saudada
def saudacao(nome):
    """
    Função: saudacao
    Descrição: Recebe o nome de uma pessoa e imprime uma mensagem de boas-vindas
    Parâmetro:
        - nome: string contendo o nome do usuário
    Retorno: None (a função apenas imprime a mensagem)
    """
    # Utiliza f-string para formatar a mensagem com o nome fornecido
    # A f-string permite inserir variáveis diretamente na string usando chaves {}
    print(f"Olá, {nome}! Seja bem-vindo(a)!")

# Demonstração do uso da função
# Abaixo estão exemplos de como chamar a função saudacao com diferentes nomes

# Exemplo 1: Saudação para Ana
# A função será executada e imprimirá: "Olá, Ana! Seja bem-vindo(a)!"
saudacao("Ana")

# Exemplo 2: Saudação para Carlos  
# A função será executada e imprimirá: "Olá, Carlos! Seja bem-vindo(a)!"
saudacao("Carlos")