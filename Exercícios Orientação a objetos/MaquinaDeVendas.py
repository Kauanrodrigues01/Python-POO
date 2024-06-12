class Produto:
    def __init__(self, nome, preco, estoque, descricao):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque
        self.descricao = descricao

    def ver_produto_completo(self):
        print(f'{"Nome".ljust(15)} | {"Preço".ljust(15)} | {"Estoque".ljust(15)} | {"Descrição"}')
        print(f'{self.nome.ljust(15)} | {str(self.preco).ljust(15)} | {str(self.estoque).ljust(15)} | {self.descricao.ljust(15)}')

class MaquinaDeVendas:
    def __init__(self):
        self.produtos = []
        self.dinheiro_inserido = 0.0

    def cadastrar_produto(self, nome, preco, estoque, descricao):
        for produto in self.produtos:
            if nome.lower() == produto.nome.lower():
                print('Já existe um produto com esse nome!')
                return
        produto = Produto(nome, preco, estoque, descricao)
        self.produtos.append(produto)
        print('Produto cadastrado com sucesso')

    def listar_produtos(self):
        print(f'{"Nome".ljust(15)} | {"Preço".ljust(15)} | {"Descrição"}')
        for produto in self.produtos:
            print(f'{produto.nome.ljust(15)} | {str(produto.preco).ljust(15)} | {produto.descricao}')

    def selecionar_produto(self, nome):
        for produto in self.produtos:
            if produto.nome.lower() == nome.lower():
                return produto
        print(f"Produto '{nome}' não encontrado.")
        return None

    def inserir_dinheiro(self, valor):
        try:
            valor = float(valor)
            if valor > 0:
                self.dinheiro_inserido += valor
                print(f"Você inseriu R${valor:.2f}. Total inserido: R${self.dinheiro_inserido:.2f}")
            else:
                print("O valor inserido deve ser positivo.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um valor numérico.")

    def comprar_produto(self, produto):
        if produto is None:
            print("Produto não selecionado.")
            return
        if self.dinheiro_inserido >= produto.preco:
            produto.estoque -= 1
            troco = self.dinheiro_inserido - produto.preco
            self.dinheiro_inserido = 0  # Zera o dinheiro inserido após a compra
            print(f"Você comprou {produto.nome}.")
            if troco > 0:
                print(f"Seu troco é de R${troco:.2f}")
        else:
            print(f"Dinheiro insuficiente. Faltam R${produto.preco - self.dinheiro_inserido:.2f}")

    def exibir_estoque(self):
        self.listar_produtos()

# Exemplo

maquina = MaquinaDeVendas()
maquina.cadastrar_produto("Refrigerante", 4.50, 10, 'Coca-cola zero')
maquina.cadastrar_produto("Chips", 3.00, 5, 'Chips de queijo')

maquina.cadastrar_produto("Chocolate", 2.50, 8, 'Chocolate belga, meio amargo')

maquina.exibir_estoque()

produto_selecionado = maquina.selecionar_produto("Refrigerante")
maquina.inserir_dinheiro("5.00")
maquina.comprar_produto(produto_selecionado)

maquina.exibir_estoque()
