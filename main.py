import cpfValido
import estadoValido
import cursoLista

nome = []
cpf = []
estado = []
curso = []
sair = 0
while (sair != 4):
    print('\nMenu')
    menu = int(input("1. Fazer Inscrição\n2. Alterar Inscrição\n3. Listar Inscrições\n4. Sair\n:"))
    if menu == 1:
        print("\nInformações para a inscrição:")
        _nome = input("Nome do aluno: ")
        _cpf = 0
        while cpfValido.estaValido != True:
            _cpf = input("CPF: ")
            cpfValido.validar(_cpf)
        _estado = ''
        while estadoValido.estaValido != True:
            _estado = input("Estado que deseja fazer o curso: ").upper()
            estadoValido.validar(_estado)
        cursoLista.cursos_por_estado(_estado)
        nome.append(_nome)
        cpf.append(_cpf)
        estado.append(_estado)

    elif menu == 2:
        opcao1 = int(input("1. Alterar inscrição pelo cpf\n2. Alterar inscrição pelo código de inscrição\n:"))
        if opcao1 == 1:
            alteraInscricaoCpf = int(input("Informe seu CPF: "))
        elif opcao1 == 2:
            alteraInscricaoCD = int(input("Informe o código de inscrição: "))
        else:
            print("Opção Inválida")
    elif menu == 3:
        print("nada")
    elif menu == 4:
        break
    else:
        print("Opção Inválida")