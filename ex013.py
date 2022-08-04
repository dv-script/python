from random import choice
n1 = input('Escreva o nome de um aluno: ')
n2 = input('Escreva o nome de um aluno: ')
n3 = input('Escreva o nome de um aluno: ')
n4 = input('Escreva o nome de um aluno: ')
list = [n1,n2,n3,n4]
print(f'O aluno sorteado foi {choice(list)}!')