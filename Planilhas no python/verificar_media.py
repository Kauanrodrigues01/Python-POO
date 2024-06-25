import openpyxl

def pegar_notas(pagina, posicao_materia, posicao_nota):
    '''
    Extrai as notas de uma planilha do Excel.

    Argumentos/Parâmetros:
        pagina (Worksheet): A página da planilha de onde as notas serão extraídas.
        posicao_materia (int): O índice da coluna que contém o nome da matéria.
        posicao_nota (int): O índice da coluna que contém a nota.

    Retorno:
        list: Uma lista de dicionários com 'materia' e 'nota'.
    '''
    materias_nota = []
    for linha in pagina.iter_rows(min_row=3):
        materia = linha[posicao_materia].value
        nota = linha[posicao_nota].value
        if materia is not None and nota is not None:
            materias_nota.append({'materia': materia, 'nota': nota})
    return materias_nota    

def calcular_media_do_bimestre(notas_BM):
    '''
    Calcula a média das notas de um bimestre.

    Argumentos/Parâmetros:
        notas_BM (list): Lista de dicionários contendo as notas do bimestre.

    Retorno:
        float: A média das notas do bimestre.
    '''
    media = sum(materia_nota['nota'] for materia_nota in notas_BM) / len(notas_BM)
    return round(media, 2)

def calcular_media_de_todos_bimestres(*notas_bimestres):
    '''
    Calcula a média das médias de todos os bimestres fornecidos.

    Argumentos/Parâmetros:
        *notas_bimestres (list): Notas de cada bimestre.

    Retorno:
        float: A média das médias dos bimestres.
    '''
    medias = [calcular_media_do_bimestre(notas) for notas in notas_bimestres if notas]
    media_dos_BM = sum(medias) / len(medias)
    return round(media_dos_BM, 2)

# Carregar a planilha e páginas
planilha = openpyxl.load_workbook('notas.xlsx')
pagina_1ano = planilha['1ºano']
pagina_2ano = planilha['2ºano']


notas_1ano = [
    pegar_notas(pagina_1ano, 0, 1),
    pegar_notas(pagina_1ano, 4, 5),
    pegar_notas(pagina_1ano, 8, 9),
    pegar_notas(pagina_1ano, 12, 13)
]

notas_2ano = [
    pegar_notas(pagina_2ano, 0, 1),
    pegar_notas(pagina_2ano, 4, 5),
    # pegar_notas(pagina_2ano, 8, 9),
    # pegar_notas(pagina_2ano, 12, 13)
]

# Exibir médias do 1º ano
print('\nNotas 1ºano')
for i, notas in enumerate(notas_1ano, start=1):
    print(f'{i}BM: {calcular_media_do_bimestre(notas)}')
print(f'Média anual: {calcular_media_de_todos_bimestres(*notas_1ano)}\n')

# Exibir médias do 2º ano
print('\nNotas 2ºano')
for i, notas in enumerate(notas_2ano, start=1):
    print(f'{i}BM: {calcular_media_do_bimestre(notas)}')
print(f'Média anual: {calcular_media_de_todos_bimestres(*notas_2ano)}\n')