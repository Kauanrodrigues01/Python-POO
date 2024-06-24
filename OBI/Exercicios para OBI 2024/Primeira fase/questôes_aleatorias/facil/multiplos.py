def verificar_multiplos(numeros):
    multiplos_de_2 = 0
    multiplos_de_3 = 0
    multiplos_de_4 = 0
    for num in numeros:
        if num%2 == 0:
            multiplos_de_2 += 1
        if num%3 == 0:
            multiplos_de_3 += 1
        if num%4 == 0:
            multiplos_de_4 += 1
    
    print(multiplos_de_2)
    print(multiplos_de_3)
    print(multiplos_de_4)



qntd_num = int(input())
numeros = []
for i in range(qntd_num):
    num = int(input())
    numeros.append(num)
    
verificar_multiplos(numeros)