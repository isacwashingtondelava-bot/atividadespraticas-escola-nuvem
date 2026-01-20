import random
import string

# Entrada do usuário
tamanho = int(input("Digite o tamanho da senha: "))

# Conjunto de caracteres
caracteres = string.ascii_letters + string.digits + string.punctuation

# Geração da senha
senha = "".join(random.choice(caracteres) for _ in range(tamanho))

print(f"Senha gerada: {senha}")