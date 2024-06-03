lista = [10, 2, 5, 7, 3, 6]
n = len(lista)
soma = 0
for i in range(n):
    if (lista[i] % 2 == 0):
        soma = soma+lista[i]
print(f'o somatorio dos elementos dos elementos pares da lista é : {soma}')
