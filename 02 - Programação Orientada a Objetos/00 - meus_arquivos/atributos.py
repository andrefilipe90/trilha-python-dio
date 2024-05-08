class Estudante:
    escola = "DIO"

    def __init__ (self,nome,matricula):
        self.nome = nome
        self.matricula = matricula

    def __str__(self):
        return f"{self.nome} - {self.matricula} - {self.escola}"

def mostrar_valores(*args):
    for arg in args:
        print(arg)

aluno_1 = Estudante("Guilherme", 123456)
aluno_2 = Estudante("André", 123123)

print(aluno_1,aluno_2)
print("#######\n")
aluno_1.matricula = 198765
Estudante.escola = "Python"
aluno_3 = Estudante("Sophie", 123789) # usar escola="DIO" não tem efeito pois escola está na classe
mostrar_valores(aluno_1,aluno_2,aluno_3)