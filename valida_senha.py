# 2. Crie um programa que peça uma senha ao usuário e só termine quando a senha correta "python123" for digitada.

senha_correta = "python123"
senha = input("Digite a senha: ")
while senha != senha_correta:
    senha = input("\nSenha incorreta!\nTente novamente: ")
print("Senha correta!")
