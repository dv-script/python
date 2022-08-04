from random import randint
number = randint(0,5)
quest = int(input('Escreva o número, de 0 a 5, que o computador pensou: '))
tentativas = 0
while number != quest:
    if quest == number:
        print('Você acertou!')
    else:
        print('Você errou! Tente novamente!')
        tentativas += 1
    quest = int(input('Escreva o número, de 0 a 5, que o computador pensou: '))
print(f'Foram utilizados {tentativas} tentativas até o acerto!')