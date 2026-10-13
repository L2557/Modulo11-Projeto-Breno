from funcionario import Recepcionista, TecnicoManutencao

class TecnicoRecepcao(Recepcionista, TecnicoManutencao):
    def __init__(self, nome, id_fun, salario, setor, especialidade):
        Recepcionista().__init__(nome, id_fun, salario)
        TecnicoManutencao().__init__(especialidade)
        self.setor = setor

    def registrar_hospede(self, nome_hospede):
        print("Hóspede registrado:", nome_hospede)

    def registrar_reparo(self, descricao):
        print("Reparo registrado:", descricao)

    def mostrar_informacoes(self):
            print(f"Técnico de Receção: {self.nome}\nID: {self.id_fun}\nSalário: {self.salario}\nSetor: {self.setor}\nEspecialidade: {self.especialidade}")
