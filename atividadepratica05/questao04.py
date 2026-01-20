from datetime import date

# Entrada do usuário
ano = int(input("Digite o ano de nascimento: "))
mes = int(input("Digite o mês de nascimento: "))
dia = int(input("Digite o dia de nascimento: "))

data_nascimento = date(ano, mes, dia)
data_atual = date.today()

dias_vivo = (data_atual - data_nascimento).days

print(f"Você está vivo há aproximadamente {dias_vivo} dias.")