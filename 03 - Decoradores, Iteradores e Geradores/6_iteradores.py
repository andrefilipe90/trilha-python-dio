class MeuIterador:
    def __init__(self, numeros: list[int]):
        self.numeros = numeros
        self.contador = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            numero = self.numeros[self.contador]
            self.contador += 1
            print(f"{numero}: {self.contador}")
            return numero * 2
            
        except IndexError:
            raise StopIteration


for i in MeuIterador(numeros=[1000, 38, 13, 11,300]):
    print(i)
