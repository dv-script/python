from random import randint
seq = n = game = soma = 0
opc = ''
print('=' * 20)
print('JOGO DO IMPAR OU PAR')
print('=' * 20)
while True:
    opc = input('\033[1;37mEscreva sua opção [IMPAR/PAR]: ').strip().upper()
    n = int(input('Escreva o valor que deseja jogar: '))
    game = randint(1,100)
    soma = game + n
    if soma % 2 == 0:
        if opc == 'PAR':
            print('\033[1;32mVocê venceu!')
            print(f'\033[1;32mEu joguei {game}!')
            seq += 1
        elif opc == 'IMPAR' or opc == 'ÍMPAR':
            print('\033[1;31mVocê perdeu!')
            print(f'\033[1;31mEu joguei {game}!')
            break
    elif soma % 2 != 0:
        if opc == 'IMPAR' or opc == 'ÍMPAR':
            print('\033[1;32mVocê venceu!')
            print(f'\033[1;32mEu joguei {game}!')
            seq += 1
        elif opc == 'PAR':
            print('\033[1;31mVocê perdeu!')
            print(f'\033[1;31mEu joguei {game}!')
            break
if seq > 5:
    print(f'A sua sequência de vitórias foi de {seq}! Parabéns!')
else:
    print(f'A sua sequência de vitórias foi de {seq}! Vamos melhorar!')
