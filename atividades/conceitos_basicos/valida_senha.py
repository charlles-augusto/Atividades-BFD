# Script: valida_senha.py
# Descrição: Programa de validação de senha com loop de repetição
# Objetivo: Demonstrar uso de while loop para validação de entrada do usuário

# Define a senha correta como constante
# Esta é a senha pré-definida que o usuário deve acertar
SENHA_CORRETA = "python123"

# Inicializa a variável para armazenar a senha digitada pelo usuário
# Começa com string vazia para garantir que o loop execute pelo menos uma vez
senha_digitada = ""

# Estrutura de repetição while
# O loop continuará executando enquanto a senha digitada for diferente da correta
# Esta é uma técnica comum para validação de entrada
while senha_digitada != SENHA_CORRETA:
    # Solicita ao usuário que digite a senha
    # A função input() sempre retorna uma string
    senha_digitada = input("Digite a senha: ")
    
    # Estrutura condicional if para verificar a senha
    # Compara a senha digitada com a senha correta
    if senha_digitada != SENHA_CORRETA:
        # Feedback ao usuário quando a senha está incorreta
        # Isso ajuda o usuário a entender por que o programa não avançou
        print("Senha incorreta. Tente novamente.")
    # Note que não há else aqui - se a senha estiver correta, o loop simplesmente termina

# Este ponto só é alcançado quando senha_digitada == SENHA_CORRETA
# Isso significa que o usuário acertou a senha
print("Senha correta. Acesso concedido!")