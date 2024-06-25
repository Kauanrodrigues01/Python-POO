import datetime
import os
import pickle
import sys

class Tarefa:
    """
    Uma classe que representa uma tarefa com título, descrição, data de vencimento e status de conclusão.

    Atributos:
    titulo (str): O título da tarefa.
    descricao (str): A descrição da tarefa.
    data_vencimento (datetime.date): A data de vencimento da tarefa.
    concluida (bool): O status de conclusão da tarefa.
    """

    def __init__(self, titulo, descricao, data_vencimento):
        self.titulo = titulo
        self.descricao = descricao
        self.data_vencimento = data_vencimento
        self.concluida = False

    def __str__(self):
        status = 'Concluída' if self.concluida else 'Pendente'
        return f"{self.titulo} (Vencimento: {self.data_vencimento}) - {status}\n{self.descricao}"

class GerenciadorDeTarefas:
    """
    Uma classe para gerenciar tarefas, permitindo operações como adicionar, visualizar, atualizar, excluir e salvar tarefas.

    Atributos:
    nome_arquivo (str): O nome do arquivo onde as tarefas são salvas.
    tarefas (list): A lista de tarefas.
    """

    def __init__(self, nome_arquivo='tarefas.pkl'):
        self.nome_arquivo = nome_arquivo
        self.tarefas = self.carregar_tarefas()

    def carregar_tarefas(self):
        """
        Carrega tarefas de um arquivo usando pickle.

        Retorna:
        list: A lista de tarefas carregadas do arquivo, ou uma lista vazia se o arquivo não existir.
        """
        if os.path.exists(self.nome_arquivo):
            with open(self.nome_arquivo, 'rb') as f:
                return pickle.load(f)
        return []

    def salvar_tarefas(self):
        """
        Salva a lista atual de tarefas em um arquivo usando pickle.
        """
        with open(self.nome_arquivo, 'wb') as f:
            pickle.dump(self.tarefas, f)

    def adicionar_tarefa(self):
        """
        Adiciona uma nova tarefa solicitando os detalhes da tarefa ao usuário e salvando a tarefa.
        """
        titulo = input("Título: ")
        descricao = input("Descrição: ")
        data_vencimento = input("Data de Vencimento (AAAA-MM-DD): ")
        try:
            data_vencimento = datetime.datetime.strptime(data_vencimento, "%Y-%m-%d").date()
        except ValueError:
            print("Formato de data inválido. Tarefa não adicionada.")
            return
        tarefa = Tarefa(titulo, descricao, data_vencimento)
        self.tarefas.append(tarefa)
        self.salvar_tarefas()
        print("Tarefa adicionada com sucesso.")

    def visualizar_tarefas(self):
        """
        Exibe todas as tarefas com seus detalhes.
        """
        if not self.tarefas:
            print("Nenhuma tarefa disponível.")
            return
        for i, tarefa in enumerate(self.tarefas, start=1):
            print(f"{i}. {tarefa}")

    def atualizar_tarefa(self):
        """
        Atualiza uma tarefa existente solicitando ao usuário o número da tarefa e os novos detalhes.
        """
        if not self.tarefas:
            print("Nenhuma tarefa disponível para atualizar.")
            return
        self.visualizar_tarefas()
        try:
            numero_tarefa = int(input("Digite o número da tarefa para atualizar: "))
            if numero_tarefa < 1 or numero_tarefa > len(self.tarefas):
                print("Número da tarefa inválido.")
                return
        except ValueError:
            print("Entrada inválida.")
            return
        tarefa = self.tarefas[numero_tarefa - 1]
        print(f"Atualizando tarefa: {tarefa}")
        tarefa.titulo = input(f"Novo título (deixe em branco para manter '{tarefa.titulo}'): ") or tarefa.titulo
        tarefa.descricao = input(f"Nova descrição (deixe em branco para manter a atual): ") or tarefa.descricao
        data_vencimento = input(f"Nova data de vencimento (AAAA-MM-DD, deixe em branco para manter '{tarefa.data_vencimento}'): ")
        if data_vencimento:
            try:
                tarefa.data_vencimento = datetime.datetime.strptime(data_vencimento, "%Y-%m-%d").date()
            except ValueError:
                print("Formato de data inválido. Data não alterada.")
        self.salvar_tarefas()
        print("Tarefa atualizada com sucesso.")

    def excluir_tarefa(self):
        """
        Exclui uma tarefa existente solicitando ao usuário o número da tarefa.
        """
        if not self.tarefas:
            print("Nenhuma tarefa disponível para excluir.")
            return
        self.visualizar_tarefas()
        try:
            numero_tarefa = int(input("Digite o número da tarefa para excluir: "))
            if numero_tarefa < 1 or numero_tarefa > len(self.tarefas):
                print("Número da tarefa inválido.")
                return
        except ValueError:
            print("Entrada inválida.")
            return
        tarefa = self.tarefas.pop(numero_tarefa - 1)
        self.salvar_tarefas()
        print(f"Tarefa '{tarefa.titulo}' excluída com sucesso.")

    def marcar_tarefa_concluida(self):
        """
        Marca uma tarefa existente como concluída solicitando ao usuário o número da tarefa.
        """
        if not self.tarefas:
            print("Nenhuma tarefa disponível para marcar como concluída.")
            return
        self.visualizar_tarefas()
        try:
            numero_tarefa = int(input("Digite o número da tarefa para marcar como concluída: "))
            if numero_tarefa < 1 or numero_tarefa > len(self.tarefas):
                print("Número da tarefa inválido.")
                return
        except ValueError:
            print("Entrada inválida.")
            return
        self.tarefas[numero_tarefa - 1].concluida = True
        self.salvar_tarefas()
        print("Tarefa marcada como concluída.")

    def limpar_tarefas_concluidas(self):
        """
        Limpa todas as tarefas que foram marcadas como concluídas após confirmação do usuário.
        """
        tarefas_concluidas = [tarefa for tarefa in self.tarefas if tarefa.concluida]
        if not tarefas_concluidas:
            print("Nenhuma tarefa concluída para limpar.")
            return
        print("Tarefas Concluídas:")
        self.visualizar_tarefas()
        confirmacao = input("Tem certeza que deseja limpar todas as tarefas concluídas? (sim/não): ").strip().lower()
        if confirmacao == 'sim':
            self.tarefas[:] = [tarefa for tarefa in self.tarefas if not tarefa.concluida]
            self.salvar_tarefas()
            print("Tarefas concluídas limpas com sucesso.")
        else:
            print("Operação cancelada.")

    def buscar_tarefas(self):
        """
        Busca tarefas por palavra-chave no título ou descrição.
        """
        palavra_chave = input("Digite a palavra-chave para buscar nas tarefas: ").lower()
        tarefas_encontradas = [tarefa for tarefa in self.tarefas if palavra_chave in tarefa.titulo.lower() or palavra_chave in tarefa.descricao.lower()]
        if not tarefas_encontradas:
            print("Nenhuma tarefa encontrada com a palavra-chave.")
        else:
            print(f"Encontrada(s) {len(tarefas_encontradas)} tarefa(s) com a palavra-chave:")
            for tarefa in tarefas_encontradas:
                print(tarefa)

    def mostrar_estatisticas_tarefas(self):
        """
        Exibe estatísticas sobre o total de tarefas, tarefas concluídas e tarefas pendentes.
        """
        total_tarefas = len(self.tarefas)
        tarefas_concluidas = sum(1 for tarefa in self.tarefas if tarefa.concluida)
        tarefas_pendentes = total_tarefas - tarefas_concluidas
        print(f"Total de Tarefas: {total_tarefas}")
        print(f"Tarefas Concluídas: {tarefas_concluidas}")
        print(f"Tarefas Pendentes: {tarefas_pendentes}")

    def salvar_e_sair(self):
        """
        Salva todas as tarefas e sai do programa.
        """
        self.salvar_tarefas()
        print("Tarefas salvas com sucesso.")
        sys.exit()

    def exibir_menu(self):
        """
        Exibe o menu principal de opções do gerenciador de tarefas.
        """
        print("\nGerenciador de Tarefas")
        print("1. Adicionar Tarefa")
        print("2. Visualizar Tarefas")
        print("3. Atualizar Tarefa")
        print("4. Excluir Tarefa")
        print("5. Marcar Tarefa como Concluída")
        print("6. Limpar Tarefas Concluídas")
        print("7. Buscar Tarefas")
        print("8. Mostrar Estatísticas das Tarefas")
        print("9. Salvar e Sair")

    def executar(self):
        """
        Executa o gerenciador de tarefas, exibindo o menu e lidando com a entrada do usuário.
        """
        while True:
            self.exibir_menu()
            escolha = input("Escolha uma opção: ")
            if escolha == '1':
                self.adicionar_tarefa()
            elif escolha == '2':
                self.visualizar_tarefas()
            elif escolha == '3':
                self.atualizar_tarefa()
            elif escolha == '4':
                self.excluir_tarefa()
            elif escolha == '5':
                self.marcar_tarefa_concluida()
            elif escolha == '6':
                self.limpar_tarefas_concluidas()
            elif escolha == '7':
                self.buscar_tarefas()
            elif escolha == '8':
                self.mostrar_estatisticas_tarefas()
            elif escolha == '9':
                self.salvar_e_sair()
            else:
                print("Escolha inválida. Insira uma opção valida, por favor.")

if __name__ == "__main__":
    task_manager = GerenciadorDeTarefas()
    task_manager.executar()
           
