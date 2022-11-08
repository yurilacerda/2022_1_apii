class Cliente:
    def __init__(self, nome, cpf, cidade):
        self.nome = nome
        self.cpf = cpf
        self.cidade = cidade

    def imprime(self):
        print("Nome:",self.nome)
        print("CPF:",self.cpf)
        print("Cidade:",self.cidade)