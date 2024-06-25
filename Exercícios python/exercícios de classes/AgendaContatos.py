# Implemente uma classe chamada “Agenda” que represente uma agenda telefônica. Essa classe deve permitir adicionar, editar e remover contatos, além de buscar por contatos a partir de um nome ou número de telefone.

class Contato:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone
    
    def ver_contato(self):
        print(f'Nome: {self.nome} | Número: {self.telefone}')

class AgendaTelefonica:
    def __init__(self):
        self.contatos = []

    def adicionar_contato(self, nome, telefone):
        if telefone.isdigit():
            contato = Contato(nome, telefone)
            self.contatos.append(contato)
            print(f'O contato {contato.nome} foi adicionado')
            return contato
        else:
            print("Número de telefone inválido. Deve conter apenas dígitos.")

    def buscar_contato_por_nome(self, nome):
        contatos_encontrados = [contato for contato  in self.contatos if contato.nome.lower() == nome.lower()]
        return contatos_encontrados
    
    def buscar_contato_por_telefone(self, telefone):
        contatos_encontrados = [contato for contato  in self.contatos if contato.telefone == telefone]
        return contatos_encontrados

    def remover_contato(self, nome):
        contatos_encontrados = self.buscar_contato_por_nome(nome)
        
        if not contatos_encontrados:
            print(f"Nenhum contato encontrado com o nome '{nome}'.")
            return

        if len(contatos_encontrados) > 1:
            num = 1
            print("Contatos encontrados:")
            for contato in contatos_encontrados:
                print(f'{num}. {contato.nome.ljust(15)} | {contato.telefone}')
                num += 1
            
            numero_remover = input('Digite o número que representa o contato que você quer remover: ')

            try:
                numero_remover = int(numero_remover)
                if 1 <= numero_remover <= len(contatos_encontrados):

                    contato_remover = contatos_encontrados[numero_remover - 1]

                    self.contatos.remove(contato_remover)
                    print(f"Contato '{contato_remover.nome}' removido com sucesso.")

                else:
                    print('Número inválido.')

            except ValueError:
                print('Entrada inválida. Digite um número.')
        else:
            contato_remover = contatos_encontrados[0]
            self.contatos.remove(contato_remover)
            print(f"Contato '{contato_remover.nome}' removido com sucesso.")
    
    def editar_contato(self, nome):
        contatos_encontrados = self.buscar_contato_por_nome(nome)

        if not contatos_encontrados:
            print(f"Nenhum contato encontrado com o nome '{nome}'.")
            return

        if len(contatos_encontrados) > 1:
            num = 1
            print("Contatos encontrados:")
            for contato in contatos_encontrados:
                print(f'{num}. {contato.nome.ljust(15)} | {contato.telefone}')
                num += 1

            num_editar = input('Digite o número que representa o contato que você quer remover: ')

            try:
                num_editar = int(num_editar)

                if  1 <= num_editar <= len(contatos_encontrados):

                    contato_editar = contatos_encontrados[num_editar - 1]

                    novo_nome = input('Digite o novo nome do seu Contato: ')
                    novo_telefone = input('Digite o novo telefone: ')

                    if novo_telefone.isdigit():
                        contato_editar.nome = str(novo_nome)
                        contato_editar.telefone = novo_telefone
                    else:
                        print("Número de telefone inválido. Deve conter apenas dígitos.")

                else: 
                    print('Número inválido')

            except ValueError:
                print('Número inválido')        

    def listar_contatos(self):
        print("Lista de Contatos:")
        for i, contato in enumerate(self.contatos, start=1):
            print(f'{i}. {contato.nome.ljust(15)} | {contato.telefone}')



agenda = AgendaTelefonica()


agenda.adicionar_contato('José', '85994324916')
agenda.adicionar_contato('Maria', '81987456321')


agenda.listar_contatos()


contatos_jose = agenda.buscar_contato_por_nome('José')
print("Contatos encontrados com nome 'José':")
for contato in contatos_jose:
    contato.ver_contato()


contatos_telefone = agenda.buscar_contato_por_telefone('85994324916')
print("Contatos encontrados com telefone '85994324916':")
for contato in contatos_telefone:
    contato.ver_contato()


agenda.remover_contato('Maria')
agenda.listar_contatos()
agenda.editar_contato('José')
agenda.listar_contatos()