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