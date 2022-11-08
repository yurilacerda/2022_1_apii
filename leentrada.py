from cliente import * 

def le_cliente():
    nome = input("Nome:")
    cpf = input("CPF:")
    cidade = input("Cidade:")
    return Cliente(nome, cpf, cidade)