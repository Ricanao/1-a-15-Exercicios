salario_fixo = float(input("Salário fixo: R$ "))
total_vendido = float(input("Total vendido: R$ "))

comissao = total_vendido * 0.04
salario_total = salario_fixo + comissao

comissao_fmt = f"{comissao:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
salario_total_fmt = f"{salario_total:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

print(f"Comissão: R$ {comissao_fmt}")
print(f"Salário total: R$ {salario_total_fmt}")
