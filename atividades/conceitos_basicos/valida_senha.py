# 2. Crie um programa que peça uma senha ao usuário e só termine quando a senha correta "python123" for digitada.

# Define a senha correta
senha_correta = "python123"

# Inicializa a variável para a senha digitada pelo usuário
senha_digitada = ""

# Loop que continua enquanto a senha digitada for diferente da senha correta
while senha_digitada != senha_correta:
    # Pede ao usuário para digitar a senha
    senha_digitada = input("Digite a senha: ")

    # Verifica se a senha está incorreta e avisa o usuário
    if senha_digitada != senha_correta:
        print("Senha incorreta. Tente novamente.")

# Se o loop terminou, a senha está correta
print("Senha correta. Acesso concedido!")