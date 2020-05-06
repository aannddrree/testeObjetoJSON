class Cliente:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome

class Produto:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome

class Funcionario:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome

class Venda:
    def __init__(self, id, descricao, produto, funcionario, cliente):
        self.id = id
        self.descricao = descricao
        self.produto = produto
        self.funcionario = funcionario
        self.cliente = cliente
