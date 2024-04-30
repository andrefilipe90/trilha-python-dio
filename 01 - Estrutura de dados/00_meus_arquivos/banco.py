

# separar acoes em funcoes unicas com duas novas
# cadastrar usuario (cliente) e cadastrar conta bancaria (conta para esse cliente)
# armazenar usuarios em uma lista, composto por nome, data de nascimento, cpf e endereco
# endereço(str) em formato string Rua, numero - bairro - cidade/sigla estado. cpf só o numero

'''rev01:

as funcoes devem fazer passagem de argumentos por posicao e nomeados (variar os casos)

cadastrar_usuario: não pode haver numeros duplicados de CPF (string)para vincular um
usuario a uma conta, filtrar lista por CPF.

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
'''

#def saque(saldo="saldo",valor="valor",extrato="extrato",limite="limite",numero_saques="",
#limite_saques="")