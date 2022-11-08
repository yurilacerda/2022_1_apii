class CadastroCliente:

    def __init__(self):
        self.lista = []
        self.tamanho = 0

    def salvar(self, cliente):
        self.lista.append(cliente)
        self.tamanho = len(self.lista)

    def imprime_tudo(self):
        for e in self.lista:
            e.imprime()