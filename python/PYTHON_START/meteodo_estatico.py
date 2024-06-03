from datetime import date


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def apartirAnoNascimento(cls, nome, ano_nascimento):
        idade = date.today().year - ano_nascimento
        return cls(nome, idade)

    @staticmethod
    def ehMaiorIdade(idade):
        return idade >= 18


# Criando as instâncias fora da classe
pessoa1 = Pessoa('maria', 26)
pessoa2 = Pessoa.apartirAnoNascimento('ana', 2006)

print(pessoa1.idade)
print(pessoa2.idade)

print(Pessoa.ehMaiorIdade(18))


class Conta:
    def __init__(self, numero, cpf, nomeTitular, saldo):
        self.numero = numero
        self.cpf = cpf
        self.nomeTitular = nomeTitular
        self.saldo = saldo


def main():
    c1 = Conta(1, 1, "Joao", 1000)  # Objeto sendo instanciado
    print(f"Nome do titular da conta: {c1.nomeTitular}")
    print(f"Número da conta: {c1.numero}")
    print(f"CPF do titular da conta: {c1.cpf}")
    print(f"Saldo da conta: {c1.saldo}")


# Quando um script python é executado, a variável reservada
# NAME referente a ele tem valor igual a "__main__".
# Nesse caso, a condição do IF a seguir será TRUE.
# Então o que está no corpo do IF será executado. No caso,
# é um chamado ao método main do script

if __name__ == "__main__":
    main()
