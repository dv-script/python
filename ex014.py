from random import shuffle
n1 = input('Escreva o nome de um aluno: ')
n2 = input('Escreva o nome de um aluno: ')
n3 = input('Escreva o nome de um aluno: ')
n4 = input('Escreva o nome de um aluno: ')
list = [n1,n2,n3,n4]
shuffle(list)
print(f'A sequencia de alunos escolhida foi {list}!')