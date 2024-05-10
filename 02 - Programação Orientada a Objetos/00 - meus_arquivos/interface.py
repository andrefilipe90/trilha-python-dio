# interface é o contrato, as informações do que deve ser feito
# usasse classes abstratas para tal

from abc import ABC, abstractmethod

class Controle_remoto(ABC):
    @abstractmethod
    def ligar(self):
        print("ligou")

    @abstractmethod
    def desligar(self):
        print("desligou")

class ControleTV(Controle_remoto):
    def ligar(self):
        return self

    def desligar(self):
        print("desligado")

class AppleTV(Controle_remoto):
    def ligar(self):
        print("apple")
    
    def desligar(self):
        print("Desligando. :)~")
ctrl = ControleTV()

print(ctrl.ligar())