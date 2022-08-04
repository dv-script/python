from random import randint
n = (randint(1,10000), randint(1,10000), randint(1,1000), randint(1,10000), randint(1,10000))
print('Sorteei os números: ', end='')
for c in n:
    print(f'{c}', end=' ')
print(f'\nO maior valor foi de {max(n)}!')
print(f'O menor valor foi de {min(n)}!')
