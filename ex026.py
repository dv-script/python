n1 = int(input('Escreva o primeiro número: '))
n2 = int(input('Escreva o segundo número: '))
n3 = int(input('Escreva o terceiro número: '))
if n1 > n2 and n2 > n3:
    print(f'O {n1} é o maior número e o {n3} é o menor!')
elif n1 > n3 and n3 > n2:
    print(f'O {n1} é o maior número e o {n2} é o menor!')
elif n2 > n1 and n1 > n3:
    print(f'O {n2} é o maior número e o {n3} é o menor!')
elif n2 > n3 and n3 > n1:
    print(f'O {n2} é o maior número e o {n1} é o menor!')
elif n3 > n1 and n1 > n2:
    print(f'O {n3} é o maior número e o {n2} é o menor!')
elif n3 > n2 and n2 > n1:
    print(f'O {n3} é o maior número e o {n1} é o menor!')
else:
    print('Você digitou algo errado!')