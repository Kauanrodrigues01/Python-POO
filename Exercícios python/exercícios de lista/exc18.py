'''
Uma grande emissora de televisão quer fazer uma enquete entre os seus telespectadores para saber qual o melhor jogador após cada jogo. Para isto, faz-se necessário o desenvolvimento de um programa, que será utilizado pelas telefonistas, para a computação dos votos. Sua equipe foi contratada para desenvolver este programa, utilizando a linguagem de programação python. Para computar cada voto, a telefonista digitará um número, entre 1 e 23, correspondente ao número da camisa do jogador. Um número de jogador igual zero, indica que a votação foi encerrada. Se um número inválido for digitado, o programa deve ignorá-lo, mostrando uma breve mensagem de aviso, e voltando a pedir outro número. Após o final da votação, o programa deverá exibir:

a) O total de votos computados;
b) Os númeos e respectivos votos de todos os jogadores que receberam votos;
c) O percentual de votos de cada um destes jogadores;
d) O número do jogador escolhido como o melhor jogador da partida, juntamente   com o número de votos e o percentual de votos dados a ele.

Observe que os votos inválidos e o zero final não devem ser computados como votos. O resultado aparece ordenado pelo número do jogador. O programa deve fazer uso de arrays. O programa deverá executar o cálculo do percentual de cada jogador através de uma função. Esta função receberá dois parâmetros: o número de votos de um jogador e o total de votos. A função calculará o percentual e retornará o valor calculado. Abaixo segue uma tela de exemplo. O disposição das informações deve ser o mais próxima possível ao exemplo. Os dados são fictícios e podem mudar a cada execução do programa. Ao final, o programa deve ainda gravar os dados referentes ao resultado da votação em um arquivo texto no disco, obedecendo a mesma disposição apresentada na tela.
'''

def calcular_percentual(votos_jogador, total_votos):
    return (votos_jogador / total_votos) * 100

def main():
    votos = [0] * 24  # Array para armazenar os votos dos jogadores de 1 a 23

    print("Enquete: Quem foi o melhor jogador da partida?")

    while True:
        try:
            voto = int(input("Número do jogador (0=fim): "))

            if voto == 0:
                break
            elif 1 <= voto <= 23:
                votos[voto] += 1
            else:
                print("Número inválido. Digite um número entre 1 e 23 ou 0 para encerrar.")
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")

    total_votos = sum(votos)
    
    if total_votos == 0:
        print("Nenhum voto computado.")
        return

    print("\nResultado da votação:")
    print(f"Total de votos computados: {total_votos}")

    print("Jogador   Votos   %")
    for jogador in range(1, 24):
        if votos[jogador] > 0:
            percentual = calcular_percentual(votos[jogador], total_votos)
            print(f"{jogador:<9}{votos[jogador]:<7}{percentual:.2f}%")

    melhor_jogador = max(range(1, 24), key=lambda jogador: votos[jogador])
    votos_melhor_jogador = votos[melhor_jogador]
    percentual_melhor_jogador = calcular_percentual(votos_melhor_jogador, total_votos)

    print(f"\nO melhor jogador foi o número {melhor_jogador}, com {votos_melhor_jogador} votos, correspondendo a {percentual_melhor_jogador:.2f}% do total de votos.")

    # Gravar os resultados em um arquivo de texto
    with open("resultado_votacao.txt", "w") as arquivo:
        arquivo.write("Resultado da votação:\n")
        arquivo.write(f"Total de votos computados: {total_votos}\n")
        arquivo.write("Jogador   Votos   %\n")
        for jogador in range(1, 24):
            if votos[jogador] > 0:
                percentual = calcular_percentual(votos[jogador], total_votos)
                arquivo.write(f"{jogador:<9}{votos[jogador]:<7}{percentual:.2f}%\n")
        arquivo.write(f"\nO melhor jogador foi o número {melhor_jogador}, com {votos_melhor_jogador} votos, correspondendo a {percentual_melhor_jogador:.2f}% do total de votos.\n")

if __name__ == "__main__":
    main()

    

        
        
    
    