num_consultas = int(input())
consultas = list(map(int, input().split()))
estoque = []
for consulta in consultas:
    if consulta not in estoque:
        estoque.append(consulta)
        estoque.append(consulta) 
print(len(estoque))