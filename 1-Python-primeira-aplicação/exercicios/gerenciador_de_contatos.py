import os

def adicao(x, y):
    return x + y 
def subtracao(x, y):
    return x - y
def multiplicacao(x, y):
    return x * y
def divisao(x, y):
    return x/y
def exponenciacao(x, y):
    return x ** y

def deseja_fazer_novamente():
    print('Você deseja fazer novamente?\n')
    s_or_n = input('Digite "S" pra sim e digite "N" para não: ')
    if s_or_n == 'S':
        main()
    elif s_or_n == 'N':
        os.system('cls')
        print('Ok, Programa encerrado')
    else:
        os.system('cls')
        print('opcao invalida')
        input('Digite qualquer tecla para continuar: ')
        deseja_fazer_novamente()

def calcular():
    os.system('cls')
    num_1 = float(input('Digite o primeiro numero: '))
    num_2 = float(input('Digite o segundo número: '))
    os.system('cls')
    print('1. Adção')
    print('2. Subtração')
    print('3. Multiplicação')
    print('4. Divisão')
    print('5. exponenciação')
    operacao = int(input('Digite o número da opeção matemática que você quer: '))
    if operacao == 1:
        resultado = adicao(num_1, num_2)
        os.system('cls')
        print(f'O resultado é {resultado}')
        deseja_fazer_novamente()
    elif operacao == 2:
        resultado = subtracao(num_1, num_2)
        os.system('cls')
        print(f'O resultado é {resultado}')
        deseja_fazer_novamente()
    elif operacao == 3:
        resultado = multiplicacao(num_1, num_2)
        os.system('cls')
        print(f'O resultado é {resultado}')
        deseja_fazer_novamente()
    elif operacao == 4:
        resultado = divisao(num_1, num_2)
        os.system('cls')
        print(f'O resultado é {resultado}')
        deseja_fazer_novamente()
    elif operacao == 5:
        resultado = exponenciacao(num_1, num_2)
        os.system('cls')
        print(f'O resultado é {resultado}')
        deseja_fazer_novamente()
    else:
        os.system('cls')
        print('opção invalida')
        input('Digite qualquer tecla para continuar: ')
        deseja_fazer_novamente()
    

def main():
    calcular()
if __name__ == '__main__':
    main()