def verificar(E, D):
    if E > D:
        return (E + D)
    else:
        return (2 * (D - E))

dedos_esquerda = int(input())
dedos_direita = int(input())
resultado = verificar(dedos_esquerda, dedos_direita)
print(resultado)