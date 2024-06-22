def colorir_fita(N, fita):
    distancia = [float('inf')] * N

    for num in range(N):
        if fita[num] == 0:
            distancia[num] == 0

    ultimo_zero = -1
    for num in range(N):
        if fita[num] == 0:
            ultimo_zero = num
        elif ultimo_zero != -1:
            distancia[num] = min(distancia[num], num - ultimo_zero)

    ultimo_zero = -1
    for num in range(N-1, -1, -1):
        if fita[num] == 0:
            ultimo_zero = num
        elif ultimo_zero != -1:
            distancia[num] = min(distancia[num], ultimo_zero - num)

    for num in range(N):
        if distancia[num] != float('inf'):
            fita[num] = min(distancia[num], 9)
    
    return fita
            


num_quadrados = int(input())
fita = list(map(int, input().strip().split()))
resultado = colorir_fita(num_quadrados, fita)
print(resultado)