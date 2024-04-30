

# separar acoes em funcoes unicas com duas novas
# cadastrar usuario (cliente) e cadastrar conta bancaria (conta para esse cliente)
# armazenar usuarios em uma lista, composto por nome, data de nascimento, cpf e endereco
# endereço(str) em formato string Rua, numero - bairro - cidade/sigla estado. cpf só o numero
# cadastrar_usuario: não pode haver numeros duplicados de CPF (string)para vincular um
# usuario a uma conta, filtrar lista por CPF.
'''rev01:

parei na correção da linha 168, agencia key error
falta adicionar extrato
falta adicionar limite de saques diario

as funcoes devem fazer passagem de argumentos por posicao e nomeados (variar os casos)

Saque: argumentos: keyword only: saque(saldo="variavel_saldo"...)
Saque: usar argumentos: (saldo, valor, extrato, limite, numero_saques,limite_saques)
Saque: retornos: saldo e extrato

deposito: argumentos: positional only: deposito(saldo,valor...)
deposito: saldo, valor, extrato
deposito: retornos: saldo e extrato

extrato: positional only e keywork only: extrato(saldo,extrato="variavel_extrato")

conta em uma lista, coposta por agencia, numero da conta e usuario, contas sequenciais
começa em 1, agencia fixo 0001,cada usuario pode ter mais de uma conta, mas uma conta não
pode ser de dois usuarios, não pode haver conta sem usuario.

lista_usuarios = [{"cpf":"05843914712",
                   "nome":"André Filipe Guering de Mattos",
                   "nascimento":"14/05/1990",
                   "endereço":"Rua Roberto Fritzgerald Kennedy,40 - Cavaleiros - Macaé/RJ"}]
lista_contas = [{"conta":1,
                 "agencia":"0001",
                 "cpf":"05843914712",
                 "saldo":100,
                 "cheque_especial":100,
                 "n_saques":0
                 "extrato":""
                 }]
                 
'''

#def saque(saldo="saldo",valor="valor",extrato="extrato",limite="limite",numero_saques="",
#limite_saques="")