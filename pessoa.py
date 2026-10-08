from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @property
    @abstractmethod
    def nome(self):
        pass
    
    @nome.setter
    @abstractmethod
    def nome(self, valor):
        pass

    @property
    @abstractmethod
    def idade(self):
        pass

    @idade.setter
    @abstractmethod
    def idade(self, valor):
        pass

    @abstractmethod
    def mostrar_informacoes(self):
        pass