def resultado_brincadeira(E, D):
    if E > D:
        resultado = E + D
    else:
        resultado = 2 * (D - E)
    return resultado

E = int(input().strip())
D = int(input().strip())
resposta = resultado_brincadeira(E, D)
print(resposta)