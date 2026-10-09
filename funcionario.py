from pessoa import Pessoa

class Funcionario(Pessoa):
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)
        self.salario = salario

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

    def mostrar_informacoes(self):
        print(f"Funcionário: {self.nome}")

class Gerente(Funcionario):
    def __init__(self, nome, idade, salario, bonus):
        super().__init__(nome, idade, salario)
        self.bonus = bonus

    def mostrar_informacoes(self):
        print(f"Gerente: {self.nome} \nIdade: {self.idade} \nSalário + Bônus: {self.salario + self.bonus}")

    def gerar_relatorio(self, funcionarios):
        for funcionario in funcionarios:
            funcionario.mostrar_informacoes()

class Recepcionista(Funcionario):
    def __init__(self, nome, id_func, idade, salario, turno):
        super().__init__(nome, idade, salario)
        self.id_func = id_func
        self.turno = turno

    @property
    def turno(self):
        return self.turno

    @turno.setter
    def turno(self, turno):
        if turno in ["manhã", "tarde", "noite"]:
            self._turno = turno
        else:
            print("Turno inválido!")

    def mostrar_informacoes(self):
        print(f"Recepcionista: {self.nome}")

    def registrar_hospede(self, hospede, lista_hospedes):
        lista_hospedes.append(hospede)

    def listar_hospedes(self, lista_hospedes):
        for hospede in lista_hospedes:
            hospede.mostrar_informacoes()


class TecnicoManutencao(Funcionario):
    def __init__(self, nome, idade, salario, especialidade):
        super().__init__(nome, idade, salario)
        self.especialidade = especialidade

    @property
    def especialidade(self):
        return self._especialidade

    @especialidade.setter
    def especialidade(self, especialidade):
        self._especialidade = especialidade

    def mostrar_informacoes(self):
        print(f"Técnico: {self.nome}")

    def registrar_reparo(self, descricao):
        print(f"Reparo registrado: {descricao}")