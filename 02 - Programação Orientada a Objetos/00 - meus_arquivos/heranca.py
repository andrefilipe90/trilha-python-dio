class Veiculo:
    def __init__(self,cor,placa,nro_rodas):
        self.cor = cor
        self.placa = placa
        self.nro_rodas = nro_rodas

    def ligar_motor(self):
        print("Ligando Motor")

class Motocicleta (Veiculo):
    pass

class Carro (Veiculo):
    pass

class Caminhao (Veiculo):
    def __init__ (self,cor,placa,nro_rodas,carregado):
        self.carregado = carregado
        # aqui, ao criar linhas dentro do __init__ estou sobescrevendo o codigo principal,
        # isso influencia o caminhao, porém mantem o vaiculo, motocicleta e carro intactos.
        super().__init__(cor,placa,nro_rodas)

    def esta_carregado(self):
        print(f"{'Sim' if self.carregado else 'nao'} está carregado")

moto = Motocicleta("preta","XDS-1233",2)
moto.ligar_motor()

carro = Carro("cinza","KVT-3119",4)
carro.ligar_motor()

caminhao = Caminhao("Branco","TVK-9113",8, True)
caminhao.esta_carregado()

print(caminhao)