import os
Contatos = []
def deseja_fazer_novamente():
    s_or_n = input('Você deseja fazer novamente?(s/n): ')
    if s_or_n == 's':
        main()
    elif s_or_n == 'n':
        os.system('cls')
        print('Ok, Programa encerrado')
    else:
        os.system('cls')
        print('opcao invalida')
        input('Digite qualquer tecla para continuar: ')
        deseja_fazer_novamente()

def adicionar_contato():
    os.system('cls')
    print('Adionando Contatos\n')
    nome = input('Nome do contato: ')
    numero = input('Numero do contato:')
    Contatos.append({'nome': nome, 'numero': numero})
    os.system('cls')
    print(f'\nO contato {nome} foi salvo com sucesso\n')
    deseja_fazer_novamente()


def exibir_opcoes():
    print('Escolha uma operação:')
    print('1. Adicionar contato')
    print('2. Remover contato')
    print('3. Buscar contato')
    print('4. Listar contatos')
    print('5. Sair\n')
def escolher_opcao():
    opcao_escolhida = int(input('Escolha: '))
    if opcao_escolhida == 1:
        adicionar_contato()

def main():
    os.system('cls')
    exibir_opcoes()
    escolher_opcao()
if __name__ == '__main__':
    main()