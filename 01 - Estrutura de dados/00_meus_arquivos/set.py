#não de pode garantir em qual ordem os itens ficarão ao se aplicar set
#os itens dentro de um set não são iteraveis como listas e toples, nem indexa nem fatia
import os
os.system('clear')

numeros = set([1,4,2,3,1,2,4,1])
print(numeros)

letras = set(["abacaxi"])
print(letras)

carros = set(("gol","celta","uno","ka","ka","ka"))
print(carros)

#para converter para listas:

numeros = {1,2,3,4,5,1,2,3,4,5}
numeros = list(numeros)
print(numeros[2])

#ainda sim é possível iterar com o for

for numero in numeros:
    print(numero)

#set são conjuntos, então dá suporte a .union
conjunto_a = {1,2,3,4,5,6}
conjunto_b = {5,6,7,8,9,0}
conjunto_c = {2,3}
print(conjunto_a.union(conjunto_b))
print(conjunto_a.intersection(conjunto_b)) #resulta a intercessão dos dois grupos
print(conjunto_a.difference(conjunto_b))
print(conjunto_b.difference(conjunto_a))
print(conjunto_a.symmetric_difference(conjunto_b)) #inverso intersection
print(conjunto_a.issuperset(conjunto_c))#retorna true se parametro for subconjunto
print(conjunto_c.issubset(conjunto_a)) #retorna true se parametro for sobreconjunto
print(conjunto_c.isdisjoint(conjunto_b)) #retorna true se se for uma disjuncao


sorteio = {1,23}
sorteio.add(25)
sorteio.add(42)
sorteio.add(23)
print(sorteio)

#suporta .clear .copy .discard .pop(tira o primeiro valor e não o ultimo como em lista)
#.remove (dá erro se item nao existir, discard não apresenta erro, só ignora) .len 
# variavel in sorteio é possivel para perguntar se um item está em um conjunto/set