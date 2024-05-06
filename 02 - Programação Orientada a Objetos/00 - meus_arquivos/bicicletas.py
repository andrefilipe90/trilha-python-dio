class Bicicleta:
    def __init__ (self,cor,modelo,ano,valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("Gui Gui Gui Gui Gui!")

    def parar(self):
        print("freiannnndoo!!!")

    def correr(self):
        print("Ran-dan-dan-tá-tá")

    def __str__(self):
        return f"{self.__class__.__name__}: {' , '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


bike_1 = Bicicleta("vermelho","Caloi",2024,15000)

Bicicleta.buzinar(bike_1)
print(bike_1.cor)

bike_2 = Bicicleta("preta","caloi",2024,7000)

bike_2.buzinar()

print(bike_2)
#sao maneiras diferentes de expressar o mesmo método