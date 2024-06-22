# Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
vetores = []

for i in range(10):
    vetores.append(i+1)

vetores.reverse()
print(vetores)
for vetor in vetores:
    print(vetor)