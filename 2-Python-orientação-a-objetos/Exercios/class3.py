'''
-Crie uma classe chamada ContaBancaria com um construtor que aceita os parâmetros titular e saldo. Inicie o atributo ativo como False por padrão.
-Na classe ContaBancaria, adicione um método especial __str__ que retorna uma mensagem formatada com o titular e o saldo da conta. Crie duas instâncias da classe e    imprima essas instâncias.
-Adicione um método de classe chamado ativar_conta à classe ContaBancaria que define o atributo ativo como True. Crie uma instância da classe, chame o método de classe e imprima o valor de ativo.
'''

class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        self._ativo = False

    def __str__(self):
        return f'Conta de {self.titular} - Saldo: R${self.saldo}'
    
    @classmethod
    def ativar_conta(cls, conta):
        '''O nome "conta" pode ser substituido por "self" é apenas para representar melhor'''
        conta._ativo = True

# Crie uma instância da classe, chame o método de classe e imprima o valor de ativo.
conta = ContaBancaria('Kauan', 2000)
print(f"\nAntes de ativar: Conta ativa? {conta._ativo}")
ContaBancaria.ativar_conta(conta)
print(f"Depois de ativar: Conta ativa? {conta._ativo}\n")

'''
- Refatore a classe ContaBancaria para utilizar a abordagem "pythonica" na criação de atributos. Utilize propriedades, se necessário.
- Crie uma instância da classe e imprima o valor da propriedade titular.
'''

class ContaBancariaPythonica:
    def __init__(self, titular, saldo):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False

    @property
    def titular(self):
        return self._titular

    @property
    def saldo(self):
        return self._saldo

    @property
    def ativo(self):
        return self._ativo

conta2 = ContaBancariaPythonica("Fernanda", 1500)
print(f"Titular da conta 2: {conta2.titular}")

'''
-Crie uma classe chamada ClienteBanco com um construtor que aceita 5 atributos. Instancie 3 objetos desta classe e atribua valores aos seus atributos através do método construtor.
-Crie um método de classe para a conta ClienteBanco.
'''
class ClienteBanco:
    def __init__(self,nome,idade,endereco,cpf, profissao):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
        self.cpf = cpf
        self.profissao = profissao
    @classmethod
    def criar_conta(cls, titular, saldo_inicial):
        conta = ContaBancariaPythonica(titular, saldo_inicial)
        return conta

cliente1 = ClienteBanco("Ana", 30, "Rua A", "123.456.789-01", "Backend")
cliente2 = ClienteBanco("Luiza", 25, "Rua B", "987.654.321-01", "Estudante")
cliente3 = ClienteBanco("Vinny Neves", 40, "Rua C", "111.222.333-44", "Frontend")

conta_cliente1 = ClienteBanco.criar_conta(cliente1.nome, 2000)
print(f"Conta de {conta_cliente1.titular} criada com saldo inicial de R${conta_cliente1.saldo}")
