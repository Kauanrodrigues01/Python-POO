# Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.
todos_numeros = []
pares = []
impares = []

for i in range(20):
    numero = int(input(f"Digite o {i+1}º número inteiro: "))
    todos_numeros.append(numero)
    
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

# Imprime os três vetores
print("Todos os números:", todos_numeros)
print("Números pares:", pares)
print("Números ímpares:", impares)
