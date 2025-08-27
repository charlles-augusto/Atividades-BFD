# 1. Faça um programa que peça números ao usuário até que ele digite 0. Ao final, mostre a soma de todos os números digitados.

# Inicializa a soma e a variável para o número
soma = 0
numero = -1 # Garante que o loop será executado pelo menos uma vez

# Loop que continua enquanto o número digitado não for 0
while numero != 0:
    try:
        # Pede ao usuário para digitar um número
        numero = int(input("Digite um número (digite 0 para encerrar): "))
        # Adiciona o número à soma total
        soma += numero
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")

# Mostra o resultado final
print(f"A soma de todos os números digitados é: {soma}")