from biblioteca.biblioteca2.avaliacao import Avaliacao

class Restaurante:
    restaurantes = []
    def __init__(self, nome, categoria):
        '''É o método construtor da classe, chamado quando uma nova instância da classe é criada.'''
        self.nome = nome
        self.categoria = categoria
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)
        
    def __str__(self):
        ''' É um método especial que define o comportamento da função str() e da função print() quando aplicadas a instâncias da classe Restaurante.'''

        return f'{self.nome.ljust(15)} | {self.categoria.ljust(15)} | {self.ativo.ljust(15)}'
    
    @classmethod 
    def listar_restaurantes(cls): 
        '''@classmethod Indica que o método é um método de classe, o que significa que ele recebe a classe como primeiro argumento em vez da instância.'''
        print(f'{'Nome do restaurante'.ljust(20)} | {'Categoria'.ljust(20)} | {'Avaliação'.ljust(20)} | {'Status'}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante.nome.ljust(20)} | {restaurante.categoria.ljust(20)} | {str(restaurante.media_avaliacoes).ljust(20)} | {restaurante.ativo.ljust(20)}')

    @property
    def ativo(self):
        '''@property Define um método como uma propriedade, permitindo que ele seja acessado como um atributo.'''
        return '✔️' if self._ativo else '❌'
    
    def alternar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        if 0 <= nota <= 10:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)
    
    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return '-'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_notas, 1)
        return media

    def exibir_avaliacoes(self):
        avalicoes = self._avaliacao
        print(f'{'Nome:'.ljust(20)} | {'Avaliação:'}')
        for avaliacao in avalicoes:
            print(f'{avaliacao._cliente.ljsut(20)} | {avaliacao._nota}')
        print(f'{'Média:'.ljust(20)} | {Restaurante.media_avaliacoes}')
            
