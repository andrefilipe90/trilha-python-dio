import os

def limpa_tela():
    os.system('cls || clear')

limpa_tela()

nome_correntista = False
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
[1] {cad_usuario.center(26,"#")}
[2] {cad_conta.center(26,"#")}
[3] {depositar.center(26,"#")}
[4] {sacar.center(26,"#")}
[5] {extrato.center(26,"#")}
[6] {sair.center(26,"#")}
=> """

def cadastrar_usuario():
    #definir atividades
    tmp_cpf: input("digite o numero do CPF:\n")
    return

def cadastrar_conta():
    #definir atividades
    print(lista_contas[0],lista_usuarios[0]["cpf"])
    
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

def saindo(nome):
    if nome is True:
        print(f"{nome}, foi um prazer ajudar você!")
    else:
        print("Obrigado por usar o banco X.")

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
        saindo(nome_correntista)
        break