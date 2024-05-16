import os


def limpa_tela():
    os.system('cls || clear')


limpa_tela()

global conta_ativa
global usuario_ativo
conta_ativa = {}
usuario_ativo = {}
lista_usuarios = [{"cpf": "05843914712",
                   "nome": "André Filipe Guering de Mattos",
                   "nascimento": "14/05/1990",
                   "endereço": "Rua Roberto Fritzgerald Kennedy,40 - Cavaleiros - Macaé/RJ"}]
lista_contas = [{"conta": 1,
                 "agencia": "0001",
                 "cpf": "05843914712",
                 "saldo": 100,
                 "cheque_especial": 100,
                 "n_saques": 0,
                 "extrato": ""
                 }] #definir tipo
cad_usuario = " Cadastro Usuario "
cad_conta = " Cadastro Conta "
depositar = " Depositar "
sacar = " Sacar "
extrato = " Extrato "
sair = " Sair "

menu = f"""
##############################

[1] {cad_usuario.center(26, "#")}
[2] {cad_conta.center(26, "#")}
[3] {depositar.center(26, "#")}
[4] {sacar.center(26, "#")}
[5] {extrato.center(26, "#")}
[6] {sair.center(26, "#")}

=> """

def cadastrar_usuario(cpf):
    # print("passou cadastrar_usuario")
    limpa_tela()
    temp_cpf = teste_cpf(cpf)
    if temp_cpf == cpf:
        return
    temp_nome = input("Informe o nome:")
    temp_nascimento = input("informe a data de nascimento dd/mm/aaaa:")
    temp_endereco = input("informe o endereço: rua, nº - bairro - cidade/ES:")
    temp_dict = {"cpf": cpf, "nome": temp_nome,
                 "nascimento": temp_nascimento,
                 "endereço": temp_endereco}
    lista_usuarios.append(temp_dict)
    criar_conta = input("gostaria de criar uma conta? [s]sim ou [n]não:")
    if criar_conta == "s":
        # print(temp_dict)
        # print(cpf)
        # print(temp_cpf)
        cadastrar_conta(agencia="0001",cpf=cpf)
        return
    elif criar_conta == "n":
        return
    else:
        print("opção não encontrada, retornando ao menu:")
    return

def cadastrar_conta(cpf,agencia):
    # print("passou cadastrar_conta")
    #limpa_tela()
    temp_agencia = agencia
    # print(cpf)
    cpf_valido = teste_cpf(cpf)
    if cpf_valido == cpf:
        for usuario in lista_usuarios:
            if usuario["cpf"] == cpf:
                temp_conta= 1+ int(lista_contas[-1]["conta"])
                temp_cheque_especial = int(input("informar limite cheque especial:"))
                lista_contas.append({"conta":temp_conta,
                                       "agencia":temp_agencia,
                                       "cpf":cpf,
                                       "saldo":0,
                                       "cheque_especial":temp_cheque_especial,
                                       "n_saques":0,
                                       "extrato":""
                                       })
    else:
        temp_cpf = str(input("Não encontrado, informe o CPF:"))
        cadastrar_usuario(temp_cpf)
    return

def depositar(valor):
    limpa_tela()
    #definir atividades
    # print(conta_ativa)
    if valor > 0:
        conta_ativa["saldo"] += valor
        print(conta_ativa["saldo"])
        conta_ativa["extrato"] += f"Deposito de R$ {valor}\n"
        print(conta_ativa["extrato"])
        atualiza_conta()
    return

def sacar(valor):
    limpa_tela()
    #definir atividades
    # print(conta_ativa)
    if valor > 0:
        conta_ativa["saldo"] -= valor
        print(conta_ativa["saldo"])
        conta_ativa["extrato"] += f"Saque de R$ {valor}\n"
        print(conta_ativa["extrato"])
        atualiza_conta()
    return

def imprimir(saldo,extrato):
    limpa_tela()
    #definir atividades
    print(extrato)
    print("\n########################\n")
    print(f"Saldo atual é R$ {saldo}")
    return

def saindo(nome):
    limpa_tela()
    if nome is True:
        print(f"{nome}, foi um prazer ajudar você!")
    else:
        print("Obrigado por usar o banco X.")

def teste_cpf(cpf):
    # print("passou por teste_cpf")
    # print(cpf)
    for usuario in lista_usuarios:
    #habilitar validação de CPF com regras de existencia de CPF.
        if usuario["cpf"] == cpf:
            print("CPF já registrado no sistema.")
            # habilitar reescrever e apagar conta.
            return cpf
        if len(cpf) != 11:
            print("CPF Invalido.")
            return
        
def validar_conta(conta):
    # print("passou validar_conta")
    for contas in lista_contas:
        if int(conta) == contas["conta"]:
            #limpa_tela()
            print("conta encontrada")
            for usuario in lista_usuarios:
                if contas["cpf"] == usuario["cpf"]:
                    global usuario_ativo
                    usuario_ativo = usuario
            global conta_ativa
            conta_ativa = contas
            # print(conta_ativa)
            return True
    return False    
    
def atualiza_conta():
    # print("passou atualiza_conta")
    for conta in lista_contas:
        if conta_ativa["conta"] == conta["conta"]:
            conta.update(conta_ativa)

while True:
    opcao = input(menu)
    if opcao == "1":
        temp_cpf = str(input("informe o CPF:"))
        cadastrar_usuario(cpf=temp_cpf)
    elif opcao == "2":
        temp_cpf = input("Informe o CPF a cadastrar conta:")
        cadastrar_conta(temp_cpf,"0001")
    elif opcao == "3":
        if conta_ativa:
            temp_valor = float(input("informe o valor para deposito:"))
            depositar(valor=temp_valor)
        else:
            agencia = input("informe o numero da agencia com 4 digitos:")
            conta = input("informe o numero da conta:")
            validade_conta = validar_conta(conta)
            #print(f"chegou aqui: {validade_conta}")
            if  validade_conta == True:
                # print("if validar_conta == True")
                temp_valor = float(input("informe o valor para deposito:"))
                depositar(temp_valor)
            elif validade_conta == False:
                # print("if validar_conta == False")
                print("Tente Novamente, conta não encontrada.")
    elif opcao == "4":
        if conta_ativa:
            temp_valor = float(input("informe o valor para saque:"))
            sacar(valor=temp_valor)
        else:
            agencia = input("informe o numero da agencia com 4 digitos:")
            conta = input("informe o numero da conta:")
            validade_conta = validar_conta(conta)
            # print(f"chegou aqui: {validade_conta}")
            if  validade_conta == True:
                # print("if validar_conta == True")
                temp_valor = float(input("informe o valor para saque:"))
                sacar(valor=temp_valor)
            elif validade_conta == False:
                # print("if validar_conta == False")
                print("Tente Novamente, conta não encontrada.")
    elif opcao == "5":
        if conta_ativa:
            imprimir(conta_ativa["saldo"],extrato=conta_ativa["extrato"])
        else:
            agencia = input("informe o numero da agencia com 4 digitos:")
            conta = input("informe o numero da conta:")
            validade_conta = validar_conta(conta)
            # print(f"chegou aqui: {validade_conta}")
            if  validade_conta == True:
                # print("if validar_conta == True")
                imprimir(conta_ativa["saldo"],extrato=conta_ativa["extrato"])
            elif validade_conta == False:
                # print("if validar_conta == False")
                print("Tente Novamente, conta não encontrada.")
    elif opcao == "7":
        limpa_tela()
        for usuario in lista_usuarios:
            print(usuario)
        print("\n#########################\n")
        for conta in lista_contas:
            print(conta)
    elif opcao == "6":
        break