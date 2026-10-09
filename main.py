from hospede import Hospede
from funcionario import Gerente, Recepcionista, TecnicoManutencao
from tecnico_recepcao import TecnicoRecepcao
from quarto import QuartoSimples, QuartoLuxo


quartos = []
hospedes = []
funcionarios = []


def criar_quarto():
    print("\nCRIAR QUARTO")

    numero = int(input("Número do quarto: "))
    for quarto in quartos:
        if quarto.numero == numero:
            print("Já existe um quarto com esse número")
            return

    print("1 - Simples\n2 - Luxo")
    tipo = int(input("Escolha o tipo: "))
    preco = float(input("Preço por dia: "))
    if preco < 0:
        print("Preço não pode ser negativo")
        return

    if tipo == 1:
        quarto = QuartoSimples(numero, preco)
    elif tipo == 2:
        quarto = QuartoLuxo(numero, preco)

    else:
        print("Tipo inválido")
        return

    quartos.append(quarto)
    print("Quarto criado")


def listar_quartos():
    print("\nQUARTOS:")

    if len(quartos) == 0:
        print("Não existem quartos registados")
        return

    for quarto in quartos:
        quarto.mostrar_informacoes()
        print("-" * 25)


def criar_hospede():
    print("\nREGISTAR HÓSPEDE")

    nome = input("Nome: ")

    idade = input("Idade: ")
    if idade.isdigit() == False:
        print("Idade inválida")
        return
    idade = int(idade)
    if idade <= 0:
        print("Idade inválida")
        return
    
    dias_estadia = input("Dias de estadia: ")
    if dias_estadia.isdigit() == False:
        print("Dias de estadia inválidos")
        return
    dias_estadia = int(dias_estadia)
    if dias_estadia <= 0:
        print("Dias de estadia inválidos")
        return

    if len(quartos) == 0:
        print("Não existem quartos")
        return

    print("\nQuartos:")
    for quarto in quartos:
        quarto.mostrar_informacoes()
        print("-" * 25)

    numero = input("Número do quarto: ")
    if numero.isdigit() == False:
        print("Número do quarto inválido")
        return
    numero = int(numero)
    if len(quartos) == 0:
        print("Não existem quartos")
        return

    quarto_escolhido = None

    for quarto in quartos:
        if quarto.numero == numero:
            quarto_escolhido = quarto
            break

    if quarto_escolhido == None:
        print("Quarto não encontrado")
        return

    if quarto_escolhido.ocupado:
        print("O quarto está ocupado")
        return

    hospede = Hospede(nome, idade, dias_estadia, quarto_escolhido)
    hospedes.append(hospede)


def listar_hospedes():
    print("\nHÓSPEDES")

    if len(hospedes) == 0:
        print("Não existem hóspedes registados")
        return

    for hospede in hospedes:
        hospede.mostrar_informacoes()
        print("Conta:", hospede.calcular_conta(), "€")
        print("-" * 25)


def fazer_checkout():
    print("\nCHECKOUT ")

    nome = input("Nome do hóspede: ")

    hospede_encontrado = None

    for hospede in hospedes:
        if hospede.nome == nome:
            hospede_encontrado = hospede
            break

    if hospede_encontrado is None:
        print("Hóspede não encontrado")
        return

    print("Valor da conta:", hospede_encontrado.calcular_conta(), "€")
    hospede_encontrado.checkout()

    hospedes.remove(hospede_encontrado)
    print(f"Quarto Limpo")


