print('=-'*12)
print('SEQUÊNCIA DE FIBONACCI')
print('=-'*12)
n = int(input('Escreva quantos termos da Sequência de Fibonacci você deseja: '))
t1 = 0
t2 = 1
print('~'*12)
print(f'{t1} → {t2}', end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(f' → {t3}', end='')
    t1 = t2
    t2 = t3
    cont += 1
print(f' → FIM')