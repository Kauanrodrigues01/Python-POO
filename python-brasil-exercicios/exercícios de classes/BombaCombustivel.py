'''
Classe Bomba de Combustível: Faça um programa completo utilizando classes e métodos que:

Possua uma classe chamada bombaCombustível, com no mínimo esses atributos:
    tipoCombustivel.
    valorLitro
    quantidadeCombustivel
Possua no mínimo esses métodos:
    abastecerPorValor( ) – método onde é informado o valor a ser abastecido e mostra a quantidade de litros que foi colocada no veículo
    abastecerPorLitro( ) – método onde é informado a quantidade em litros de combustível e mostra o valor a ser pago pelo cliente.
    alterarValor( ) – altera o valor do litro do combustível.
    alterarCombustivel( ) – altera o tipo do combustível.
    alterarQuantidadeCombustivel( ) – altera a quantidade de combustível restante na bomba.
'''

class BombaCombustivel:
    """
    Classe que representa uma bomba de combustível.

    Atributos:
        tipo_combustivel (str): O tipo de combustível da bomba (ex: Gasolina, Diesel).
        valor_litro (float): O valor por litro do combustível.
        qntd_combustivel (float): A quantidade de combustível disponível na bomba.

    Métodos:
        __init__(tipo_combustivel, valor_litro, quantidade_combustivel): Inicializa uma nova instância da classe BombaCombustivel.
        __str__(): Retorna uma string representando os atributos da bomba de combustível.
        abastecer_por_preco(valor): Abastece o veículo com combustível baseado no valor fornecido.
        abastacer_por_litro(qntd_litros): Abastece o veículo com a quantidade de litros fornecida.
        alterar_valor_do_combustivel(valor): Altera o valor por litro do combustível.
        alterar_tipo_do_combustivel(novo_tipo): Altera o tipo de combustível da bomba.
        alterar_quantidade_do_combustivel(nova_qntd): Altera a quantidade de combustível disponível na bomba.
    """

    def __init__(self, tipo_combustivel, valor_litro, quantidade_combustivel) -> None:
        """
        Inicializa uma nova instância da classe BombaCombustivel.

        Parâmetros:
            tipo_combustivel (str): O tipo de combustível da bomba.
            valor_litro (float): O valor por litro do combustível.
            quantidade_combustivel (float): A quantidade de combustível disponível na bomba.
        """
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = valor_litro
        self.qntd_combustivel = quantidade_combustivel
    
    def __str__(self):
        """
        Retorna uma string representando os atributos da bomba de combustível.

        Retorno:
            str: Representação em string dos atributos da bomba de combustível.
        """
        return f'{self.tipo_combustivel, self.valor_litro, self.qntd_combustivel}'

    def abastecer_por_preco(self, valor):
        """
        Abastece o veículo com combustível baseado no valor fornecido.

        Parâmetros:
            valor (float): O valor a ser abastecido.

        Exibe:
            str: Quantidade de litros abastecidos ou mensagem de combustível insuficiente.
        """
        qntd_litros = valor / self.valor_litro 
        if qntd_litros <= self.qntd_combustivel:
            print('Foram abastecidos {} litros'.format(round(qntd_litros, 2)))
            self.qntd_combustivel -= qntd_litros
        else:
            print('Combustível insuficiente')

    def abastacer_por_litro(self, qntd_litros):
        """
        Abastece o veículo com a quantidade de litros fornecida.

        Parâmetros:
            qntd_litros (float): A quantidade de litros a ser abastecida.

        Exibe:
            str: Valor a ser pago pelo cliente ou mensagem de combustível insuficiente.
        """
        if qntd_litros <= self.qntd_combustivel:
            valor = qntd_litros * self.valor_litro
            print(f'Valor a pagar {valor:.2f}')
            self.qntd_combustivel -= qntd_litros
        else:
            print('Combustível insuficiente')

    def alterar_valor_do_combustivel(self, valor):
        """
        Altera o valor por litro do combustível.

        Parâmetros:
            valor (float): O novo valor por litro do combustível.
        """
        self.valor_litro = valor

    def alterar_tipo_do_combustivel(self, novo_tipo):
        """
        Altera o tipo de combustível da bomba.

        Parâmetros:
            novo_tipo (str): O novo tipo de combustível.
        """
        self.tipo_combustivel = novo_tipo
    
    def alterar_quantidade_do_combustivel(self, nova_qntd):
        """
        Altera a quantidade de combustível disponível na bomba.

        Parâmetros:
            nova_qntd (float): A nova quantidade de combustível.
        """
        self.qntd_combustivel = nova_qntd

# Exemplo:
bomba = BombaCombustivel("Gasolina", 5.49, 1000)
bomba.abastecer_por_preco(100)
bomba.abastacer_por_litro(20) 
bomba.alterar_valor_do_combustivel(5.59)   
bomba.alterar_tipo_do_combustivel("Diesel")
bomba.alterar_quantidade_do_combustivel(500)
print(bomba)
