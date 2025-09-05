# Script: contador_de_vogais.py
# Descrição: Programa para contar vogais em uma string digitada pelo usuário
# Objetivo: Demonstrar manipulação de strings, loops e estruturas condicionais
# Exercício: 6. Crie um programa que percorra uma string digitada pelo usuário e conte quantas vogais ela possui.

# Seção 1: Entrada de dados
# Solicita ao usuário uma frase ou palavra para análise
# .lower() converte toda a string para minúsculas, facilitando a comparação
# Isso evita ter que verificar vogais maiúsculas e minúsculas separadamente
frase = input("Digite uma frase ou palavra: ").lower()

# Seção 2: Definição das vogais
# Cria uma string contendo todas as vogais minúsculas
# Esta string será usada para verificar cada letra da entrada
vogais = "aeiou"

# Seção 3: Inicialização do contador
# Variável acumuladora para contar o número de vogais encontradas
contador_vogais = 0

# Seção 4: Processamento - loop de contagem
# Percorre cada caractere da string digitada pelo usuário
for letra in frase:
    # Verificação de vogal
    # O operador 'in' verifica se a letra atual existe na string 'vogais'
    # Isso é mais eficiente que verificar cada vogal individualmente
    if letra in vogais:
        # Incrementa o contador quando encontra uma vogal
        # += 1 é equivalente a contador_vogais = contador_vogais + 1
        contador_vogais += 1
    # Caracteres que não são vogais (consoantes, números, espaços, pontuação) são ignorados

# Seção 5: Exibição dos resultados
# Exibe o total de vogais encontradas
print(f"\nAnálise da string: '{frase}'")
print(f"A string possui {contador_vogais} vogais.")

# Seção 6: Informações adicionais (opcional)
# Calcula e exibe estatísticas extras
comprimento = len(frase)
percentual_vogais = (contador_vogais / comprimento * 100) if comprimento > 0 else 0

print(f"\nEstatísticas:")
print(f"- Comprimento total: {comprimento} caracteres")
print(f"- Vogais encontradas: {contador_vogais}")
print(f"- Percentual de vogais: {percentual_vogais:.1f}%")

# Seção 7: Demonstração de vogais individuais (opcional)
print(f"\nDetalhamento por vogal:")
for vogal in vogais:
    quantidade = frase.count(vogal)
    if quantidade > 0:
        print(f"- Vogal '{vogal}': {quantidade} ocorrência(s)")

# Observações sobre o algoritmo:
print(f"\nObservações:")
print("- O programa ignora acentuação (á, é, í, ó, ú não são contados)")
print("- Espaços, números e símbolos não são considerados")
print("- A conversão para minúsculas garante case-insensitive counting")