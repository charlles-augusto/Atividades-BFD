# 6. Crie um programa que percorra uma string digitada pelo usuário e conte quantas vogais ela possui.

# Pede ao usuário para digitar uma frase ou palavra
frase = input("Digite uma frase ou palavra: ").lower() # Converte para minúsculas para facilitar a contagem

# Define as vogais
vogais = "aeiou"

# Inicializa o contador de vogais
contador_vogais = 0

# Loop que percorre cada letra na frase
for letra in frase:
    # Verifica se a letra atual está na string de vogais
    if letra in vogais:
        # Se for uma vogal, incrementa o contador
        contador_vogais += 1

# Imprime o resultado final
print(f"A string possui {contador_vogais} vogais.")