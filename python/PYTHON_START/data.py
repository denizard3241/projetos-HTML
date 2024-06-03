from sklearn.datasets import load_digits

# Carregar os dados
digits = load_digits()

# Informar a quantidade de dados
quantidade_dados = len(digits.data)
print("Quantidade de dados:", quantidade_dados)
