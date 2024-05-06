class Passaro:
    def voar(self):
        print("Voando...")

class Pardal(Passaro):
    def voar(self):
        super().voar()

class Avestruz(Passaro):
    def voar(self):
        print("Avestruz não pode voar...")

class Aviao(Passaro):
    def voar(self):
        print("aviao decolando........")

def plano_voo(obj):
    obj.voar()

p1 = Pardal()
p2 = Avestruz()

plano_voo(p1)
plano_voo(p2)
print("#####")
plano_voo(Pardal())

# a mesma função vai ter capacidades diferentes dependendo da classe que ela está associada
# FIX: PENSAR EM COMO ISSO SE APLICA NA CLASSE CARRO E MOTORES
