from abc import ABC, abstractmethod

class Quarto(ABC):

    def __init__(self, numero, tipo, preco_diaria):
        self.numero = numero
        self.tipo = tipo
        self.preco_diaria = preco_diaria
        self._ocupado = False

    @property
    @abstractmethod
    def ocupado(self):
        pass

    @ocupado.setter
    @abstractmethod
    def ocupado(self, valor):
        pass

    @property
    @abstractmethod
    def preco_diaria(self):
        pass

    @preco_diaria.setter
    @abstractmethod
    def preco_diaria(self, valor):
        pass

    @abstractmethod
    def mostrar_informacoes(self):
        pass

class QuartoSimples(Quarto):

    def __init__(self, numero, preco_diaria):
        super().__init__(numero, "Simples", preco_diaria)

    @property
    def ocupado(self):
        return self._ocupado

    @ocupado.setter
    def ocupado(self, valor):
        self._ocupado = valor

    @property
    def preco_diaria(self):
        return self._preco_diaria

    @preco_diaria.setter
    def preco_diaria(self, valor):
        if valor < 0:
            raise ValueError("Preço não pode ser negativo!")
        self._preco_diaria = valor

    def mostrar_informacoes(self):
        print(f"Quarto: {self.numero}\nTipo: {self.tipo}\nPreço: {self.preco_diaria}\nOcupado: {self.ocupado}")


class QuartoLuxo(Quarto):

    def __init__(self, numero, preco_diaria):
        super().__init__(numero, "Luxo", preco_diaria)

    @property
    def ocupado(self):
        return self._ocupado

    @ocupado.setter
    def ocupado(self, valor):
        self._ocupado = valor

    @property
    def preco_diaria(self):
        return self._preco_diaria

    @preco_diaria.setter
    def preco_diaria(self, valor):
        if valor < 0:
            raise ValueError("Preço não pode ser negativo!")
        self._preco_diaria = valor
        

    def mostrar_informacoes(self):
        print(f"Quarto: {self.numero}\nTipo: {self.tipo}\nPreço: {self.preco_diaria}\nOcupado: {self.ocupado}")
