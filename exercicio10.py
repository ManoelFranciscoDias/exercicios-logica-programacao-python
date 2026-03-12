#entrada
tempo = float(input("Digite o tempo de duração do evento em segundos: "))

#processamento
hora = tempo // 3600
minuto = (tempo % 3600) // 60
segundo = tempo % 60

#saida
print("O evento durou", hora, "horas,", minuto, "minutos e", segundo, "segundos.")