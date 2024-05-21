# Classe UsuarioTelefone e o encapsulamento dos atributos nome, numero e plano:
class UsuarioTelefone:
    def __init__(self, nome, numero, plano):
        self._nome = nome
        self._numero = numero
        self._plano = plano
        print(f"UsuarioTelefone inicializado: {self._nome}, {self._numero}, plano saldo: {self._plano.verificar_saldo()}")


# TODO: Crie um método fazer_chamada para permitir que um usuário faça uma chamada telefônica:
    def fazer_chamada(self, destinatario,duracao):
# TODO: Calcule o custo da chamada usando o método 'custo_chamada' do objeto 'plano':
        custo = self._plano.custo_chamada(duracao)
        print(f"Custo da chamada: {custo}")
# TODO: Verifique se o saldo do plano é suficiente para a chamada.
        if self._plano.verificar_saldo() >= custo:
# TODO: Se o saldo for suficiente, deduz o custo da chamada do saldo do plano.
            self._plano.deduzir_saldo(custo)
# TODO: E retorne uma mensagem de sucesso com o destinatário e o saldo restante após a chamada:
            return (f"Chamada para {destinatario}")

# Classe Pano, ela representa o plano de um usuário de telefone:
# TODO: Crie um método para verificar_saldo e retorne o saldo atual:
# TODO: Crie um método custo_chamada para calcular o custo de uma chamada supondo o custo de $0.10 por minuto:
# TODO: Crie um método deduzir_saldo para deduz o valor do saldo do plano:
class Plano:
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial
        print(f"Plano inicializado com saldo: {self.saldo}")

    def verificar_saldo(self):
        return self.saldo
    
    def custo_chamada(self, duracao):
        return duracao*0.1
    
    def deduzir_saldo(self, a_deduzir):
        self.saldo -= a_deduzir


# Classe UsuarioPrePago, aqui vemos a herança onde UsuarioPrePago herda os atributos e métodos da classe UsuarioTelefone:
class UsuarioPrePago(UsuarioTelefone):
    def __init__(self, nome, numero, saldo_inicial):
        super().__init__(nome, numero, Plano(saldo_inicial))


# Recebendo as informações do usuário:
nome = input()
numero = input()
saldo_inicial = float(input())

# Objeto de UsuarioPrePago com os dados fornecidos:
usuario_pre_pago = UsuarioPrePago(nome, numero, saldo_inicial)
destinatario = input()
duracao = int(input())

# Chama o método fazer_chamada do objeto usuario_pre_pago e imprime o resultado:
print(usuario_pre_pago.fazer_chamada(destinatario, duracao))
