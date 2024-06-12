# Crie uma classe chamada “Pessoa” que possua atributos para armazenar nome, idade e profissão. Implemente métodos para calcular a idade em anos bissextos e exibir informações da pessoa.
import datetime

class Pessoa:
    def __init__(self, nome, idade, profissao, data_nascimento):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao
        self.data_nascimento = data_nascimento

    def calcular_idade_bissexta(self):
        # Verifica se a data de nascimento é 29 de fevereiro
        dia, mes, ano = self.data_nascimento.day, self.data_nascimento.month, self.data_nascimento.year
        aniversarios_bissextos = 0

        if dia == 29 and mes == 2:
            ano_atual = datetime.date.today().year
            for ano in range(ano, ano_atual + 1):
                if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
                    aniversarios_bissextos += 1
        
        return aniversarios_bissextos

    def exibir_informacoes(self):
        aniversarios_bissextos = self.calcular_idade_bissexta()
        print(f'Nome: {self.nome}')
        print(f'Idade: {self.idade} anos')
        print(f'Profissão: {self.profissao}')
        print(f'Aniversários bissextos: {aniversarios_bissextos}')

# Exemplo de uso da classe
'''
pessoa1 = Pessoa('Ana', 30, 'Engenheira', datetime.date(1992, 2, 29))
pessoa1.exibir_informacoes()
'''



