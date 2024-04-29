import os

def limpa_tela():
    os.system('cls || clear')

limpa_tela()

lista_usuarios = []
lista_contas = [] #definir tipo

cad_usuario = " Cadastro Usuario "
cad_conta = " Cadastro Conta "
depositar = " Depositar "
sacar = " Sacar "
extrato = " Extrato "
sair = " Sair "

menu = f"""
[1] {cad_usuario.center(26,"#")}
[2] {cad_conta.center(26,"#")}
[3] {depositar.center(26,"#")}
[4] {sacar.center(26,"#")}
[5] {extrato.center(26,"#")}
[6] {sair.center(26,"#")}
=> """

while True:
    opcao = input(menu)
    if opcao == "1":
        cadastrar_usuario()
    elif opcao == "2":
        cadastrar_conta()
    elif opcao == "3":
        depositar()
    elif opcao == "4":
        sacar()
    elif opcao == "5":
        imprimir()
    elif opcao == "6":
        print(f"{nome_correntista}, obrigado por estar conosco.")
        break

def cadastrar_usuario():
    #definir atividades
    tmp_cpf: input("digite o numero do CPF:\n")
    return

def cadastrar_conta():
    #definir atividades
    return

def sacar():
    #definir atividades
    return

def depositar():
    #definir atividades
    return

def imprimir():
    #definir atividades
    return

