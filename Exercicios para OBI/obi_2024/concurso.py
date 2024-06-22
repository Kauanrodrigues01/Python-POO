def verificar_nota_corte(x,nota_participantes):
    nota_de_corte = []
    nota_participantes.sort(reverse=True)
    num_min_participantes_aprovados = (x[1] - 1)
    while num_min_participantes_aprovados >= 0:
        nota_de_corte.append(nota_participantes[num_min_participantes_aprovados])  
        num_min_participantes_aprovados -= 1  
    if len(nota_de_corte) == 1:
        print(nota_de_corte[0])
    else:
        print(nota_de_corte[0])
x = list(map(int, input().split()))
nota_participantes = list(map(int, input().split()))
verificar_nota_corte(x,nota_participantes)

