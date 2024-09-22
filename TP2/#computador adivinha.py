#computador adivinha
import random

tentativas = 0
min = 0
max = 100
y = random.randint(min, max)
x = (input(f'O número que pensaste é {y}'))

while x != 'Acertaste!' and tentativas <= 7:
    if x == 'maior':
        min = y + 1
        y = random.randint(min, max)
        x = (input(f'O número que pensaste é {y}'))
        tentativas = tentativas + 1
    elif x == 'menor':
        max = y - 1
        y = random.randint(min, max)
        x = (input(f'O número que pensaste é {y}'))
        tentativas = tentativas + 1
    
if x == 'Acertaste!': 
    print(f'Finalmente! Acertei, em {tentativas} tentativas.')
else:
    print('Não consegui adivinhar em 7 tentativas... :(')