def calcular_arvores(num_arvores, num_mudas_por_arvore, num_arvores_atingir):
    num_arvores_total = num_arvores
    contador_dias = 0
    while num_arvores_total < num_arvores_atingir:
        num_arvores_total += (num_arvores_total*num_mudas_por_arvore)
        contador_dias += 1
    print(contador_dias)


num_arvores = int(input())
num_mudas_por_arvore = int(input())
num_arvores_atingir = int(input())
calcular_arvores(num_arvores, num_mudas_por_arvore, num_arvores_atingir)