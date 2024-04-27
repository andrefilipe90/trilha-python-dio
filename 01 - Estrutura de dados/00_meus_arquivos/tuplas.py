#tuplas são estruturas imutáveis, como constantes
lista_compras = ("banana","maça","pera","uva","pão","manteiga",)
print(lista_compras)
letras_python = tuple("Python")
print(letras_python)
numeros = tuple([1,2,3,4])
print(numeros)
print(numeros[2])
pais = ("Brasil",)
print(pais)
#pais.append("Argentina") #não funciona em tuple
#tem suporte a maior partes dos metodos de leitura e fatiamento, mas não temos opções de edição
# suporta count, index, len, mas não suporta append ou extend