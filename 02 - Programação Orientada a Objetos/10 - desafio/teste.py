def repetir(num_vezes):
    def decorador_real(func):
        def envoltorio(*args, **kwargs):
            for _ in range(num_vezes):
                resultado = func(*args, **kwargs)
            return resultado
        return envoltorio
    return decorador_real

@repetir(num_vezes=3)
def saudar(nome):
    print(f"Olá {nome}")

saudar("Alice")
