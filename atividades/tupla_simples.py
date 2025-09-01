cores = ["vermelho", "verde", "azul", "amarelo", "roxo"]
if "azul" in cores:
    print("A cor azul está presente na lista")
else:
    print("A cor azul não está presente na lista")

print(f"Primeira cor: {cores[0]}")
print(f"Segunda cor: {cores[1]}")
print(f"Terceira cor: {cores[2]}")
print(f"Quarta cor: {cores[3]}")
print(f"Quinta cor: {cores[4]}")

print(f"Última cor usando índice negativo: {cores[-1]}")

cores = tuple(cores)

try:
    cores[0] = "preto"
except TypeError as e:
    print("\nErro ao tentar modificar a tupla:")
    print(e)
