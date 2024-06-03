# Solicita ao usuário que forneça seu peso em kg
peso = float(input("Digite o seu peso em kg: "))

# Solicita ao usuário que forneça sua altura em metros
altura = float(input("Digite a sua altura em metros: "))

# Calcula o IMC utilizando a fórmula: IMC = peso / (altura ** 2)
imc = peso / (altura ** 2)

# Exibe o resultado para o usuário
print("O seu IMC é:", imc)
