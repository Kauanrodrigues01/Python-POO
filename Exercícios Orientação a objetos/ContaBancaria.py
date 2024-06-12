# Implemente uma classe chamada “Banco” que represente uma instituição financeira. Essa classe deve conter métodos para cadastrar clientes, abrir contas bancárias e realizar operações como saques, depósitos e transferências.

class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

    def ver_informacoes_cliente(self):
        print(f'{self.nome} {self.cpf}')

class ContaBancaria:
    def __init__(self, numero_conta, cliente):
        self.numero_conta = numero_conta
        self.cliente = cliente
        self.saldo = 0.0

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f'Depósito de R${valor:.2f} realizado com sucesso.')
        else:
            print('Valor de depósito inválido.')

    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            print(f'Saque de R${valor:.2f} realizado com sucesso.')
        else:
            print('Saldo insuficiente ou valor de saque inválido.')

    def transferir(self, valor, conta_destino):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            conta_destino.depositar(valor)
            print(f'Transferência de R${valor:.2f} para a conta {conta_destino.numero_conta} realizada com sucesso.')
        else:
            print('Saldo insuficiente ou valor de transferência inválido.')

    def exibir_saldo(self):
        print(f'Saldo atual da conta {self.numero_conta}: R${self.saldo:.2f}')

class Banco:
    def __init__(self, nome):
        self.nome = nome
        self.clientes = []
        self.contas = []
        self.numero_conta_corrente = 1000

    def cadastrar_cliente(self, nome, cpf):
        cliente = Cliente(nome, cpf)
        self.clientes.append(cliente)
        print(f'Cliente {nome} cadastrado com sucesso.')
        return cliente

    def abrir_conta(self, cliente):
        numero_conta = self.numero_conta_corrente
        self.numero_conta_corrente += 1
        conta = ContaBancaria(numero_conta, cliente)
        self.contas.append(conta)
        print(f'Conta {numero_conta} aberta com sucesso para o cliente {cliente.nome}.')
        return conta

    def buscar_conta_por_numero(self, numero_conta):
        for conta in self.contas:
            if conta.numero_conta == numero_conta:
                return conta
        return None
    
    def ver_clientes(self):
        for cliente in self.clientes:
            print(cliente.ver_informacoes_cliente())


banco = Banco('Banco Exemplo')

cliente1 = banco.cadastrar_cliente('João Silva', '12345678900')
cliente2 = banco.cadastrar_cliente('Maria Souza', '09876543211')

banco.ver_clientes()

conta1 = banco.abrir_conta(cliente1)
conta2 = banco.abrir_conta(cliente2)

print(conta1.cliente.nome)

conta1.depositar(1000)
conta1.exibir_saldo()
conta1.sacar(200)
conta1.exibir_saldo()
conta1.transferir(300, conta2)
conta1.exibir_saldo()
conta2.exibir_saldo()