def criar_funcionario():
    print("\nCRIAR FUNCIONÁRIO")
    print("1 - Gerente\n2 - Recepcionista\n3 - Técnico de Manutenção\n4 - Técnico de Recepção")

    opcao = int(input("Escolha: "))

    if opcao == 1:
        nome = input("Nome: ")

        idade = input("Idade: ")
        if idade.isdigit() == False:
            print("Idade inválida")
            return
        idade = int(idade)
        if idade <= 0:
            print("Idade inválida")
            return
        
        salario = input("Salário: ")
        if salario.isdigit() == False:
            print("Salário inválida")
            return
        salario = float(salario)
        if salario <= 0:
            print("Salário inválido")
            return

        bonus = input("Bônus: ")
        if bonus.isdigit() == False:
            print("Bônus inválido")
            return
        bonus = float(bonus)
        if bonus <= 0:
            print("Bônus inválido")
            return

        funcionario = Gerente(nome,idade,salario, bonus)

    elif opcao == 2:
        nome = input("Nome: ")

        id_func = input("ID do funcionário: ")
        if id_func.isdigit() == False:
            print("ID inválido")
            return
        id_func = int(id_func)
        if id_func <= 0:
            print("ID inválido")
            return
        
        for funcionario in funcionarios:
            if isinstance(funcionario, Recepcionista) or isinstance(funcionario, TecnicoRecepcao):
                if funcionario.id_func == id_func:
                    print("Já existe um funcionário com esse ID!")
                    return

        idade = input("Idade: ")
        if idade.isdigit() == False:
            print("Idade inválida")
            return
        idade = int(idade)
        if idade <= 0:
            print("Idade inválida")
            return
        
        salario = input("Salário: ")
        if salario.isdigit() == False:
            print("Salário inválido")
            return
        salario = float(salario)
        if salario <= 0:
            print("Salário inválido")
            return
        turno = input("Turno (manhã/tarde/noite): ")

        funcionario = Recepcionista(nome, id_func, idade, salario, turno)

    elif opcao == 3:
        nome = input("Nome: ")
        
        idade = input("Idade: ")
        if idade.isdigit() == False:
            print("Idade inválida")
            return
        idade = int(idade)
        if idade <= 0:
            print("Idade inválida")
            return
        
        salario = input("Salário: ")
        if salario.isdigit() == False:
            print("Salário inválido")
            return
        salario = float(salario)
        if salario <= 0:
            print("Salário inválido")
            return
        especialidade = input("Especialidade: ")

        funcionario = TecnicoManutencao(nome, idade, salario, especialidade)

    elif opcao == 4:
        nome = input("Nome: ")

        id_func = input("ID do funcionário: ")
        if id_func.isdigit() == False:
            print("ID inválido")
            return
        id_func = int(id_func)
        if id_func <= 0:
            print("ID inválido")
            return
        
        for funcionario in funcionarios:
            if isinstance(funcionario, Recepcionista) or isinstance(funcionario, TecnicoRecepcao):
                if funcionario.id_func == id_func:
                    print("Já existe um funcionário com esse ID!")
                    return
        
        salario = input("Salário: ")
        if salario.isdigit() == False:
            print("Salário inválido")
            return
        salario = float(salario)
        if salario <= 0:
            print("Salário inválido")
            return
        setor = input("Setor: ")
        especialidade = input("Especialidade: ")

        funcionario = TecnicoRecepcao(nome, id_func, salario, setor, especialidade)

    else:
        print("Opção inválida!")
        return

    funcionarios.append(funcionario)


def relatorio():
    print("\nRELATÓRIO:\n")

    if len(funcionarios) == 0:
        print("Não existem funcionários registados")
        return

    for funcionario in funcionarios:
        funcionario.mostrar_informacoes()
        print("-" * 25)


def registrar_reparo():
    print("\nREGISTAR REPARO ")

    descricao = input("Descrição do reparo: ")
    tecnicos = []

    for funcionario in funcionarios:
        if isinstance(funcionario, TecnicoManutencao):
            tecnicos.append(funcionario)

    if len(tecnicos) == 0:
        print("Não existem técnicos registados")
        return

    for i, tecnico in enumerate(tecnicos):
        print(i + 1, "-", tecnico.nome)

    escolha = int(input("Escolha o técnico: "))

    if escolha < 1 or escolha > len(tecnicos):
        print("Opção inválida!")
        return

    tecnicos[escolha - 1].registrar_reparo(descricao)

###########################################################

while True:
        print("\n===== HOTEL =====")

        print("1 - Criar quarto")
        print("2 - Listar quartos")
        print("3 - Registar hóspede")
        print("4 - Listar hóspedes")
        print("5 - Fazer checkout")
        print("6 - Criar funcionário")
        print("7 - Imprimir relatório")
        print("8 - Registar reparo")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            criar_quarto()
        elif opcao == "2":
            listar_quartos()
        elif opcao == "3":
            criar_hospede()
        elif opcao == "4":
            listar_hospedes()
        elif opcao == "5":
            fazer_checkout()
        elif opcao == "6":
            criar_funcionario()
        elif opcao == "7":
            relatorio()
        elif opcao == "8":
            registrar_reparo()
        elif opcao == "0":
            break
        else:
            print("Opção inválida!")