# Lembre-se de alterar o caminho do arquivo, para o caminho completo da sua máquina!

endereco = "c:/trilha-python-dio/05 - Manipulação de arquivos/lorem.txt"
arquivo = open(endereco , 'r')
print(arquivo.read())
arquivo.close()

# arquivo = open(endereco, 'r')
# print(arquivo.readline())
# arquivo.close()

# arquivo = open(endereco, 'r')
# print(arquivo.readlines())
# arquivo.close()

# arquivo = open(endereco, 'r')
# # tip
# while len(linha := arquivo.readline()):
#     print(linha)

# arquivo.close()
