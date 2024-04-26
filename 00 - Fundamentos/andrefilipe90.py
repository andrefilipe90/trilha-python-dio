import os

# Dio.me - Codigo Primeiro Desafio - andrefilipe90

def limpar_tela():
    os.system('cls')

# Chamada da função para limpar a tela
limpar_tela()

depositar = " Depositar "
sacar = " Sacar "
extrato = " Extrato "
sair = " Sair "

menu = f"""
[1] {depositar.center(18,"#")}
[2] {sacar.center(18,"#")}
[3] {extrato.center(18,"#")}
[4] {sair.center(18,"#")}

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        #recebe valor para deposito
        valor = float(input("Informe o valor do depósito: "))
        #valida valor positivo
        if valor > 0:
            #agrega saldo, agrega listagem extrato, resultado em tela
            limpar_tela()
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"valor R$ {valor:.2f} depositado com sucesso.")
        #implementar condicao para tratar caracteres nao numericos
        #resultado erro em tela para valores negativos
        else:
            limpar_tela()
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES
        print(valor,excedeu_saldo,excedeu_limite,excedeu_saques)
        if excedeu_saldo:
            limpar_tela()
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            limpar_tela()
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            limpar_tela()
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            limpar_tela()
            extrato += f"Saque: R$ {valor:.2f}\n"
            print(f"valor R$ {valor:.2f} sacado com sucesso.")
            numero_saques += 1

        else:
            limpar_tela()
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "3":
        limpar_tela()
        print(f"{extrato}")
        #print(f"""
        #      \n{extrato.center(18,"#")}
        #      """)
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "4":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
