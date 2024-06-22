def gerar_matriz(N, Q):
    matriz = [[0] * N for _ in range(N)]
    for i in range(N):
        linha = input().strip()
        for j in range(N):
            matriz[i][j] = int(linha[j])
            
    for i in range(N):
        for j in range(N):
            if matriz[i][j] == 1:
                vizinhos = 0
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        ni, nj = i + dx, j + dy
                        if 0 <= ni < N and 0 <= nj < N and matriz[ni][nj] == 1:
                            vizinhos += 1
                if vizinhos >= Q:
                    matriz[i][j] = 0
                    
    for linha in matriz:
        print("".join(map(str, linha)))

N, Q = map(int, input().split())
gerar_matriz(N, Q)
