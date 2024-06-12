import math

# 1. Crie uma classe chamada “Triângulo” com atributos para armazenar os três lados do triângulo. Implemente métodos para verificar se é um triângulo válido e calcular sua área.
class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def eh_valido(self):
        return (self.lado1 + self.lado2 > self.lado3 and
                self.lado1 + self.lado3 > self.lado2 and
                self.lado2 + self.lado3 > self.lado1)

    def calcular_area(self):
        if not self.eh_valido():
            return "Não é um triângulo válido."
        
        s = (self.lado1 + self.lado2 + self.lado3) / 2
        area = math.sqrt(s * (s - self.lado1) * (s - self.lado2) * (s - self.lado3))
        return round(area, 2)
        
# Exemplo:
'''triangulo1 = Triangulo(3, 4, 5)
if triangulo1.eh_valido():
    area = triangulo1.calcular_area()
    print(f'A área do triângulo é {area}')
else:
    print("Os lados fornecidos não formam um triângulo válido.")
'''

# 2. Implemente uma classe chamada “Livro” com atributos para armazenar o título, o autor e o número de páginas do livro. Adicione métodos para emprestar o livro, devolvê-lo e verificar se está disponível.
class Livro:
    def __init__(self, titulo, autor, num_pag):
        self.titulo = titulo
        self.autor = autor
        self.numero_paginas = num_pag
        self.disponivel = True

    def verificar_disponibilidade(self):
        if self.disponivel:
            print(f'O livro "{self.titulo}" está disponível')
        else:
            print(f'O livro "{self.titulo}" está indisponível')

    def emprestar_livro(self):
        if self.disponivel:
            self.disponivel = False
            print(f'O livro "{self.titulo}" foi emprestado')
        else:
            print(f'O livro "{self.titulo}" está indisponível')

    def livro_devolvido(self):
        if not self.disponivel:
            self.disponivel = True
            print(f'O livro "{self.titulo}" foi devolvido com sucesso!')
        else:
            print(f'O livro "{self.titulo}" já está disponível, verifique se houve um erro.')

# Exemplo:
'''livro1 = Livro("O Alquimista", "Paulo Coelho", 208)
livro1.verificar_disponibilidade()
livro1.emprestar_livro()
livro1.verificar_disponibilidade()
livro1.livro_devolvido()
livro1.verificar_disponibilidade()
'''

# 3. Implemente uma classe chamada “Carro” com atributos para armazenar a marca, o modelo e a velocidade atual do carro. Adicione métodos para acelerar, frear e exibir a velocidade atual.
class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.velocidade_atual = 0

    def acelerar(self, incremento):
        self.velocidade_atual += incremento
        print(f"O carro {self.marca} {self.modelo} acelerou para {self.velocidade_atual} km/h")

    def frear(self, decremento):
        if self.velocidade_atual - decremento >= 0:
            self.velocidade_atual -= decremento
        else:
            self.velocidade_atual = 0
        print(f"O carro {self.marca} {self.modelo} reduziu para {self.velocidade_atual} km/h")

    def exibir_velocidade_atual(self):
        print(f"A velocidade atual do carro {self.marca} {self.modelo} é {self.velocidade_atual} km/h")

# Exemplo:
'''
carro1 = Carro("Toyota", "Corolla")
carro1.exibir_velocidade_atual()
carro1.acelerar(20)
carro1.acelerar(30)
carro1.frear(10)
carro1.exibir_velocidade_atual()
carro1.frear(50)
carro1.exibir_velocidade_atual()
'''

# 4. Crie uma classe chamada “Paciente” que possua atributos para armazenar o nome, a idade e o histórico de consultas de um paciente. Implemente métodos para adicionar uma nova consulta ao histórico e exibir as consultas realizadas.
class Paciente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.historico_consultas = []

    def adicionar_consulta(self, consulta):
        self.historico_consultas.append(consulta)
        print(f"Consulta adicionada para {self.nome}: {consulta}")

    def exibir_consultas(self):
        if self.historico_consultas:
            print(f"Histórico de consultas de {self.nome}:")
            for consulta in self.historico_consultas:
                print(f" - {consulta}")
        else:
            print(f"{self.nome} não possui consultas registradas.")

