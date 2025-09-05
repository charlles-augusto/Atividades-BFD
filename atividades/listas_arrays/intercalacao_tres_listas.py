A = []  # criando a primeira lista vazia
B = []  # criando a segunda lista vazia
C = []  # criando a terceira lista vazia

# Entrada de dados para as listas A, B e C
print("Digite 10 números inteiros para a lista A:")
for i in range(10):
    num = int(input(f'Digite o {i+1}º número inteiro para lista A: '))
    A.append(num)

print("\nDigite 10 números inteiros para a lista B:")
for i in range(10):
    num = int(input(f'Digite o {i+1}º número inteiro para lista B: '))
    B.append(num)

print("\nDigite 10 números inteiros para a lista C:")
for i in range(10):
    num = int(input(f'Digite o {i+1}º número inteiro para lista C: '))
    C.append(num)

# Criando a lista D com elementos intercalados das três listas
D = []

# Intercalando os elementos das três listas
for i in range(10):
    D.append(A[i])  # Adiciona elemento da lista A
    D.append(B[i])  # Adiciona elemento da lista B
    D.append(C[i])  # Adiciona elemento da lista C

# Exibindo os resultados
print("\nLista A:", A)
print("Lista B:", B)
print("Lista C:", C)
print("Lista D (intercalada):", D)