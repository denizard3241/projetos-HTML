lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 13, 21, 50, 340, 899]


def fTesteParidade(x): return x % 2 == 0


print(f"teste de fTesteParidade(5) = {fTesteParidade(5)}")

pares = list(filter(fTesteParidade, lista))

print(f"lista de números pares = {pares}")
