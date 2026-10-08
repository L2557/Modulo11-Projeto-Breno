from pessoa import Pessoa


class Hospede(Pessoa):

    def __init__(self, nome, idade, dias_estadia, quarto=None):
        super().__init__(nome, idade)
        self.dias_estadia = dias_estadia
        self._quarto = None

        if quarto != None:
            self.quarto = quarto

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        self._nome = valor

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, valor):
        if valor < 0:
            raise ValueError("A idade não pode ser negativa!")
        self._idade = valor

    @property
    def quarto(self):
        return self._quarto

    @quarto.setter
    def quarto(self, quarto):
        if quarto.ocupado == False:
            self._quarto = quarto
            quarto.ocupado = True
        else:
            print("ocupado")

    def atribuir_quarto(self, quarto):
        self.quarto = quarto

    def calcular_conta(self):
        return self.dias_estadia * self.quarto.preco_diaria

    def mostrar_informacoes(self):
        print(f"Nome: {self.nome}\nIdade: {self.idade}\nQuarto: {self.quarto.numero}")

    def checkout(self):
        self.quarto.ocupado = False
        print(f"Checkout realizado para {self.nome}")
        self._quarto = None
