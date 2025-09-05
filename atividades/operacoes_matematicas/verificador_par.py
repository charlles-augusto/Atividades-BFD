def eh_par(numero):
    """
    Esta função recebe um número e retorna True se ele for par e False caso contrário.
    """
    # Verifica se o número é divisível por 2 (ou seja, se é par)
    return numero % 2 == 0

# Exemplos de como usar a função:
print(f"O número 10 é par? {eh_par(10)}")  # Vai mostrar: O número 10 é par? True
print(f"O número 7 é par? {eh_par(7)}")    # Vai mostrar: O número 7 é par? False
