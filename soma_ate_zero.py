soma = 0
numero = -1

while numero != 0:
    numero = int(input("Digite um número inteiro: "))
    soma += numero
    print(f"A soma dos números é: {soma}")
    if soma == 0:
        print("A soma atingiu zero. Encerrando o programa.")
        break