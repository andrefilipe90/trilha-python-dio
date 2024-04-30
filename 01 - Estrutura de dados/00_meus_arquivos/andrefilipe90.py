import os

def limpa_tela():
    os.system('cls || clear')

limpa_tela()

conta_ativa = {}
usuario_ativo = {}
lista_usuarios = [{"cpf":"05843914712",
                   "nome":"André Filipe Guering de Mattos",
                   "nascimento":"14/05/1990",
                   "endereço":"Rua Roberto Fritzgerald Kennedy,40 - Cavaleiros - Macaé/RJ"}]
lista_contas = [{"conta":1,
                 "agencia":"0001",
                 "cpf":"05843914712",
                 "saldo":100,
                 "cheque_especial":100}] #definir tipo
cad_usuario = " Cadastro Usuario "
cad_conta = " Cadastro Conta "
depositar = " Depositar "
sacar = " Sacar "
extrato = " Extrato "
sair = " Sair "

menu = f"""
##############################

[1] {cad_usuario.center(26,"#")}
[2] {cad_conta.center(26,"#")}
[3] {depositar.center(26,"#")}
[4] {sacar.center(26,"#")}
[5] {extrato.center(26,"#")}
[6] {sair.center(26,"#")}

=> """

def cadastrar_usuario(cpf):
    limpa_tela()
    temp_cpf = teste_cpf(cpf)
    if temp_cpf == cpf:
        return
    temp_nome = input("Informe o nome:")
    temp_nascimento = input("informe a data de nascimento dd/mm/aaaa:")
    temp_endereco = input("informe o endereço: rua, nº - bairro - cidade/ES:")
    temp_dict = {"cpf":temp_cpf,"nome":temp_nome,"nascimento":temp_nascimento,"endereço":temp_endereco}
    lista_usuarios.append(temp_dict)
    criar_conta = input("gostaria de criar uma conta? [s]sim ou [n]não:")
    if criar_conta == "s":
        cadastrar_conta(agencia="0001",cpf=temp_cpf)
        return
    elif criar_conta == "n":
        return
    else:
        print("opção não encontrada, retornando ao menu:")
    return

def cadastrar_conta(cpf,agencia):
    limpa_tela()
    temp_agencia = agencia
    cpf_valido = teste_cpf(cpf)
    if cpf_valido == cpf:
        for usuario in lista_usuarios:
            if usuario["cpf"] == cpf:
                temp_conta= 1+ int(lista_contas[-1]["conta"])
                temp_cheque_especial = int(input("informar limite cheque especial:"))
                lista_contas.append = {"conta":temp_conta,
                                       "agencia":temp_agencia,
                                       "cpf":cpf,
                                       "saldo":0,
                                       "cheque_especial":temp_cheque_especial}
    else:
        temp_cpf = str(input("Não encontrado, informe o CPF:"))
        cadastrar_usuario(temp_cpf)
    #definir atividades
    return

def depositar(agencia,conta):
    limpa_tela()
    #definir atividades
    valor = float(input("informe o valor para saque:"))
    if valor > 0:
        print("valor")
    return

def sacar():
    limpa_tela()
    #definir atividades
    return

def imprimir():
    limpa_tela()
    #definir atividades
    return

def saindo(nome):
    limpa_tela()
    if nome is True:
        print(f"{nome}, foi um prazer ajudar você!")
    else:
        print("Obrigado por usar o banco X.")

def teste_cpf(cpf):
    for usuario in lista_usuarios:
    #habilitar validação de CPF com regras de existencia de CPF.
        if usuario["cpf"] == cpf:
            print("CPF já registrado no sistema.")
            # habilitar reescrever e apagar conta.
            return cpf
        if len(cpf) != 11:
            print("CPF Invalido.")
            return
        
def validar_conta(agencia,conta):
    for contas in lista_contas:
        if int(conta) == contas["conta"]:
            limpa_tela()
            print("conta encontrada")
            for usuario in lista_usuarios:
                if contas["cpf"] == usuario["cpf"]:
                    global usuario_ativo
                    usuario_ativo = usuario
            global conta_ativa
            conta_ativa = contas
            return True
    return False    
    
def atualiza_conta(conta_ativa):
    for conta in lista_contas:
        if conta_ativa["conta"] == conta["conta"]:
            conta.update(conta_ativa)
while True:
    opcao = input(menu)
    if opcao == "1":
        temp_cpf = str(input("informe o CPF:"))
        cadastrar_usuario(temp_cpf)
    elif opcao == "2":
        temp_cpf = input("Informe o CPF a cadastrar conta:")
        cadastrar_conta(temp_cpf,"0001")
    elif opcao == "3":
        if conta_ativa:
            depositar(conta_ativa["agencia"],conta_ativa["conta"])
        else:
            agencia = input("informe o numero da agencia com 4 digitos:")
            conta = input("informe o numero da conta:")
            validade_conta = validar_conta(agencia,conta)
            if  validar_conta == True:
                depositar(conta_ativa["agencia"],conta_ativa["conta"])
            elif validar_conta == False:
                print("Tente Novamente, conta não encontrada.")
    elif opcao == "4":
        sacar()
    elif opcao == "5":
        imprimir()
    elif opcao == "7":
        limpa_tela()
        for usuario in lista_usuarios:
            print(usuario)
        print("\n#########################\n")
        for conta in lista_contas:
            print(conta)
    elif opcao == "6":
        break