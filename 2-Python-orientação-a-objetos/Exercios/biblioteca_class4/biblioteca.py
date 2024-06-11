# class importada para class4.py
class Livro:
    livros = []
    def __init__(self, titulo, autor, ano_publicacao) -> None:
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self._disponivel = True
        Livro.livros.append(self)

    def __str__(self):
        return f'nome: {self.titulo} | {self.autor} | {self.ano_publicacao} | {self._disponivel}'
    
    def emprestar(self):
        self._disponivel = False

    @staticmethod
    def verificar_disponibilidade(ano):
        livros_disponiveis = [livro for livro in Livro.livros if livro.ano_publicacao == int(ano) and livro._disponivel]
        return livros_disponiveis
    
    @staticmethod
    def exibir_disponibilidade(ano):
        lista = Livro.verificar_disponibilidade(ano)
        print('Livros disponíveis:')
        for livro in lista:
            print(f'{livro.titulo}')