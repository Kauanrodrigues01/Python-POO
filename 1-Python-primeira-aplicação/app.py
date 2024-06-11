import os

restaurantes = [{'nome': 'Praça', 'categoria': 'Japonesa', 'ativo':False },{'nome': 'Pizza suprema', 'categoria': 'Pizza','ativo':True}, {'nome': 'Cantina', 'categoria': 'Italiana','ativo':False}]

def exibir_nome_programa():
    ''' Exibe o nome estilizado do programa na tela '''
    print('''
    ░██████╗░█████╗░██████╗░░█████╗░██████╗░
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝

    ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░''')
def exibir_opcoes():
    ''' Exibe as opções disponíveis no menu principal '''
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Ativar/Desativar restaurante')
    print('4. Sair\n')
def voltar_menu():
    ''' Solicita uma tecla para voltar ao menu principal 
    
    Outputs:
    - Retorna ao menu principal
    '''
    input('\nDigite uma tecla para voltar ao menu: ')
    main()
def exibir_subtitulo(texto):
    ''' Exibe um subtítulo estilizado na tela 
    
    Inputs:
    - texto: str - O texto do subtítulo
    '''
    os.system('cls')
    linha = '*' * len(texto) 
    print(linha)
    print(texto)
    print(linha)

    print()

def cadastrar_restaurante():
    '''Essa função é responsável por cadastrar um novo Restaurante
    inputs:
    - Nome do restaurante
    - Categoria

    Outputs:
    - Adicona um novo restaurante a Lista de restaurantes
    '''
    exibir_subtitulo('Cadastro de Novos Restaurantes:')

    nome_restaurante = input('Digite o nome do novo restaurante: ')
    categoria = input(f'Digite a categoria do restaurante {nome_restaurante}: ')
    restaurantes.append({'nome': nome_restaurante, 'categoria': categoria, 'ativo':False})

    print(f'o restaurante {nome_restaurante} foi cadastrado com sucesso')
    voltar_menu()
def listar_restaurantes():
    ''' Lista os restaurantes presentes na lista 
    
    Outputs:
    - Exibe a lista de restaurantes na tela
    '''
    exibir_subtitulo('Listando todos os restaurantes')

    print(f'{'Nome restaurante:'.ljust(17)} | {'Categoria:'.ljust(10)} | Status')
    for restaurante in  restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = f'ativo' if restaurante['ativo'] else f'desativado'
        print(f'- {nome_restaurante.ljust(15)} | {categoria.ljust(10)} | {ativo}')

    voltar_menu()
def alternar_estado_restaurante():
    ''' Altera o estado ativo/desativado de um restaurante 
    
    Outputs:
    - Exibe mensagem indicando o sucesso da operação
    '''
    exibir_subtitulo('Ativar/Desativar restaurante')
    nome = input('Digite o nome do restaurante: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O resturante {nome} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome} foi desativado com sucesso'
            print(mensagem)
            voltar_menu()
    if not restaurante_encontrado:
        print('O restaurante não foi encontado')
    
def finalizar_app():
    ''' Exibe mensagem de finalização do aplicativo '''
    exibir_subtitulo('app encerrado')
def opcao_invalida():
    ''' Exibe mensagem de opção inválida e retorna ao menu principal 
    
    Outputs:
    - Retorna ao menu principal
    '''
    os.system('cls')
    print('Opção invalida\n')
    voltar_menu()


def escolher_opcao():
    ''' Solicita e executa a opção escolhida pelo usuário 
    
    Outputs:
    - Executa a opção escolhida pelo usuário
    '''
    try:
        opcao_escolhida = input('Escolha uma opção: ')
        opcao_escolhida = int(opcao_escolhida)
        if opcao_escolhida == 1:
            cadastrar_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3: 
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    ''' Função principal que inicia o programa '''
    os.system('cls')
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()