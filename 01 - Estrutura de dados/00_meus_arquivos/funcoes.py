import os

os.system('cls')

def exibir_mensagem():
    print("olá mundo!")

def exibir_mensagem_2(nome):
    print(f"seja bem vindo {nome}.")

def exibir_mensagem_3(nome="Anonimo"):
    print(f"seja bem vindo {nome}.")

def exibit_mensagem_4(genero,nome):
    #print(type(genero),genero)
    if genero == 0:
        print(f"Bem vindo {nome}, aqui está um poema para voce:\n\n")
    elif genero == 1:
        print(f"Bem vinda {nome}, aqui está um poema para voce:\n\n")
    else:
        print(f"Saudações {nome}, aqui está um poema para voce:\n\n")
    genero_msg = genero
    inicial = nome[0]
    return genero_msg, inicial

exibir_mensagem()
exibir_mensagem_2("Guilherme")
exibir_mensagem_3()
exibir_mensagem_3(nome="André")

genero = int(input('''
Informe o genero:
[1] - Feminino
[0] - Masculino
'''))
nome = input("Informe o nome:")
exibit_mensagem_4(genero, nome)
#print (genero_msg, inicial)

# *args = tupla
# **kwargs = dict

def exibir_poema(data,*args,**kwargs):
    cabecalho = "\n".join(args)
    texto = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
    printar = f"{data}\n\n{cabecalho}\n\n{texto}"
    print(printar)

exibir_poema("20240429",
"rosas são vermelhas",
"violetas são azuis",
"brocoles são verdes",
"e eu gosto de aucassus",
por="André Mattos",
cidade="Macaé"
)

# para argumentos em funções, se houver barra tudo depois dela a 
#chave é opcional, antes da barra tudo é obrigatório sem, depois do
#asterisco tudo é obrigatório com chave ex:)

# funcao (sem_chave,/,chave_opcional,#,chave_obrigatoria)

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

#def teste(a, b):

def exibir (a, b, funcao):
    resultado = funcao(a,b)
    print(f"O resultado da operacao é: {resultado}")

exibir(2,2, multiplicar)

pagamento_abril = 2000
bonus = [500]

def variavel_funcao(salario,bonus):
    global pagamento_abril
    print(salario)
    salario += bonus[0]
    diferenca_bonus = bonus[0] + bonus[0] * 0.2
    novo_bonus = bonus.copy() #para escopo local (preferivel)
    novo_bonus.append(diferenca_bonus)
    bonus.append(diferenca_bonus) #para escopo global (evitar)
    
    print(bonus, salario)
    return print(salario)


variavel_funcao(pagamento_abril,bonus)