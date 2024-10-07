print('Menu:')
print('1) Jogador começa primeiro')
print('2) Computador começa primeiro')
modalidade=(input('Qual a modalidade em que deseja jogar?' ))

import random
if modalidade == '1':
    i = 21
    while i > 1:
        x = int(input('Quantos fósforos tira? (1 a 4)'))
        y = 5 - x
        print(f'tiro {y} fósforos.')
        i = i - x - y
        print(f'restam {i} fósforos!')
    print ('Perdeste')


if modalidade == '2':
    i = 21
    while i > 1:
        y = (i - 1) % 5
        if y == 0:
            y = random.randint(1, min(4, i))
        print (f'tiro {y} fósforos')
        i = i - y
        print(f'restam {i} fósforos!')
        if i == 1:
            print('Perdeste')
        x = int(input('Quantos fósforos tira? (1 a 4)'))
        i = i - x
        print(f'restam {i} fósforos')
        if i == 1:
            print('Perdi :(')
        
        
        

            