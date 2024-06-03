def calcular_gordura_corporal(peso, altura):
    # Calcula o IMC (Índice de Massa Corporal)
    imc = peso / (altura ** 2)

    # Estima a porcentagem de gordura corporal com base no IMC
    # A fórmula usada aqui é apenas uma estimativa e pode não ser precisa para todas as pessoas
    porcentagem_gordura = (1.2 * imc) + (0.23 * 30) - 10.8 - 5.4

    return porcentagem_gordura


# Solicita ao usuário que forneça seu peso em kg
peso = float(input("Digite o seu peso em kg: "))

# Solicita ao usuário que forneça sua altura em metros
altura = float(input("Digite a sua altura em metros: "))

# Calcula a porcentagem de gordura corporal
gordura_corporal = calcular_gordura_corporal(peso, altura)

# Exibe o resultado para o usuário
print("A sua porcentagem de gordura corporal é de:", gordura_corporal, "%")
