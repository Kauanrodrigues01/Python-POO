'''Crie uma classe chamada Livro com um construtor que aceita os parâmetros titulo, autor e ano_publicacao. Inicie um atributo chamado disponivel como True por padrão.

Na classe Livro, adicione um método especial str que retorna uma mensagem formatada com o título, autor e ano de publicação do livro. Crie duas instâncias da classe Livro e imprima essas instâncias.

Adicione um método de instância chamado emprestar à classe Livro que define o atributo disponivel como False. Crie uma instância da classe, chame o método emprestar e imprima se o livro está disponível ou não.

Adicione um método estático chamado verificar_disponibilidade à classe Livro que recebe um ano como parâmetro e retorna uma lista dos livros disponíveis publicados nesse ano.

Crie um arquivo chamado class4.py e importe a classe Livro neste arquivo.

No arquivo class4.py, empreste o livro chamando o método emprestar e imprima se o livro está disponível ou não após o empréstimo.

No arquivo class4.py, utilize o método estático verificar_disponibilidade para obter a lista de livros disponíveis publicados em um ano específico.
'''

from biblioteca_class4.biblioteca import Livro

livro1 = Livro('Harry potter', 'J.K howiling', 2017)
livro2 = Livro('O ladrão de Raios', 'José de Alencar', 2017)
livro3 = Livro("Data Science Fundamentals", "Jane Smith", 2020)
Livro.exibir_disponibilidade(2017)