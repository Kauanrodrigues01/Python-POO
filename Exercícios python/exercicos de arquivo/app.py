# Lendo o arquivo e processando os dados
with open('exercicos de arquivo/nomes_telefones.txt', 'r') as arquivo:
    linhas = arquivo.readlines()

# Inicializando variáveis para cálculos
espacos_utilizados = []
espaco_total = 0.0

# Processando cada linha para extrair o nome do usuário e o espaço utilizado
for idx, linha in enumerate(linhas):
    # Dividindo a linha em nome e espaço utilizado
    nome = linha[:15].strip()
    espaco_mb = float(linha[15:].strip())  # Convertendo para float

    # Calculando o total de espaço ocupado
    espaco_total += espaco_mb

    # Armazenando o espaço utilizado por usuário para o relatório
    espacos_utilizados.append((idx + 1, nome, espaco_mb))

# Abrindo o arquivo de relatório para escrita
with open('exercicos de arquivo/relatório.txt', 'w') as relatorio:
    # Escrevendo o cabeçalho do relatório
    relatorio.write("ACME Inc.               Uso do espaço em disco pelos usuários\n")
    relatorio.write("------------------------------------------------------------------------\n")
    relatorio.write("Nr.  Usuário        Espaço utilizado     % do uso\n")
    relatorio.write("\n")

    # Escrevendo cada linha com os dados de cada usuário
    for nr, usuario, espaco_mb in espacos_utilizados:
        percentual = (espaco_mb / espaco_total) * 100
        relatorio.write(f"{nr:<5} {usuario:<15} {espaco_mb:>10.2f} MB       {percentual:>8.2f}%\n")
    
    relatorio.write("\n")
    relatorio.write(f"Espaço total ocupado: {espaco_total:.2f} MB\n")
    relatorio.write(f"Espaço médio ocupado: {(espaco_total / len(espacos_utilizados)):.2f} MB\n")

print("Relatório 'relatório.txt' gerado com sucesso.")
