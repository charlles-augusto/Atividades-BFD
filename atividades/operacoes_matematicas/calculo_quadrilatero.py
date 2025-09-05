# Script: calculo_quadrilatero.py
# Descrição: Programa para calcular a área de N quadriláteros (quadrados)
# Objetivo: Demonstrar uso de loops com entrada do usuário e cálculos matemáticos
# Fórmula utilizada: Área = lado × lado = lado²

# Entrada do usuário: número de quadriláteros a calcular
# int() converte a entrada string para número inteiro
n = int(input("Digite o número de quadriláteros: "))

# Validação básica (opcional):
if n <= 0:
    print("Por favor, digite um número positivo de quadriláteros.")
else:
    # Loop principal: processa cada quadrilátero
    # range(n) gera números de 0 até n-1
    for i in range(n):
        # Entrada do comprimento do lado para cada quadrilátero
        # float() converte a entrada string para número decimal
        lado = float(input(f"Digite o comprimento do lado do quadrilátero {i+1}: "))
        
        # Validação do lado (deve ser positivo)
        if lado <= 0:
            print("O lado deve ser um valor positivo!")
            continue  # Pula para o próximo quadrilátero
        
        # Cálculo da área do quadrado
        # Um quadrilátero com todos os lados iguais é um quadrado
        area = lado * lado
        
        # Exibição do resultado formatado
        print(f"Área do quadrilátero {i+1}: {area}")
        
        # Informações adicionais (opcional):
        print(f"  - Lado: {lado} unidades")
        print(f"  - Área: {area} unidades²")
        print("-" * 30)  # Separador visual

# Observações sobre o código:
# - Este programa calcula áreas de quadrados (todos os lados iguais)
# - Para quadriláteros genéricos, seria necessário solicitar base e altura
# - A área é sempre expressa em unidades quadradas (m², cm², etc.)
