n = 0
while True:
    n = int(input('Escreva um número para calcular a Tabuada: '))
    if n < 0:
        break
    for c in range(1,11):
        print(f'{n} x {c} = {n*c}')
print('Fim do programa!')