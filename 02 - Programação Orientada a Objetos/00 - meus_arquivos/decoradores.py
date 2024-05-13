def diga_nome(func):

    def mensagem1(nome):
        print(f"bom dia, {nome}")

    def mensagem2(nome):
        print(f"boa tarde, {nome}")

    if func == "mensagem1":
        return mensagem1
    elif func == "mensagem2":
        return mensagem2


diga_nome('mensagem2')("André")