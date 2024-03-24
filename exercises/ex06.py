# Solicita ao usuário que informe o valor
valor = float(input("Digite o valor a ser reajustado: "))

# Calcula o reajuste de 5%
reajuste = valor * 0.05

# Calcula o novo valor com o reajuste
novo_valor = valor + reajuste

# Imprime o resultado na tela
print(f"O valor reajustado em 5% é: R${novo_valor:.2f}")
