# Lendo os valores de entrada
H = int(input())
M = int(input())
S = int(input())
T = int(input())
horario_original_segundos = 3600 * H + 60 * M + S
novo_horario_segundos = horario_original_segundos + T
novas_horas = novo_horario_segundos // 3600
novos_minutos = (novo_horario_segundos % 3600) // 60
novos_segundos = novo_horario_segundos % 60
print(novas_horas)
print(novos_minutos)
print(novos_segundos)