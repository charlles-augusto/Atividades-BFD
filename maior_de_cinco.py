# 5. Escreva um programa que leia 5 números e mostre o maior deles.

# Inicializa a variável para armazenar o maior número com um valor muito baixo
maior_numero = float('-inf')

# Loop para ler 5 números
for i in range(5):
    try:
        # Pede ao usuário para digitar um número
        numero = float(input(f"Digite o {i+1}º número: "))
        
        # Compara o número digitado com o maior_numero atual
        if numero > maior_numero:
            # Se for maior, atualiza a variável maior_numero
            maior_numero = numero
    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")

# Mostra o resultado final
print(f"O maior número digitado é: {maior_numero}")