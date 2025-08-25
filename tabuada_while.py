# 3. Escreva um programa que mostre a tabuada de um número escolhido pelo usuário, de 1 até 10, usando while.

# Pede ao usuário para escolher um número para a tabuada
try:
    numero = int(input("Digite o número para ver a tabuada: "))

    # Inicializa o contador para o loop
    contador = 1

    # Loop que vai de 1 a 10
    while contador <= 10:
        # Calcula o resultado da multiplicação
        resultado = numero * contador
        # Imprime a linha da tabuada
        print(f"{numero} x {contador} = {resultado}")
        # Incrementa o contador
        contador += 1
except ValueError:
    print("Entrada inválida. Por favor, digite um número inteiro.")