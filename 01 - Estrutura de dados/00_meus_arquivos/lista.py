import os

def limpa_tela():
    os.system('cls || clear')

def quebra_linha():
    print('\n ====================================\n')

limpa_tela()
quebra_linha()
frutas = ["laranja","limao","morango"]
print(frutas)
quebra_linha()
for fruta in frutas:
    print(fruta)

quebra_linha()
i = -1
while i >= -3:
    print(frutas[i])
    i -= 1

quebra_linha()
letras = list("Python")
for letra in letras:
    print(letra, end='')
print(letras)

quebra_linha()
numeros = list(range(11))
print(numeros)
print(numeros[1::2])

'''quebra_linha()
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(matrix[0,0])
print(matrix[1,1])
print(matrix[2,2])
'''
quebra_linha()
carros = ["celta","gol","uno","ora","picanto","up","march","dolphin"]
for i, carro in enumerate(carros):
    print (f"{i}:{carro}")
    print (carros[i*-1])

quebra_linha()
numeros = [0,1,2,3,4,5,6,7,8,9,11,22,33,44,55,66,77,88,99,100]
pares = [numero for numero in numeros if numero % 2 == 0]
#aqui retorna numero para numero em numeros se mod de numero igual a zero
print(pares)
quadrados = [ numero * numero for numero in numeros]
print(quadrados)
#aqui retorna numero ao quadrado para cada numero em numeros

quebra_linha()
listagem = ["banana","ovos","pão"]
print(listagem)
listagem.append("queijo")
#append adiciona um item a lista, se adicionar uma lista ela se comportará como um unico item transformando a lista em uma matriz
print(listagem)
#listagem.clear() # limpa a lista
print(listagem)
print(listagem.count("banana"))
lista_geral = []
lista_geral.extend(numeros)
lista_geral.extend(pares)
lista_geral.extend(listagem)
lista_geral.extend(frutas)
lista_geral.extend(quadrados)
lista_geral.extend(letras)
lista_geral.append(carros)
#extend adiciona os itens de uma listagem passada (ou manualmente inserida) em uma lista pré existente
print(lista_geral)
print(lista_geral.index("P"))
#index encontra a primeira ocorrencia e retorna a posição daquele objeto

lista_geral.pop() #tira o ultimo item
print(lista_geral)
lista_geral.pop(0) #tira o item 0 da lista
print(lista_geral)
lista_geral.remove(100) #remove o item com conteudo 100
print(lista_geral)
#lista_espelho = copy.lista_geral #verificar como usar copy
#lista_espelho.reverse #espelha a lista
print(lista_geral)
#print(lista_espelho)

quebra_linha()
print(f"lista original:          {carros}")
carros.sort(reverse=True) #classifica a lista e ordena reverso
print(f"lista .sort com reverse: {carros}")
carros.sort(key=lambda x: len(x), reverse=True) #aqui faz o sort com base no comprimento da string pois usa len() menor para o maior
print(f"lista .sort len+reverse: {carros}")
print(f"lista sorted +len:       {sorted(carros, key=lambda x: len(x))}")
print(f"lista sorted +len+rev:   {sorted(carros, key=lambda x: len(x), reverse=True)}")

# o sort faz diferenciação por tamanho, ao encontrar string com tamanhos iguais dependendo dos critérios pode ser que
#a listagem len(x) reverse=True não fique o espelho da reverse=True, pois depende em qual string de maior tamanho ele
#passar primeiro em cada um dos casos que houver mais de uma string do tamanho final.