# Exemplo:
'''
paciente1 = Paciente("Maria Silva", 30)
paciente1.adicionar_consulta("10/01/2024 - Check-up")
paciente1.adicionar_consulta("15/02/2024 - Consulta de rotina")
paciente1.exibir_consultas()
'''


# 5. Implemente uma classe chamada “Produto” que possua atributos para armazenar o nome, o preço e a quantidade em estoque. Adicione métodos para calcular o valor total em estoque e verificar se o produto está disponível.

class Produto:
    def __init__(self, nome, preco, quantidade_estoque):
        self.nome = nome
        self.preco = preco
        self.quantidade_estoque = quantidade_estoque

    def valor_total_estoque(self):
        valor_total = self.preco * self.quantidade_estoque
        return valor_total

    def verificar_disponibilidade(self):
        if self.quantidade_estoque > 0:
            return True
        else:
            return False

    def exibir_detalhes(self):
        disponibilidade = "disponível" if self.verificar_disponibilidade() else "indisponível"
        print(f"Produto: {self.nome}")
        print(f"Preço: R${self.preco:.2f}")
        print(f"Quantidade em estoque: {self.quantidade_estoque}")
        print(f"Disponibilidade: {disponibilidade}")

# Exemplo de uso:
'''
produto1 = Produto("Camiseta", 49.90, 10)
produto2 = Produto("Calça Jeans", 129.90, 0)

print(f"Valor total em estoque de {produto1.nome}: R${produto1.valor_total_estoque():.2f}")
print(f"Valor total em estoque de {produto2.nome}: R${produto2.valor_total_estoque():.2f}")

produto1.exibir_detalhes()
produto2.exibir_detalhes()
'''

#Implemente uma classe chamada “Aluno” que possua atributos para armazenar o nome, a matrícula e as notas de um aluno. Adicione métodos para calcular a média das notas e verificar a situação do aluno (aprovado ou reprovado).

class Aluno:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self._notas = []
        self.media = 0

    def adicionar_notas(self, nota):
        if 0 <= nota <= 10:
            self._notas.append(nota)
        else:
            print("Nota inválida. Insira uma nota entre 0 e 10.")

    def calcular_media(self):
        if not self._notas:
            print("Nenhuma nota disponível para calcular a média.")
            return 0
        notas = sum(self._notas)
        media = notas / len(self._notas)
        media = round(media, 2)
        self.media = media
        print(f'A média atual do aluno é de {self.media}')

    def mostrar_notas(self):
        if len(self._notas) > 0:
            print(f'Notas do aluno {self.nome}')
            for nota in self._notas:
                print(nota)
        else:
            print('O aluno não tem notas para serem exibidas')

'''
aluno1 = Aluno('Jose', 2345678)
aluno1.adicionar_notas(10)
aluno1.adicionar_notas(7.66)
aluno1.calcular_media()
aluno1.adicionar_notas(10)
aluno1.calcular_media()
'''

# 6. Crie uma classe chamada “Retângulo” que possua atributos para armazenar a largura e a altura. Implemente métodos para calcular a área e o perímetro do retângulo.
class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
        
    def calcular_area(self):
        area = self.largura * self.altura
        print(f'A área é de {area}')
      
    def calcular_perimetro(self):
        perimetro = (self.largura * 2) + (self.altura * 2)
        print(f'O perímetro é de {perimetro}')


# 7. Crie uma classe chamada “Círculo” que possua um atributo para armazenar o raio e métodos para calcular a área e o perímetro do círculo.

class Circulo:
    def __init__(self, raio):
        self.raio = raio
    
    def area_do_circulo(self):
        pi = 3.14159265358979323846
        area = pi * (self.raio ** 2)
        area = round(area, 2)
        print(f'A área do circulo é {area}')

    def calcular_perimetro(self):
        pi = 3.14159265358979323846
        perimetro = (2 * pi * self.raio)
        perimetro = round(perimetro, 2)
        print(f'perimetro: {perimetro}')

#Exemplo:
'''
circulo1 = Circulo(3)
circulo1.area_do_circulo()
circulo1.calcular_perimetro()
'''