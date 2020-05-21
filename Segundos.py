segundos = int(input('Digite a quantidade de segundos: '))
horas = segundos // 3600
segundos_restante = segundos % 3600
minutos = segundos_restante// 60
segundos_restante = segundos_restante % 60

print(horas,'hr',minutos,'min',segundos_restante,'s')
