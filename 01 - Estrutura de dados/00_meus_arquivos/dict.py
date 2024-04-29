#dicionarios é um conjunto de pares chave(imutável):valor
import os
os.system('clear')
''''
pessoa = {"nome":"Guilherme","idade":28}
pessoa = dict(nome="André",idade=33)
pessoa["telefone"] = "3333-1231"
print(pessoa)
'''
#dicionario_aninhado
contatos = {
    "guilherme@gmail.com": {"nome":"guilherme","telefone":"1234-5678"},
    "giovanna@gmail.com": {"nome":"giovanna","telefone":"9876-5432"},
    "vinicius@gmail.com": {"nome":"vinicius","telefone":"1357-9753"},
    "melanie@gmail.com": {"nome":"melanie","telefone": {"celular": "999623322"}},
}

#print(contatos["guilherme@gmail.com"]["telefone"])

print("for contato in contatos")
for contato in contatos:
    print(contato, contatos[contato])
    if contatos[contato] is dict:
        print("dicionario encontrado.")

print("\n####################\n")

print("for chave,contato in contatos.items")
for chave, contato in contatos.items():
    print(chave, contato)

print("\n####################\n")

backup_contatos = dict()
backup_contatos = contatos.copy()

print("for chave, b_contato in backup_contatos.items")
for chave, b_contato in backup_contatos.items():
    print(chave, b_contato)

#backup_contatos.clear()
print("\n####################\n")

print("contatos.get melanie@gmail.com")
print(contatos.get("melanie@3gmail.com"))
print("contatos = contatos.fromkeys")
contatos = contatos.fromkeys({"apelido","endereco"},"vazio")
print("print contato.keys")
print(contatos.keys())
print("contatos.pop apelido")
contatos.pop("apelido", print("valor nao encontrato")) #elimina a chave, se não encontrar retorna o segundo parametro
print("contatos.setdefault sono")
contatos.setdefault("sono", "muito") #verifica se a chave existe, se não existir adiciona

print("\n####################\n")

contatos.update({"endereco": {"rua": "R F Kennedy", "numero": 40, "bairro": "Cavaleiros"}}) #adiciona ou edita o conteudo de uma chave
print("for chave, contato in contatos.items")
for chave, contato in contatos.items():
    print(chave, contato)

print("\n####################\n")

print("for chave, b_contato in backup_contatos.items")
for chave, b_contato in backup_contatos.items():
    print(chave, b_contato)

print(["endereco"]["rua"] in "contatos")