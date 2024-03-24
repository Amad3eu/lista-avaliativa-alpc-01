import math

# Solicita ao usuário que informe o raio (R) e a altura (H) do tanque
R = float(input("Informe o raio da base do tanque (em metros): "))
H = float(input("Informe a altura do tanque (em metros): "))

# Calcula a área a ser pintada usando a fórmula (A = 2*p*R2 + 2*p*R*H)
area = 2 * math.pi * R**2 + 2 * math.pi * R * H

# Calcula a quantidade de galões de tinta necessária (considerando 3 metros quadrados por litro)
litros_tinta = area / 3
galoes_tinta = math.ceil(litros_tinta / 3.6)  # Arredonda para cima

# Calcula o custo total da tinta (considerando R$40,00 por galão de 3,6 litros)
custo_tinta = galoes_tinta * 40

# Exibe os resultados
print(f"Área a ser pintada: {area:.2f} metros quadrados")
print(f"Quantidade de galões de tinta necessária: {galoes_tinta}")
print(f"Custo total da tinta: R${custo_tinta:.2f}")
