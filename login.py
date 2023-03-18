# Dicionário de usuários e senhas
usuarios = {"usuario1": "senha1", "usuario2": "senha2", "usuario3": "senha3"}

# Função de login
def login():
    usuario = input("Digite o seu nome de usuário: ")
    senha = input("Digite a sua senha: ")

    if usuario in usuarios and usuarios[usuario] == senha:
        print("Login efetuado com sucesso!")
    else:
        print("Usuário ou senha incorretos.")

# Chamada da função de login
login()
