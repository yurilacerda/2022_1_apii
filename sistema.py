from  cadastrocliente import *
from cliente import *
from leentrada import *

cadastro = CadastroCliente()
c1 = le_cliente()
c2 = le_cliente()
cadastro.salvar(c1)
cadastro.salvar(c2)

cadastro.imprime_tudo()