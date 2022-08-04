from random import randint
print('''Aqui estão suas opções
[1] PEDRA
[2] PAPEL
[3] TESOURA''')
opc = int(input('Escreva sua opção: '))
jogo = randint(1,3)
if opc == 1 and jogo == 1:
    print('PEDRA x PEDRA. Empate!')
elif opc == 1 and jogo == 2:
    print('PEDRA x PAPEL. Derrota!')
elif opc == 1 and jogo == 3:
    print('PEDRA x TESOURA. Vitória!')
elif opc == 2 and jogo == 1:
    print('PAPEL x PEDRA. Vitória!')
elif opc == 2 and jogo == 2:
    print('PAPEL x PAPEL. Empate!')
elif opc == 2 and jogo == 3:
    print('PAPEL x TESOURA. Derrota!')
elif opc == 3 and jogo == 1:
    print('TESOURA x PEDRA. Derrota!')
elif opc == 3 and jogo == 2:
    print('TESOURA x PAPEL. Vitória!')
elif opc == 3 and jogo == 3:
    print('TESOURA x TESOURA. Empate!')
else:
    print('Erro! Tente novamente!')