# classe salario
class salario:
    def __init__(self, base, bonus):
        self.base = base
        self.bonus = bonus

    def salario_anual(self):
        return (self.base*12)+self.bonus

# classe empregado


class empregado:
    def __init__(self, nome, idade, salario):
        self.nome = nome
        self.idade = idade
        self.salario_agregado = salario

    def salario_total(self):
        return self.salario_agregado.salario_anual()


Salario = salario(10000, 700)
# Passando o objeto Salario em vez de uma string
emp = empregado('musashi', 46, Salario)
print(emp.salario_total())
