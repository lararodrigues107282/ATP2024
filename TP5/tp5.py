#Cinema = [Sala]
##Sala = [nlugares, Vendidos, filme, numsala]
#nlugares = Int
#filme = String 
#Vendidos = [Int]

#---------------------------------------------------------#
from datetime import date
cinemaUM = []


def criarSala(cinema):
    filme = input("Introduza o nome do filme: ")
    nlugares = int(input("Introduza o numero de lugares na sala: "))
    vendidos = []
    numsala = input('Introduza o nome da sala (ex: s1): ')
    sala_existe = False
    for n in cinema:
        if filme == n[2] or numsala == n[3]:
            print("Sala ou filme já existem.")
            sala_existe = True
    if not sala_existe:
        cinema.append((nlugares, vendidos, filme, numsala))
        print("Sala criada")
    
    print("Salas:", cinema)


def listar(cinema):
    print('Sala          Filme')
    print('-----------------------')
    for sala in cinema:
        print(f' {sala[3]}          {sala[2]}')
    today = date.today()
    print('-----------------------')
    print(today)

def listardisponibilidade(cinema):
    print('Sala          Filme          Nº lugares disponíveis')
    print('---------------------------------------------------')
    for sala in cinema:
        print(f'{sala[3]}           {sala[2]}                    {int(sala[0]) - len(sala[1])}')
    today = date.today()
    ('---------------------------------------------------')
    print(today)

def disponivel(cinema, filme, lugar):
    filme_existe = False
    for sala in cinema:
        if filme == sala[2]:
            if lugar in sala[1]:
                print('False')
            else:
                print('True')
            filme_existe = True
    if not filme_existe:
        for sala in cinema:
            print("Filme não se encontra em exposição.")
            

def vendelugar(cinema, filme, lugar):
    lugar_vendido = False
    for sala in cinema:
            nlugares, vendidos, nome, numsala = sala
            if filme == nome:
                if lugar not in vendidos:
                    vendidos.append(lugar)
                    print(f'Bilhete vendido para o lugar {lugar}')
                    lugar_vendido = True
                else:
                    print('Lugar já vendido')
    if not lugar_vendido:
            print('Operação não é possível')
    print('Sala          Filme          Lugares Ocupados')
    print('---------------------------------------------')
    for sala in cinema:
        print(f'{sala[3]}         {sala[2]}              {sala[1]}')
    today = date.today()
    print('---------------------------------------------')
    print(today)


def menu():
    print('''1) Criar Sala
2) Listar Cinema
3) Listar Disponibilidade
4) Confirmar Disponibilidade
5) Vender Bilhete
0) Sair''')

op = -1
while op != 0:
    menu()
    op = int(input('Selecione a opção que deseja: '))
    if op == 1:
        criarSala(cinemaUM)
    elif op == 2:
        listar(cinemaUM)
    elif op == 3:
        if cinemaUM == []:
            print('Cinema sem filmes em exposição')
        else:
            listardisponibilidade(cinemaUM)
    elif op == 4:
        if cinemaUM == []:
            print('Cinema sem filmes em exposição')
        else:
            filme = input('Qual o filme que deseja ver? ')
            lugar = int(input('Qual o lugar que deseja? '))
            disponivel(cinemaUM, filme, lugar)
    elif op == 5:
        if cinemaUM == []:
            print('Cinema sem filmes em exposição')
        else:
            filme = input('Qual o filme que deseja ver? ')
            lugar = int(input('Qual o lugar que deseja? '))
            vendelugar(cinemaUM, filme, lugar)
    elif op not in [0, 1, 2, 3, 4, 5]:
        print('Opção inválida')
print('Programa Encerrado.')

