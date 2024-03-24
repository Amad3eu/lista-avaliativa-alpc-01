# Solicita ao usuário informações sobre a viagem
tempo = float(input("Informe o tempo gasto na viagem (em horas): "))
velocidade_media = float(
    input("Informe a velocidade média durante a viagem (em km/h): ")
)

# Calcula a distância percorrida
distancia = tempo * velocidade_media

# Calcula a quantidade de litros utilizados (considerando 12 km por litro)
litros_usados = distancia / 12

# Exibe os resultados na tela
print(f"Distância percorrida: {distancia} km")
print(f"Litros de combustível utilizados: {litros_usados} litros")
