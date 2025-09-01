minha_tupla = (1, 2, 3, 4, 5)
print("Tupla original:", minha_tupla)

try:
    minha_tupla[0] = 10
except TypeError as e:
    print("\nErro ao tentar modificar a tupla:", e)
    print("Isso acontece porque tuplas são imutáveis - seus elementos não podem ser alterados após a criação")

nova_tupla = (10,) + minha_tupla[1:]
print("\nNova tupla criada:", nova_tupla)
print("Tupla original permanece inalterada:", minha_tupla)
