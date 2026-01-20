int(input("Digite sua idade: "))

if idade >= 0 and idade <= 12:
    categoria = "Criança"
elif idade <= 17:
    categoria = "Adolescente"
elif idade <= 59:
    categoria = "Adulto"
else:
    categoria = "Idoso"

print(f"Idade: {idade} anos")
print(f"Categoria: {categoria}")