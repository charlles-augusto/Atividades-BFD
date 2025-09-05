# Script: calculo_soma.py
# Descrição: Função simples para somar dois números
# Objetivo: Introduzir conceitos básicos de funções em Python
# Exercício: 7. Crie uma função que receba dois números e retorne a soma deles.

# Definição da função somar
# Parâmetros: num1 e num2 (podem ser int ou float)
# Retorno: soma dos dois números
# Tipo de retorno: mantém o tipo dos parâmetros de entrada
def somar(num1, num2):
    """
    Função: somar
    
    Descrição: Recebe dois números e retorna a soma deles.
    
    Parâmetros:
        - num1: primeiro número (int ou float)
        - num2: segundo número (int ou float)
    
    Retorno:
        - int ou float: soma dos dois números
    
    Exemplos de uso:
        somar(5, 10) retorna 15
        somar(3.5, 2.5) retorna 6.0
        somar(-5, 8) retorna 3
    
    Notas:
        - Aceita números positivos e negativos
        - Mantém o tipo dos números de entrada
        - Não faz validação de tipos (confia nos parâmetros)
    """
    
    # Operação de soma básica
    # O operador + funciona para números inteiros e decimais
    return num1 + num2

# Demonstração do uso da função
# Criando variáveis de exemplo
a = 5
b = 10

# Chamando a função somar com os valores de exemplo
resultado = somar(a, b)

# Exibição do resultado formatado
print(f"Exemplo básico:")
print(f"Primeiro número: {a}")
print(f"Segundo número: {b}")
print(f"A soma é: {resultado}")  # Saída esperada: A soma é: 15

# Testes adicionais para demonstrar versatilidade:
print(f"\nTestes adicionais:")
print(f"Soma de decimais: {somar(3.5, 2.5)}")
print(f"Soma com negativos: {somar(-5, 8)}")
print(f"Soma de zeros: {somar(0, 0)}")
print(f"Soma de grandes números: {somar(1000000, 2000000)}")

# Observações sobre a função:
# - É uma função pura: sempre retorna o mesmo resultado para os mesmos parâmetros
# - Não tem efeitos colaterais
# - É simples e direta, ideal para demonstrar conceitos básicos