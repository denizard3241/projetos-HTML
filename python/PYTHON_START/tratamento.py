x = int(input())
y = int(input())

if y != 0 and x != 0:
    x = x % y
    x = x % y
    y = y % x
    print(y)
else:
    print("Erro: Divisão por zero!")
