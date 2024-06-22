# Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

def calcular_consoantes(vetor):
    vogais = ['a', 'e', 'i', 'o', 'u']
    quant_consoantes = 0
    for letra in vetor:
        if letra not in vogais:
            quant_consoantes += 1
        if letra in vogais:
            vetor.remove(letra)

    print(f'quantidade de consoantes: {quant_consoantes}')
    print(f'as consoantes: {''.join(vetor)}')


vetor = list(input())
calcular_consoantes(vetor)