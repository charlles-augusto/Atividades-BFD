# 4. Faça um programa que mostre todos os números pares de 1 a 20.

# Loop que percorre os números de 1 a 20
for numero in range(1, 21):
    # Verifica se o número é par (o resto da divisão por 2 é 0)
    if numero % 2 == 0:
        # Imprime o número
        print(numero)
    else:
        print(f"{numero} é ímpar.")