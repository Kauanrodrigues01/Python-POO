'''Estudando classes no python'''

# Exercicio 1
class Carro:
    def __init__(self, modelo, cor, ano):
         self.modelo = modelo
         self.cor = cor
         self.ano = ano
    
    def __str__(self):
         return f'{self.modelo} | {self.cor} | {self.ano}'
    
siena = Carro('Gran Siena', 'preto', '2016')
print(siena)


# Exercicio 2
class Cliente:
    def __init__(self, nome, sexo, idade, nacionalidade):
        self.nome = nome
        self.sexo = sexo
        self.idade = idade
        self.nacionalidade = nacionalidade
    def __str__(self):
        return f'{self.nome} | {self.sexo} | {self.idade} | {self.nacionalidade}'
    
cliente1 = Cliente('Andre', 'M', 39, 'Brasileiro')
cliente2 = Cliente('Matheus', 'M', 22, 'Português')
cliente3 = Cliente('Júlia', 'F', 19, 'Brasileira')
cliente4 = Cliente('Antonela', 'M', 37, 'Argentina')
print(cliente1)
print(cliente2)
print(cliente3)
print(cliente4)

# Exercicio 3

class Cliente:
    def __init__(self, nome='', idade=0, email='', telefone=''):
        self.nome = nome
        self.idade = idade
        self.email = email
        self.telefone = telefone

# Instanciando três objetos da classe Cliente e atribuindo valores aos seus atributos através do construtor
cliente1 = Cliente(nome='Alice', idade=25, email='alice@gmail.com', telefone='123-456-7890')
cliente2 = Cliente(nome='Bob', idade=30, email='bob@gmail.com', telefone='987-654-3210')
cliente3 = Cliente(nome='Charlie', idade=22, email='charlie@gmail.com', telefone='555-123-4567')