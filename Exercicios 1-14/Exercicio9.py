salario_atual = float(input("Salário atual: R$ "))

aumento = salario_atual * 0.15
novo_salario = salario_atual + aumento

aumento_formatado = f"{aumento:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
novo_salario_formatado = f"{novo_salario:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

print(f"Aumento: R$ {aumento_formatado}")
print(f"Novo salário: R$ {novo_salario_formatado}")