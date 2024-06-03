# Solicita ao usuário que insira a média do aluno como um número real
media = float(input("Digite a média do aluno: "))

if media >= 7.0:
    situacao = "aprovado"
elif media >= 5.0:  # Verifica se a média está entre 5.0 e 7.0
    situacao = "em recuperação"
else:
    situacao = "reprovado"

print(f'O estudante está: {situacao}')
