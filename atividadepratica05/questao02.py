def eh_palindromo(texto):
    texto_limpo = ""
    
    for char in texto.lower():
        if char.isalnum():  # ignora espaços e pontuação
            texto_limpo += char

    return texto_limpo == texto_limpo[::-1]


# Exemplo de uso
frase = input("Digite uma palavra ou frase: ")

if eh_palindromo(frase):
    print("Sim")
else:
    print("Não")