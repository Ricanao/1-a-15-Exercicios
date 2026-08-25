A = int(input("A: "))
B = int(input("B: "))

auxiliar = A
A = B
B = auxiliar

print("Depois da troca:")
print(f"A: {A}")
print(f"B: {B}")