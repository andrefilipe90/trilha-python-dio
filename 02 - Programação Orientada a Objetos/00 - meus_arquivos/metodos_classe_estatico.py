# metodo de classe - cls
# metodos de fabrica retornam instancias (como se fosse variaveis)
# metodos estatico (para funções que por exemplo validam informações)

class Pessoa:
    def __init__(self,nome=None,idade=None):
        self.nome = nome
        self.idade = idade
    
    @classmethod
    def cria_com_idade(cls,ano,nome): #cls aponta para a classe, sem criar uma instancia inutil
        idade = 2024 - ano
        return cls(nome,idade)
    
    @staticmethod
    def maior_idade(idade):
        return idade >= 18

pessoa1 = Pessoa("andre", 33)

print(pessoa1.nome,pessoa1.idade)

pessoa2 =Pessoa.cria_com_idade(nome="Filipe", ano=1990)
print(pessoa2.nome, pessoa2.idade)

print(Pessoa.maior_idade(16))
print(Pessoa.maior_idade(28))
