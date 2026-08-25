preco = float(input("Preço: R$ "))

desconto = preco * 0.10
preco_final = preco - desconto

print(f"Desconto: R$ {desconto:.2f}".replace(".", ","))
print(f"Preço final: R$ {preco_final:.2f}".replace(".", ","))