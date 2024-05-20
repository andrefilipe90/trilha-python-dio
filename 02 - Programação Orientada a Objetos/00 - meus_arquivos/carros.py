class Veiculo:
    def __init__(self,n_roda,cor,n_porta,tem_ar,tem_abs):
        self.n_roda = n_roda
        self.cor = cor
        self.n_porta = n_porta
        self.tem_ar = tem_ar
        self.tem_abs = tem_abs
    
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


class Motor_eletrico:
    def __init__(self):
        pass

class Motor_combustao:
    def __init__(self):
        pass

class Caminhao:
    def __init__(self):
        pass

class Carro(Veiculo):
    def __init__(self,**kw):
        super().__init__(**kw)

class Moto:
    def __init__(self):
        pass

gol = Veiculo(n_roda=4,cor="branco",n_porta=2,tem_ar=True,tem_abs=False)
print(f"{gol} \n")

# motor_1 = Motor_eletrico()