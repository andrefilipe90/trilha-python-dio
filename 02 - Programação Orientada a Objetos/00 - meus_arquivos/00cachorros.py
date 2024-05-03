class Cachorro:
    def __init__ (self, nome, cor, acordado=True):
        self.nome = nome
        self.cor = cor
        self.acordado = acordado
    
    def latir(self):
        print("au-au")
    
    def dormir(self):
        self.acordado = False
        print("ZzzzZz...")


cao_1 = Cachorro("Joe","preto",False)
cao_2 = Cachorro("Suzi","preto")

cao_1.latir()

print(cao_2.acordado)

cao_2.dormir()

print(cao_2.acordado)
