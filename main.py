import cpfValido
import estadoValido
import cursoLista


nome = []
cpf = []
estado = []
curso = []
aluno = [nome, cpf, estado, curso]
sair = 0
while (sair != 4):
    print('\nMenu')
    menu = int(input("1. Fazer Inscrição\n2. Alterar Inscrição\n3. Listar Inscrições\n4. Sair\n:"))
    if menu == 1:
        print("\nInformações para a inscrição:")
        _nome = input("Nome do aluno: ")
        _cpf = 0
        while not cpfValido.estaValido:
            _cpf = input("CPF: ")
            cpfValido.validar(_cpf)
        _estado = ''
        while not estadoValido.estaValido:
            _estado = input("Estado que deseja fazer o curso: ").upper()
            estadoValido.validar(_estado)
        cursoLista.cursos_por_estado(_estado)
        _curso = input("Escolha um dos cursos disponíveis: ")
        nome.append(_nome)
        cpf.append(_cpf)
        estado.append(_estado)
        curso.append(_curso)
        cpfValido.estaValido= False
        estadoValido.estaValido = False

    elif menu == 2:
        opcao1 = int(input("1. Alterar inscrição pelo cpf\n2. Alterar inscrição pelo código de inscrição\n:"))
        if opcao1 == 1:
            alteraInscricaoCpf = int(input("Informe seu CPF: "))
        elif opcao1 == 2:
            alteraInscricaoCD = int(input("Informe o código de inscrição: "))
        else:
            print("Opção Inválida")
    elif menu == 3:
        matriz = [nome, cpf, estado, curso]
        print("Imprimir lista aninhada: ")
        for lista in aluno:
            for elemento in lista:
                print(elemento, end=' ')
            print()
        print('Total de alunos: ', len(aluno[0]))
        print(json.loads(aluno[0]))
    elif menu == 4:
        break
    else:
        print("Opção Inválida")
