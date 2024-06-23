import openpyxl

# Função para pegar as notas
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
        materias_nota.append({'materia': materia, 'nota': nota})
    return materias_nota    

# Funções para calcular a média de um bimestre ou de todos os bimestres
def calcular_media_do_bimestre(notas_BM):
    '''
    Calcula a média das notas de um bimestre.

    Argumentos/Parâmetros:
        notas_BM (list): Lista de dicionários contendo as notas do bimestre.

    Retorno:
        float: A média das notas do bimestre.
    '''
    soma_notas = 0
    qntd_notas = 0
    for materia_nota in notas_BM:
        nota = materia_nota['nota']
        if nota is not None:
            soma_notas += nota
            qntd_notas += 1
    media = soma_notas / qntd_notas
    return round(media, 2)

def calcular_media_de_todos_bimestres(notas_1BM=None, notas_2BM=None, notas_3BM=None, notas_4BM=None):
    '''
    Calcula a média das médias de todos os bimestres fornecidos.

    Argumentos/Parâmetros:
        notas_1BM (list, optional): Notas do 1º bimestre. Default é None.
        notas_2BM (list, optional): Notas do 2º bimestre. Default é None.
        notas_3BM (list, optional): Notas do 3º bimestre. Default é None.
        notas_4BM (list, optional): Notas do 4º bimestre. Default é None.

    Retorno:
        float: A média das médias dos bimestres.
    '''
    medias = [
        calcular_media_do_bimestre(notas_1BM) if notas_1BM is not None else None,
        calcular_media_do_bimestre(notas_2BM) if notas_2BM is not None else None,
        calcular_media_do_bimestre(notas_3BM) if notas_3BM is not None else None,
        calcular_media_do_bimestre(notas_4BM) if notas_4BM is not None else None
    ]

    soma_medias = 0
    qntd_medias = 0
    for media in medias:
        if media is not None:
            soma_medias += media
            qntd_medias += 1

    media_dos_BM = soma_medias / qntd_medias
    return round(media_dos_BM, 2)

# Funções para calcular e EXIBIR a média de um bimestre ou de todos os bimestres
def exibir_media_de_todos_bimestres(notas_1BM=None, notas_2BM=None, notas_3BM=None, notas_4BM=None):
    '''
    Calcula e exibe a média das médias de todos os bimestres fornecidos.

    Argumentos/Parâmetros:
        notas_1BM (list, optional): Notas do 1º bimestre. Default é None.
        notas_2BM (list, optional): Notas do 2º bimestre. Default é None.
        notas_3BM (list, optional): Notas do 3º bimestre. Default é None.
        notas_4BM (list, optional): Notas do 4º bimestre. Default é None.

    Retorno:
        None: Esta função não retorna um valor. Ela exibe a média das médias dos bimestres.
    '''
    media_dos_BM = calcular_media_de_todos_bimestres(notas_1BM, notas_2BM, notas_3BM, notas_4BM)
    print(round(media_dos_BM, 2))

def exibir_media_do_bimestre(notas_BM):
    '''
    Calcula e exibe a média das notas de um bimestre.

    Argumentos/Parâmetros:
        notas_BM (list): Lista de dicionários contendo as notas do bimestre.

    Retorno:
        None: Esta função não retorna um valor. Ela exibe a média das notas do bimestre.
    '''
    media = calcular_media_do_bimestre(notas_BM)
    print(round(media, 2))

# Carregar a planilha e páginas
planilha = openpyxl.load_workbook('notas.xlsx')
pagina_1ano = planilha['1ºano']
pagina_2ano = planilha['2ºano']

# Pegar notas de cada bimestre
notas_1ano = [
    pegar_notas(pagina_1ano, 0, 1),
    pegar_notas(pagina_1ano, 4, 5),
    pegar_notas(pagina_1ano, 8, 9),
    pegar_notas(pagina_1ano, 12, 13)
]

notas_2ano = [
    pegar_notas(pagina_2ano, 0, 1),
    pegar_notas(pagina_2ano, 4, 5),
    # Descomentar as linhas abaixo se houver dados para o 3º e 4º bimestres
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