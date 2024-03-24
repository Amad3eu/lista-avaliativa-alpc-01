# Solicita ao usuário que informe a hora, o minuto e o segundo
hora = int(input("Informe a hora: "))
minuto = int(input("Informe o minuto: "))
segundo = int(input("Informe o segundo: "))

# Calcula o total de segundos passados desde a meia-noite
total_segundos = hora * 3600 + minuto * 60 + segundo

# Exibe o resultado na tela
print(f"Total de segundos passados desde a meia-noite: {total_segundos} segundos")
