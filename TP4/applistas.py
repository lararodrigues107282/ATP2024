def menu():
    print('Menu')
    print('0) Sair')
    print('1) Criar Lista')
    print('2) Ler Lista')
    print('3) Soma')
    print('4) Média')
    print('5) Maior')
    print('6) Menor')
    print('7) estaOrdenada por ordem crescente')
    print('8) estaOrdenada por ordem descresente')
    print('9) Procura um elemento')

import random

def criaLista():
    lista = []
    i = 0
    N = int(input('Quantos números pretende ter na sua lista?'))
    while i < N:
        lista.append(random.randint(1, 100))
        i = i + 1
    return lista

def lerLista():
    lista = []
    i = 1
    N = int(input('Quantos números pretende ter na sua lista?'))
    while i <= N:
        num = int(input('Insira um número'))
        lista.append(num)
        i = i + 1
    return lista

def soma(lista):
    soma = 0 
    for num in lista:
        soma = soma + num
    return soma

def mediaLista(lista):
    soma = 0
    i = 0
    while i < len(lista):
        soma = soma + lista[i]
        i = i + 1
    media = soma/len(lista)
    return media

def maiorLista(lista):
    maior = lista[0]
    for num in lista:
        if num > maior:
            maior = num
    return maior

def menorLista(lista):
    menor = lista[0]
    for num in lista:
        if num < menor:
             menor = num
    return menor

def ordemCrescente(lista):
    estaordenada = True
    for i in range(len(lista) - 1):
        if lista[i] >= lista [i + 1]:
            estaordenada = False
    return print('Sim') if estaordenada else print('Não')

def ordemDecrescente(lista):
    estaordenada = True
    for i in range(len(lista) - 1):
        if lista[i] <= lista [i + 1]:
            estaordenada = False
    return print('Sim') if estaordenada else print('Não')

def procuraElem(lista):
    contador = 0
    N = int(input('Qual elemento procura?'))
    encontrado = False
    for num in lista:
        if num == N:
            print(f'O elemento que procura encontra-se na posição {contador}')
            encontrado = True
        contador = contador + 1
    if not encontrado:
        print('-1')
    return

opcao = -1
minha_lista = []
while opcao != 0:
    menu()
    opcao = int(input('Seleciona a opção desejada:'))
    if opcao not in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
        print('Resposta inválida')
        menu()
        opcao = int(input('Seleciona a opção desejada:'))

    if opcao == 1:
        minha_lista = criaLista()
        print(f' a sua lista é {minha_lista}')
    elif opcao == 2:
        minha_lista = lerLista()
        print(f' a sua lista é {minha_lista}')
    if (opcao != 1 or 2) and minha_lista == []:
        print('Ainda não tem uma lista.')
        print('Escolha uma das seguintes opções: 1) Criar Lista  2) Ler Lista  0) Sair')
    elif opcao == 3:
        print(soma(minha_lista))
    elif opcao == 4:
        print(mediaLista(minha_lista))
    elif opcao == 5:
        print(maiorLista(minha_lista))
    elif opcao == 6:
        print(menorLista(minha_lista))
    elif opcao == 7:
        ordemCrescente(minha_lista)
    elif opcao == 8:
        ordemDecrescente(minha_lista)
    elif opcao == 9:
        print(procuraElem(minha_lista))
    
print(f'A sua lista é {minha_lista}')
print('Obrigada, volte sempre!')