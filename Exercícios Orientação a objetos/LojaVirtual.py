class Produto:
    def __init__(self, nome_produto, preco, estoque):
        self.nome_produto = nome_produto
        self.preco = preco
        self.estoque = estoque

    def aumentar_preco(self, valor):
        if valor > 0: 
            taxa = valor / 100
            self.preco += (self.preco * taxa)
            print(f"Preço do produto {self.nome} aumentado em {valor}%. Novo preço: R${self.preco:.2f}")
        else:
            print("O valor de aumento deve ser positivo.")

    def diminuir_preco(self, valor):
        if valor > 0:
            taxa = valor / 100
            self.preco -= (self.preco * taxa)
        else:
            print("O valor de decresimo deve ser positivo.")

class Carrinho:
    def __init__(self):
        self.itens = []

    def adicionar_itens(self, produto, quantidade):
        if quantidade > produto.estoque:
            print(f"Quantidade solicitada para {produto.nome} excede o estoque disponível.")
        else:
            self.itens.append((produto, quantidade))
            produto.estoque -= quantidade
            print(f"{quantidade} unidade(s) de {produto.nome_produto} adicionada(s) ao carrinho.")

    def remover_itens(self, produto):
        for item in self.itens:
            if item[0] == produto:
                produto.estoque += item[1]
                self.itens.remove(item)
                print(f"{item[1]} unidade(s) de {produto.nome_produto} removida(s) do carrinho.")
                return
            else:
                print(f"{produto.nome} não encontrado no carrinho.")
    
    def aplicar_desconto(self, valor):
        if valor > 0: 
            taxa = valor / 100
            for item in self.itens:
                item[0].preco -= (item[0].preco * taxa)
            print(f"Desconto de {valor}% aplicado a todos os itens do carrinho.")
        else:
            print(f"o valor do desconto tem que ser positivo")

    def calcular_total(self):
        total = 0
        if len(self.itens) > 0:
            for item in self.itens:
                total += (item[0].preco * item[1])
            print(f'Valor Total: R${total}')
        else:
            print('Não tem itens no seu carrinho')


class LojaVirtual:
    def __init__(self, nome_loja):
        self.nome_loja = nome_loja
        self.produtos = []
        self.carrinho = Carrinho()

    def cadastrar_produto(self, nome, preco, estoque):
        if preco > 0 and estoque > 0:
            produto = Produto(nome, preco, estoque)
            self.produtos.append(produto)
            return produto
        else:
            print(f'O preço e o estoque tem que ser positivos, confira!')
    
    def listar_produtos(self):
        print('Lista de produtos\n')
        print(f'{'Nome'.ljust(20)} | Preço')
        for produto in self.produtos:
            print(f'{produto.nome_produto.ljust(20)} | R${str(produto.preco).ljust(20)}')


loja_virtual = LojaVirtual("Minha Loja Virtual")


notebook = loja_virtual.cadastrar_produto("Notebook", 3000.00, 10)
celular = loja_virtual.cadastrar_produto("Smartphone", 1500.00, 20)

loja_virtual.listar_produtos()

carrinho = Carrinho()

carrinho.adicionar_itens(notebook, 1)
carrinho.adicionar_itens(celular, 2)
carrinho.aplicar_desconto(10)
carrinho.calcular_total()
carrinho.remover_itens(notebook)
carrinho.calcular_total()