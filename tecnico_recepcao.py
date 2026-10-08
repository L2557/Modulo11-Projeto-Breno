from funcionario import Recepcionista, TecnicoManutencao

class TecnicoRecepcao(Recepcionista, TecnicoManutencao):
    def __init__(self,nome, id_fun, salario, setor, especialidade):
        self.nome = nome
        self.id_fun = id_fun
        self.salario = salario
        self.setor = setor
        self.especialidade = especialidade

    def registrar_hospede(self, nome_hospede):
        print("Hóspede registrado:", nome_hospede)

    def registrar_reparo(self, descricao):
        print("Reparo registrado:", descricao)

    def mostrar_informacoes(self):
            print(f"\nTécnico de Receção: {self.nome}\nIdade: {self.idade}\nID: {self.id_fun}\nSalário: {self.salario}\nSetor: {self.setor}\nEspecialidade: {self.especialidade}")