sec = int(input("Digite seu tempo em segundos: "))

horas = sec // 3600
sec = sec % 3600

minutos = sec // 60
sec = sec % 60

print("Seu tempo é de", horas, "hora", minutos, "minutos", sec, "segundos")