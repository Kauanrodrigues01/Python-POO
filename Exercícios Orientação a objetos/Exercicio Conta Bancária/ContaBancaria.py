class Deposito:
    def __init__(self, conta, valor, limite_deposito):
        self.conta = conta
        self.valor = valor
        self.limite_deposito = limite_deposito

    def realizar(self):
        if self.valor <= 0:
            print('O valor de depósito deve ser positivo.')
            return

        if self.conta.quant_depositos_realizados >= 2:
            self.limite_deposito = 2000
        if self.conta.quant_depositos_realizados >= 4:
            self.limite_deposito = 3000

        if self.valor > self.limite_deposito:
            print('Esse valor excedeu o seu limite para depósito.')
        else:
            self.conta.quant_depositos_realizados += 1
            self.conta._extrato.append(f'+ R${self.valor:.2f}')
            self.conta.saldo += self.valor
            print(f'Valor R${self.valor:.2f} foi depositado!')
            self.conta.exibir_saldo()


class Saque:
    TAXA_SAQUE = 0.05

    def __init__(self, conta, valor, limite_saque):
        self.conta = conta
        self.valor = valor
        self.limite_saque = limite_saque

    def realizar(self):
        if self.valor <= 0:
            print('O valor de saque deve ser positivo.')
            return

        if self.conta.quant_saques_realizados >= 2:
            self.limite_saque = 2000
        if self.conta.quant_saques_realizados >= 4:
            self.limite_saque = 3000

        taxa = self.valor * self.TAXA_SAQUE
        valor_com_taxa = self.valor + taxa
        print(f'O valor com a taxa é de R${taxa:.2f}')

        confirmacao = 's'  # Para testes, assumimos que a confirmação é sempre 's'
        if confirmacao == 's':
            if valor_com_taxa > self.conta.saldo:
                print('Saldo insuficiente!')
            else:
                self.conta.saque_total += self.valor
                if self.conta.saque_total > self.limite_saque:
                    print('Você excedeu os limites do seu saque diário, confira seus limites.')
                else:
                    self.conta.quant_saques_realizados += 1
                    self.conta._extrato.append(f'- R${valor_com_taxa:.2f}')
                    self.conta.saldo -= valor_com_taxa
                    print(f'Valor R${self.valor:.2f} foi sacado, com taxa de: R${taxa:.2f}')
                    self.conta.exibir_saldo()
        else:
            print('Saque cancelado.')


class ContaBancaria:
    def __init__(self, nome_titular, saldo):
        self.nome_titular = nome_titular
        self.saldo = saldo
        self.saque_total = 0
        self.limite_deposito = 1000
        self.limite_saque = 1000
        self.quant_depositos_realizados = 0
        self.quant_saques_realizados = 0
        self._extrato = []
    
    def __str__(self) -> str:
        return f'Nome: {self.nome_titular} | Saldo: R${self.saldo:.2f}'
    
    def exibir_saldo(self):
        print(f'O saldo do {self.nome_titular} é de: R${self.saldo:.2f}')

    def exibir_extrato(self):
        print(f'Extrato da conta de {self.nome_titular}:')
        for transacao in self._extrato:
            print(transacao)

    def transferir(self, valor_transferencia, conta_destino):
        if valor_transferencia <= 0:
            print('O valor de transferência deve ser positivo.')
            return
        if valor_transferencia > self.saldo:
            print('Saldo insuficiente.')
        else:
            self._extrato.append(f'- R${valor_transferencia:.2f} (transferência)')
            self.saldo -= valor_transferencia
            conta_destino.depositar(valor_transferencia)
            print(f'Transferência de R${valor_transferencia:.2f} realizada para {conta_destino.nome_titular}')

    def depositar(self, valor):
        deposito = Deposito(self, valor, self.limite_deposito)
        deposito.realizar()

    def sacar(self, valor):
        saque = Saque(self, valor, self.limite_saque)
        saque.realizar()

    def aumentar_limite_deposito(self, valor):
        self.limite_deposito += valor

    def visualizar_limite_deposito(self):
        print(f'O seu limite de deposito atual é de R${self.limite_deposito}')

    def aumentar_limite_saque(self, valor):
        self.limite_saque += valor

    def visualizar_limite_saque(self):
        print(f'O seu limite de saque atual é de R${self.limite_saque}')


# Função de testes
def testes():
    print("\n--- Teste Inicial ---")
    conta1 = ContaBancaria('Carlos', 0)
    conta2 = ContaBancaria('José', 4000)
    print(conta1)
    print(conta2)

    print("\n--- Teste de Transferência ---")
    conta2.transferir(4000, conta1)
    conta1.exibir_saldo()
    conta2.exibir_saldo()

    print("\n--- Teste de Saque ---")
    conta1.sacar(3000)
    conta1.exibir_saldo()

    print("\n--- Teste de Transferência Insuficiente ---")
    conta1.transferir(1000, conta2)
    conta1.exibir_saldo()
    conta2.exibir_saldo()

    print("\n--- Teste de Extrato ---")
    conta1.exibir_extrato()

    print("\n--- Teste de Depósito Excedendo Limite ---")
    conta1.depositar(1500)
    conta1.exibir_saldo()

    print("\n--- Teste de Depósito Válido ---")
    conta1.depositar(500)
    conta1.exibir_saldo()

    print("\n--- Teste de Saque Excedendo Limite ---")
    conta1.sacar(1500)
    conta1.exibir_saldo()

    print("\n--- Teste de Depósito Ajustando Limite ---")
    conta1.depositar(1000)
    conta1.depositar(1000)
    conta1.depositar(1000)
    conta1.exibir_saldo()
    conta1.depositar(2500)
    conta1.exibir_saldo()

    print("\n--- Teste de Saque Ajustando Limite ---")
    conta1.sacar(500)
    conta1.sacar(500)
    conta1.sacar(500)
    conta1.sacar(500)
    conta1.sacar(1000)
    conta1.exibir_saldo()

# Executar os testes
testes()
