#APP METEO

tabmeteo = []

def inserir(tab):
    continuar = True
    while continuar:
        data = (int(input('Insira o ano: ')), int(input('Insira o mês: ')), int(input('Insira o dia: ')))
        data_existe = False
        for dia in tab:
            if dia[0]==data:
                data_existe = True
        if data_existe:
                print('Dia já registado')
        else:
            temp_min = int(input('Insira a temperatura mínima: '))
            temp_max = int(input('Insira a temperatura máxima: '))
            prec = float(input('Insira a pluviosidade: '))
            tab.append((data, temp_min, temp_max, prec))

        op = input("Deseja continuar? [S/N] ").strip().upper()
        while op not in ['S', 'N']:
            print("Por favor, insira apenas 'S' ou 'N'.")
            op = input("Deseja continuar? [S/N] ").strip().upper()
    
        continuar = (op == 'S')
    return tab

def medias(tab):
    res = []
    for i in tab:
        tempmedia = (i[2] + i[1])/2
        res.append((i[0], tempmedia))
    return res

def guardaTabMeteo(tab, fnome):
    f = open(fnome, 'w')
    for data, tmin, tmax, precip in tab:
        linha = f'{data[0]}::{data[1]}::{data[2]}::{tmin}::{tmax}::{precip}\n'
        f.write(linha)
    f.close()
    return f'Tabela guardada no ficheiro {fnome}.txt'

def carregaTabMeteo(fnome):
    f = open(fnome, 'r')
    res = []
    for linha in f:
        campos = linha.split('::')
        data = (int(campos[0]), int(campos[1]), int(campos[2]))
        res.append((data, float(campos[3]), float(campos[4]), float(campos[5])))
    f.close()
    return 'A tabela carregada é:', res


def minMin(tab):
    minima = tab[0][1]
    for i in tab:
        if i[1] < minima:
            minima = i[1]
    return 'A temperatura mínima mais baixa registada é:', minima

def amplTerm(tab):
    res = []
    for i in tab:
        amp = i[2] - i[1]
        res.append((i[0], amp))
    return 'As amplitudes térmicas de cada dia são:', res

def maxChuva(tab):
    max_prec = tab[0][3]
    for i in tab:
        if i[3] > max_prec:
            max_prec = i[3]
            max_data = i[0]
    return 'O dia e valor de maior precipitação foram:', (max_data, max_prec)

def diasChuvosos(tab, p):
    res = []
    for i in tab:
        if i[3] > p:
            res.append((i[0], i[3]))
    if res == []:
        res = f'Não há dias com precipitação superior a {p}'
    return res if res == [] else f'Os dias com precipitação superior a {p} foram:', res


def maxPeriodoCalor(tab, p):
    res = 0
    consecutivo = 0
    for i in tab:
        if i[3] < p:
            res += 1
        else: 
            if res > consecutivo:
                consecutivo = res
            res = 0   
    if res > consecutivo:
                consecutivo = res 
    return f'O nº de dias consecutivos com precipitação inferior a {p} é:', consecutivo


import matplotlib.pyplot as plt

def grafTabMeteo(t):
    dia=[]
    min=[]
    max=[]
    prec=[]
    for dias in t:
       dia.append(dias[0][2])
       min.append(dias[1])
       max.append(dias[2])
       prec.append(dias[3])

    plt.plot(dia,min)
    plt.xlabel('Dias')
    plt.ylabel('Temperatura')
    plt.title('Temperaturas Mínimas')
    plt.show()

    plt.plot(dia,max)
    plt.xlabel('Dias')
    plt.ylabel('Temperatura')
    plt.title('Temperaturas Máximas')
    plt.show()

    plt.plot(dia,prec)
    plt.xlabel('Dias')
    plt.ylabel('Quantidade Precipitação')
    plt.title('Precipitação')
    plt.show()
    
def main():
    print('''1) Inserir novos dados meteorológicos
2) Consultar a temperatura média dos dias disponíveis
3) Guardar a tabela num ficheiro
4) Carregar uma tabela de um ficheiro
5) Consultar a temperatura mínima absoluta registada
6) Consultar a amplitude térmica dos dias disponíveis
7) Consultar o valor de precipitação máxima registada
8) Filtrar os dados da tabela para precipitações superiores a p
9) Consultar o número de dias consecutivos com precipitação inferior a p
10) Consultar gráficos
0) Sair''')
    
programa = True
while programa:
    tab = tabmeteo
    main()
    op = input('Qual operação deseja realizar? ')
    if op not in '12345678910':
        print('Opção inválida.')
    elif op == '1':
        print(inserir(tab))
    elif op == '2':
        print(medias(tab))
    elif op == '3':
        f = input('Insira o nome do ficheiro ')
        fnome = f'{f}.txt'
        print(guardaTabMeteo(tab, fnome))
    elif op == '4':
        print(carregaTabMeteo('meteorologia.txt'))
    elif op == '5':
        print(minMin(tab))
    elif op == '6':
        print(amplTerm(tab))
    elif op == '7':
        print(maxChuva(tab))
    elif op == '8':
        p = float(input('Insira o limite mínimo de precipitação: '))
        print(diasChuvosos(tab, p))
    elif op == '9':
        p = float(input('Insira o limite máximo de precipitação: '))
        print(maxPeriodoCalor(tab,p))
    elif op == '10':
        print(grafTabMeteo(tab))
    elif op == '0':
        programa = False
print('Programa encerrado')