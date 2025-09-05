# Script: calculo_media.py
# Descrição: Função para calcular a média aritmética de uma lista de números
# Objetivo: Demonstrar cálculo estatístico básico com tratamento de casos especiais

# Definição da função calcular_media
# Parâmetro: lista_de_numeros (list) - lista contendo números (int ou float)
def calcular_media(lista_de_numeros):
    """
    Função: calcular_media
    
    Descrição: Calcula a média aritmética de uma lista de números.
    
    Parâmetros:
        - lista_de_numeros: lista contendo números inteiros ou decimais
    
    Retorno:
        - float: média dos números na lista
        - int: 0 (zero) se a lista estiver vazia (prevenção de divisão por zero)
    
    Exemplo:
        calcular_media([10, 20, 30]) retorna 20.0
        calcular_media([]) retorna 0
    """
    
    # Validação de entrada: verifica se a lista está vazia
    # 'if not lista_de_numeros' é equivalente a 'if len(lista_de_numeros) == 0'
    if not lista_de_numeros:
        # Retorna 0 para evitar erro de divisão por zero
        # Isso torna a função mais robusta
        return 0
    
    # Cálculo da soma total dos elementos
    # sum() é uma função built-in que soma todos os elementos da lista
    soma_total = sum(lista_de_numeros)
    
    # Contagem de elementos na lista
    # len() retorna o número de elementos na lista
    quantidade = len(lista_de_numeros)
    
    # Cálculo da média aritmética
    # Divide a soma total pela quantidade de elementos
    return soma_total / quantidade

# Demonstração do uso da função
# Cria uma lista de exemplo com números inteiros
numeros = [10, 20, 30, 40, 50]

# Chama a função calcular_media com a lista de números
media = calcular_media(numeros)

# Exibe o resultado formatado
print(f"Lista de números: {numeros}")
print(f"A média da lista é: {media}")  # Saída esperada: A média da lista é: 30.0

# Testes adicionais para demonstrar robustez:
print(f"Média de lista vazia: {calcular_media([])}")  # Saída: 0
print(f"Média de [100]: {calcular_media([100])}")  # Saída: 100.0