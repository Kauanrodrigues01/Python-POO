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