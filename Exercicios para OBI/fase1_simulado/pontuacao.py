def verificar_medalha(esportes, artes, ciencias):
    soma_atividades = (esportes*2) + (artes*3) + (ciencias*5)
    if soma_atividades >= 200:
        medalha = 'ouro'
    elif soma_atividades >= 150:
        medalha = 'prata'
    elif soma_atividades >=100:
        medalha = 'bronze'
    elif soma_atividades < 100:
        medalha = None
    return medalha

def exibir_medalha(medalha):
    if medalha == 'ouro':
        print('O')
    elif medalha == 'prata':
        print('S')
    elif medalha == 'bronze':
        print('B')
    else:
        print('N')

num_atv_esportes = int(input())
num_atv_artes = int(input())
num_atv_ciencias = int(input())
medalha = verificar_medalha(num_atv_esportes, num_atv_artes, num_atv_ciencias)
exibir_medalha(medalha)
