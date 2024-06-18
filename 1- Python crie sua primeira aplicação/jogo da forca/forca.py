import random
import os

def exibir_abertura():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")
def escolhendo_palavra_secreta():
    arquivo = open('palavras.txt', 'r')
    palavras = []

    for linha in arquivo:
        palavras.append(linha.strip())

    palavra_secreta = random.choice(palavras).capitalize()

    arquivo.close()
    return palavra_secreta
def chute_jogador():
    chute = input('\nQual letra? ')
    return chute.strip()
def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")
def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")
def desenha_forca(chances_para_enforcar):
    print("  _______     ")
    print(" |/      |    ")

    if(chances_para_enforcar == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(chances_para_enforcar == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(chances_para_enforcar == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(chances_para_enforcar == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(chances_para_enforcar == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(chances_para_enforcar == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (chances_para_enforcar == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def jogar():
    os.system('cls')
    exibir_abertura()
    palavra_secreta = escolhendo_palavra_secreta()

    letras_acertadas = ['_' for letra in palavra_secreta]

    ganhou = False
    enforcou = False
    chances_para_enforcar = 0

    print(letras_acertadas)
    while (not ganhou and not enforcou):
        chute = chute_jogador()

        if chute.lower() in palavra_secreta.lower():
            index = 0
            for letra in palavra_secreta:
                if chute.lower() == letra.lower():
                    letras_acertadas[index] = letra.lower()
                index += 1
        else:
            desenha_forca(chances_para_enforcar)
            print(f'Você errou você ainda tem {6 -chances_para_enforcar}')
            chances_para_enforcar += 1

        print(letras_acertadas)

        enforcou = chances_para_enforcar == 7
        ganhou = '_' not in letras_acertadas

    if (ganhou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)

print('Fim do jogo')


if __name__ == '__main__':
    jogar()




# palavras_exemplo = [
#     "amor", "casa", "felicidade", "mundo", "livro", "computador", "mesa", "cadeira", "janela", "porta",
#     "carro", "bicicleta", "estrada", "sol", "lua", "estrela", "céu", "mar", "rio", "floresta",
#     "montanha", "planeta", "cidade", "vila", "aldeia", "bairro", "rua", "avenida", "praça", "parque",
#     "jardim", "flor", "árvore", "fruta", "animal", "pássaro", "peixe", "cachorro", "gato", "coelho",
#     "livro", "revista", "jornal", "papel", "caneta", "lápis", "borracha", "estojo", "caderno", "mochila",
#     "escola", "universidade", "aula", "professor", "aluno", "médico", "enfermeiro", "hospital", "clínica", "farmácia",
#     "loja", "supermercado", "mercado", "feira", "restaurante", "padaria", "lanchonete", "bar", "café", "sorveteria",
#     "cinema", "teatro", "museu", "galeria", "biblioteca", "livraria", "parque", "praia", "campo", "quadra",
#     "estádio", "ginásio", "academia", "piscina", "sauna", "spa", "hotel", "pousada", "resort", "camping",
#     "viagem", "turismo", "feriado", "festa", "celebração", "aniversário", "casamento", "nascimento", "batizado", "funeral",
#     "política", "governo", "eleição", "partido", "presidente", "senador", "deputado", "prefeito", "vereador", "justiça",
#     "lei", "tribunal", "juiz", "advogado", "procurador", "defensor", "acusado", "réu", "crime", "prisão",
#     "economia", "negócio", "empresa", "indústria", "comércio", "serviço", "produto", "mercado", "cliente", "consumidor",
#     "trabalho", "emprego", "salário", "profissão", "carreira", "vaga", "entrevista", "currículo", "experiência", "qualificação",
#     "tecnologia", "internet", "rede", "sistema", "programa", "software", "hardware", "aplicativo", "site", "plataforma",
#     "ciência", "pesquisa", "experimento", "laboratório", "teoria", "hipótese", "prova", "evidência", "resultado", "descoberta",
#     "saúde", "doença", "sintoma", "tratamento", "cura", "medicamento", "vacina", "epidemia", "pandemia", "vírus",
#     "arte", "música", "pintura", "escultura", "dança", "teatro", "cinema", "fotografia", "literatura", "poesia",
#     "esporte", "futebol", "basquete", "vôlei", "tênis", "natação", "atletismo", "ginástica", "luta", "corrida", "amor", "casa", "felicidade", "mundo", "livro", "computador", "mesa", "cadeira", "janela", "porta",
#     "carro", "bicicleta", "estrada", "sol", "lua", "estrela", "céu", "mar", "rio", "floresta",
#     "montanha", "planeta", "cidade", "vila", "aldeia", "bairro", "rua", "avenida", "praça", "parque",
#     "jardim", "flor", "árvore", "fruta", "animal", "pássaro", "peixe", "cachorro", "gato", "coelho",
#     "livro", "revista", "jornal", "papel", "caneta", "lápis", "borracha", "estojo", "caderno", "mochila",
#     "escola", "universidade", "aula", "professor", "aluno", "médico", "enfermeiro", "hospital", "clínica", "farmácia",
#     "loja", "supermercado", "mercado", "feira", "restaurante", "padaria", "lanchonete", "bar", "café", "sorveteria",
#     "cinema", "teatro", "museu", "galeria", "biblioteca", "livraria", "parque", "praia", "campo", "quadra",
#     "estádio", "ginásio", "academia", "piscina", "sauna", "spa", "hotel", "pousada", "resort", "camping",
#     "viagem", "turismo", "feriado", "festa", "celebração", "aniversário", "casamento", "nascimento", "batizado", "funeral",
#     "política", "governo", "eleição", "partido", "presidente", "senador", "deputado", "prefeito", "vereador", "justiça",
#     "lei", "tribunal", "juiz", "advogado", "procurador", "defensor", "acusado", "réu", "crime", "prisão",
#     "economia", "negócio", "empresa", "indústria", "comércio", "serviço", "produto", "mercado", "cliente", "consumidor",
#     "trabalho", "emprego", "salário", "profissão", "carreira", "vaga", "entrevista", "currículo", "experiência", "qualificação",
#     "tecnologia", "internet", "rede", "sistema", "programa", "software", "hardware", "aplicativo", "site", "plataforma",
#     "ciência", "pesquisa", "experimento", "laboratório", "teoria", "hipótese", "prova", "evidência", "resultado", "descoberta",
#     "saúde", "doença", "sintoma", "tratamento", "cura", "medicamento", "vacina", "epidemia", "pandemia", "vírus",
#     "arte", "música", "pintura", "escultura", "dança", "teatro", "cinema", "fotografia", "literatura", "poesia",
#     "esporte", "futebol", "basquete", "vôlei", "tênis", "natação", "atletismo", "ginástica", "luta", "corrida"
# ]
# palavras_aleatorias = [random.choice(palavras_exemplo) for _ in range(10000)]
# arquivo = open('palavras.txt', 'w')

# for palavra in palavras_aleatorias:
#     arquivo.write(f'{palavra}\n')