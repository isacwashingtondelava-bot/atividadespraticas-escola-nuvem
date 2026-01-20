# Verificador de Senha

senha = input("Digite a senha: ")

tem_numero = any(char.isdigit() for char in senha)

if len(senha) >= 8 and tem_numero:
    print("Senha válida ✔")
else:
    print("Senha inválida ❌")
    print("A senha deve ter pelo menos 8 caracteres e conter um número.")