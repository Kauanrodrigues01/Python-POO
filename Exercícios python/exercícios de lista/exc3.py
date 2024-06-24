# Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
def calcular_media(notas):
    soma_das_notas = sum(notas)
    media = (soma_das_notas / len(notas))
    print(media)
notas = list(map(int, input().split()))
calcular_media(notas)