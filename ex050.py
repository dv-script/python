n = int(input('Escreva um número para calcular seu fatorial: '))
cont = n
f = 1
while cont > 0:
    print(f'{cont}', end='')
    print(f' x ' if cont > 1 else ' = ', end = '')
    f *= cont
    cont -= 1
print(f)