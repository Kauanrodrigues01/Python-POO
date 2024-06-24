'''Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
a) "Telefonou para a vítima?"
b) "Esteve no local do crime?"
c) "Mora perto da vítima?"
d) "Devia para a vítima?"
e) "Já trabalhou com a vítima?" 

O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
'''


p1 = input(f'Telefonou para a vítima?(S/N)')
p2 = input(f'Esteve no local do crime?(S/N) ')
p3 = input(f'Mora perto da vítima?(S/N) ')
p4 = input(f'Devia para a vítima?(S/N) ')
p5 = input(f'Já trabalhou com a vítima?(S/N) ')

respostas = [p1,p2,p3,p4,p5]
respostas_positivas = 0

for resposta in respostas:
    if (resposta.strip().upper()) == 'S':
        respostas_positivas += 1

if respostas_positivas == 2:
    print(f'Você é SUSPEITO!')
elif 3 <= respostas_positivas <= 4:
    print(f'Você é CÚMPLICE')
else:
    print(f'Você é o ASSASINO!')