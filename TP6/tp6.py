#aluno = (nome, id, [notaTPC, notaProj, notaTeste])
#turma = [alunos]

turma = []
programa = True


def inserirAluno():
    continuar = True
    while continuar:
        nome = input('Introduza o nome do aluno: ')
        id = int(input('Introduza o id do aluno: '))
        alunoemturma = False
        for aluno in turma:
            if id == aluno[1]:
                alunoemturma = True
        if alunoemturma:
            print("Aluno já se encontra inserido na turma.")
        else:
            notaTPC = int(input('Introduza a nota do TPC do aluno: '))
            notaProj = int(input('Introduza a nota do Projeto do aluno: '))
            notaTeste = int(input('Introduza a nota do teste do aluno: '))
            notas = [notaTPC, notaProj, notaTeste]
            turma.append((nome, id, notas))
            print("Aluno inserido")

        op = input("Deseja continuar? [S/N] ").strip().upper()
        while op not in ['S', 'N']:
            print("Por favor, insira apenas 'S' ou 'N'.")
            op = input("Deseja continuar? [S/N] ").strip().upper()
        
        continuar = (op == 'S')
        

def listarTurma():
    print('Aluno         Id         TPC         Projeto         Teste')
    print('--------------------------------------------------------------')
    for aluno in turma:
        print(f'{aluno[0]}        {aluno[1]}         {aluno[2][0]}            {aluno[2][1]}             {aluno[2][2]}')
        print('----------------------------------------------------------')

def consultarId(id):
    idexiste = False
    for aluno in turma:
        if id == aluno[1]:
            print('Aluno         Id         TPC         Projeto         Teste')
            print('----------------------------------------------------------------')
            print(f'{aluno[0]}        {aluno[1]}         {aluno[2][0]}            {aluno[2][1]}             {aluno[2][2]}')
            idexiste = True
    if not idexiste:
        print('id não encontrado')

def guardarTurma(fnome):
    f = open(fnome, 'w')
    for nome, id, notas in turma:
        linha = f'{nome}::{id}::{notas[0]}::{notas[1]}::{notas[2]}\n'
        f.write(linha)
    f.close()

def carregarTurma(fnome):
    turmacarregada = []
    f = open(fnome)
    for linha in f:
        campos = linha.split('::')
        notas = (int(campos[2]), int(campos[3]), int(campos[4]))
        turmacarregada.append((campos[0], int(campos[1]), notas))
    f.close()
    return turmacarregada

def menu():
    print('''
1) Inserir Aluno
2) Listar Turma
3) Procurar por Id
4) Guardar turma num documento
5) Carregar turma de um documento
0) Sair''')



while programa:
    menu()
    op = input('Qual a opção que deseja? ')
    if op == '1':
        inserirAluno()
    elif op == '2':
        listarTurma()
    elif op == '3':
        id = int(input('Qual o id do aluno que procura? '))
        consultarId(id)
    elif op == '4':
        fnome = 'turma.txt'
        guardarTurma(fnome)
    elif op == '5': 
        turmacarregada = carregarTurma('turma.txt')
        print(turmacarregada)
    elif op == '0':
        programa = False
    else:
        print('Opção inválida, tente novamente')
        menu()
        op = input('Qual a opção que deseja? ')


print('A encerrar o programa... ')

