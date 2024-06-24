def risada_engracada(risada):
    vogais = ['a', 'e', 'i', 'o', 'u']
    risada = [letra for letra in risada if letra in vogais]

    if risada == risada[::-1]:
        return 'S'
    else:
        return 'N'
risada = list(input())
resultado = risada_engracada(risada)
print(resultado)