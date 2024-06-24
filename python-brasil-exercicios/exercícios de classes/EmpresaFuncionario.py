'''
Sistema de Gestão de Funcionários e Empresas

Você foi contratado para desenvolver um sistema de gestão de funcionários para uma empresa fictícia chamada "Tech Solutions". Este sistema deve ser capaz de gerenciar informações sobre os funcionários, bem como registrar e administrar funcionários demitidos. O sistema deve ser implementado utilizando classes e métodos em Python.

Requisitos do Sistema
Classe Funcionario:
    Atributos:
        nome (str): Nome do funcionário.
        sexo (str): Sexo do funcionário.
        cpf (str): CPF do funcionário.
        telefone (str): Número de telefone do funcionário.
        salario (float): Salário do funcionário.
        cargo (str): Cargo do funcionário.
        demitido (bool): Status de demissão do funcionário, inicialmente definido como False.
        Métodos:
        alterar_salario(novo_salario): Altera o salário do funcionário.
        alterar_cargo(novo_cargo): Altera o cargo do funcionário.
        atualizar_telefone(novo_telefone): Atualiza o telefone do funcionário.
        ver_salario(): Retorna o salário do funcionário.
        ver_cargo(): Retorna o cargo do funcionário.
        __str__(): Retorna uma representação em string do funcionário com todos os seus atributos.

Classe Empresa:
    Atributos:
        nome_empresa (str): Nome da empresa.
        cnpj (str): CNPJ da empresa.
        endereco (str): Endereço da sede da empresa.
        telefone (str): Número de telefone principal da empresa.
        funcionarios (list): Lista de funcionários ativos.
        funcionarios_demitidos (list): Lista de funcionários demitidos.
        Métodos:
        adicionar_funcionario(nome, sexo, cpf, telefone, salario, cargo): Adiciona um novo funcionário à empresa.
        listar_funcionarios(): Lista todos os funcionários ativos.
        listar_funcionarios_demitidos(): Lista todos os funcionários demitidos.
        procurar_funcionario(nome): Procura um funcionário pelo nome.
        demitir_funcionario(nome): Demite um funcionário, movendo-o para a lista de funcionários demitidos.

Desafios:
    Implemente a classe Funcionario com todos os atributos e métodos descritos.
    Implemente a classe Empresa com todos os atributos e métodos descritos.
    Crie um script de exemplo que faça o seguinte:
    Inicialize uma instância da classe Empresa com alguns funcionários.
    Liste todos os funcionários ativos.
    Procure um funcionário pelo nome e exiba suas informações.
    Demita um funcionário e mova-o para a lista de funcionários demitidos.
    Liste todos os funcionários demitidos.
'''

class Funcionario:
    def __init__(self, nome, sexo, cpf, telefone, salario, cargo) -> None:
        self.nome = nome
        self.sexo = sexo
        self.cpf = cpf
        self.telefone = telefone
        self.salario = salario
        self.cargo = cargo
        self.demitido = False
    
    def alterar_salario(self, novo_salario):
        self.salario = novo_salario
    
    def alterar_cargo(self, novo_cargo):
        self.cargo = novo_cargo
    
    def atualizar_telefone(self, novo_telefone):
        self.telefone = novo_telefone

    def ver_salario(self):
        return self.salario
    
    def ver_cargo(self):
        return self.cargo
    
    def __str__(self):
        status = "Ativo" if not self.demitido else "Demitido"
        return f"Funcionario(Nome: {self.nome}, Cargo: {self.cargo}, Salário: R${self.salario:.2f}, Status: {status})"

    def __repr__(self):
        return self.__str__()

class Empresa:
    def __init__(self, nome_empresa, cnpj, endereco, telefone) -> None:
        """
        Inicializa uma nova instância da classe Empresa.

        Parâmetros:
            nome_empresa (str): O nome da empresa.
            cnpj (str): O CNPJ da empresa.
            endereco (str): O endereço da sede da empresa.
            telefone (str): O número de telefone principal da empresa.
        """
        self.nome_empresa = nome_empresa
        self.cnpj = cnpj
        self.endereco = endereco
        self.telefone = telefone
        self.funcionarios = []
        self.funcionarios_demitidos = []
    
    def adicionar_funcionario(self, nome, sexo, cpf, telefone, salario, cargo):
        funcionario = Funcionario(nome, sexo, cpf, telefone, salario, cargo)
        self.funcionarios.append(funcionario)
        print(f"Funcionário {nome} adicionado com sucesso.")
        return funcionario

    def listar_funcionarios(self):
        if not self.funcionarios:
            print("Nenhum funcionário cadastrado.")
        else:
            print("Funcionários ativos:")
            for funcionario in self.funcionarios:
                print(funcionario)

    def listar_funcionarios_demitidos(self):
        if not self.funcionarios_demitidos:
            print("Nenhum funcionário demitido.")
        else:
            print("Funcionários demitidos:")
            for funcionario in self.funcionarios_demitidos:
                print(funcionario)

    def procurar_funcionario(self, nome):
        for funcionario in self.funcionarios:
            if funcionario.nome.lower() == nome.lower():
                return funcionario
        return None

    def demitir_funcionario(self, nome):
        funcionario = self.procurar_funcionario(nome)
        if funcionario:
            funcionario.demitido = True
            self.funcionarios.remove(funcionario)
            self.funcionarios_demitidos.append(funcionario)
            print(f"Funcionário {nome} demitido com sucesso e movido para a lista de funcionários demitidos.")
        else:
            print(f"Funcionário com nome {nome} não encontrado.")

# Exemplo:
empresa = Empresa(
    nome_empresa="Tech Solutions",
    cnpj="12.345.678/0001-99",
    endereco="Av. Paulista, 1234, São Paulo, SP",
    telefone="(11) 1234-5678"
)

empresa.adicionar_funcionario(
    nome="Alice Souza",
    sexo="Feminino",
    cpf="123.456.789-00",
    telefone="(11) 9999-8888",
    salario=6000.00,
    cargo="Desenvolvedora"
)

empresa.adicionar_funcionario(
    nome="Bruno Lima",
    sexo="Masculino",
    cpf="987.654.321-00",
    telefone="(11) 8888-7777",
    salario=4000.00,
    cargo="Analista de RH"
)

print("\nLista de Funcionários:")
empresa.listar_funcionarios()

# procurando pelo nome
nome_procurado = "Alice Souza"
funcionario_encontrado = empresa.procurar_funcionario(nome_procurado)
if funcionario_encontrado:
    print(f"\nFuncionário encontrado: {funcionario_encontrado}")
else:
    print(f"\nFuncionário com nome {nome_procurado} não encontrado.")

# demitindo funcionário
empresa.demitir_funcionario("Alice Souza")
print("\nLista de Funcionários após demissão:")
empresa.listar_funcionarios()

print("\nLista de Funcionários Demitidos:")
empresa.listar_funcionarios_demitidos()