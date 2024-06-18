# Forma complexa
def nota_corte(num, notas):
    min_aprovados = num[1]
    notas.sort(reverse=True)
    nota_corte = []
    for i in range(min_aprovados):
        nota_corte.append(notas[i])
    print(min(nota_corte))

num_candidados_num_min_aprovados = list(map(int, input().split()))
notas = list(map(int, input().split()))
nota_corte(num_candidados_num_min_aprovados, notas)


# Forma simplificada
def nota_corte(num, notas):
    min_aprovados = num[1]
    notas.sort(reverse=True)
    nota_corte = notas[min_aprovados - 1]
    print(nota_corte)

num_candidados_num_min_aprovados = list(map(int, input().split()))
notas = list(map(int, input().split()))
nota_corte(num_candidados_num_min_aprovados, notas)