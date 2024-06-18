texto = input().strip()
palavras = texto.split()
letras = list(input().strip())

contagem_palavras = 0
for palavra in palavras:
    for letra in letras:
        if letra in palavra:
            contagem_palavras += 1
            break

print(contagem_palavras)