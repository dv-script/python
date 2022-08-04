from random import randint
number = randint(0,5)
quest = int(input('Escreva o número, de 0 a 5, que o computador pensou: '))
if quest == number:
    print('Você acertou!')
else:
    print('Você errou! Tente novamente!')
