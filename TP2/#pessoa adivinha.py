#pessoa adivinha
import random

tentativas = 1
min = 0
max = 100
x = random.randint(min, max)
y = int(input('Qual o número que pensei?'))

while y != x and tentativas <= 7:
    if y < x:
        print(f'O número que pensei é maior que {y}')
        y = int(input('O número que pensei é maior. Qual o número que pensei?'))
        tentativas = tentativas + 1 
    elif y > x:
        print(f'O número que pensei é menor que {y}')
        y = int(input('O número que pensei é menor. Qual o número que pensei?'))
        tentativas = tentativas + 1

if y == x:
    print(f'Parabéns! Acertaste em {tentativas} tentativas!')
else:
    print('Esgoastaste as tuas tentativas :(')