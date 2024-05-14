class Animal:
    def __init__(self,nro_patas,tem_rabo):
        self.nro_patas = nro_patas
        self.tem_rabo = tem_rabo
    
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


class Mamifero(Animal):
    def __init__(self,cor_pelos, **kw):
        super().__init__(**kw)
        self.cor_pelos = cor_pelos

        # ainda nao entendi o porque tenho que declarar algo que já está inserido na __init__ pai
        # se a classe já está associada, os atribulos nao deveriam ser herdados? ou será que para
        # herdar eu tenho de informar o que foi herdado? nesse caso qual a utilidade dessas relaçoes

class Ave(Animal):
    def __init__(self,cor_bico,**kw):
        super().__init__(**kw)
        self.cor_bico = cor_bico

class Cachorro(Mamifero):
    pass

class Gato(Mamifero):
    def __init__(self,**kw):
       super().__init__(**kw)
       # print(Gato.__mro__) demonstra a sequencia de validacao de metodos do python
       # sempre procurando resolver algo de dentro pra fora, na classe que a instancia
       # foi criada, depois na sequencia de superiores até a classe objeto, por isso
       # uma variavel global que é usada dentro de um escopo de looping deve ser copiada
       # para dentro do escopo local como boa pratica e ganho de velocidade de execuçao

class Leao(Mamifero):
    def __init__(self,**kw):
        super().__init__(**kw)

class Ornitorinco(Mamifero, Ave):
    pass

gato = Gato(nro_patas=4,cor_pelos="amarelo",tem_rabo=True)
print(f"{gato} \n")
ornitorrinco = Ornitorinco(nro_patas=2,cor_pelos="vermelho", cor_bico="laranja",tem_rabo=False)
print(f"{ornitorrinco} \n")
leao = Leao(nro_patas=4,cor_pelos="amarelo",tem_rabo=True)
print(leao)