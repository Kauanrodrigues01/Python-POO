# Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.

def calcular_media(notas_alunos):
    medias = []
    for aluno_nota in notas_alunos:
        media = sum(aluno_nota) / len(aluno_nota)
        medias.append(media)

    return medias

notas_alunos = []
for i in range(4):
    aluno = list(map(int, input(f'Digite as 4 notas do aluno {i+1}:').split()))
    notas_alunos.append(aluno)

medias = calcular_media(notas_alunos)
for i in range(len(medias)):
    print(f'Média do aluno {i+1}: {medias[i]}')