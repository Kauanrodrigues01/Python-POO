class Aluno:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self._notas = []
        self.media = 0

    def adicionar_notas(self, nota):
        if 0 <= nota <= 10:
            self._notas.append(nota)
        else:
            print("Nota inválida. Insira uma nota entre 0 e 10.")

    def calcular_media(self):
        if not self._notas:
            print("Nenhuma nota disponível para calcular a média.")
            return 0
        notas = sum(self._notas)
        media = notas / len(self._notas)
        media = round(media, 2)
        self.media = media
        print(f'A média atual do aluno é de {self.media}')

    def mostrar_notas(self):
        if len(self._notas) > 0:
            print(f'Notas do aluno {self.nome}')
            for nota in self._notas:
                print(nota)
        else:
            print('O aluno não tem notas para serem exibidas')

aluno1 = Aluno('Jose', 2345678)
aluno1.adicionar_notas(10)
aluno1.adicionar_notas(7.66)
aluno1.calcular_media()
aluno1.adicionar_notas(10)
aluno1.calcular_media()