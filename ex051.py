p = float(input('Escreva o primeiro termo de uma P.A: '))
r = float(input('Escreva a razão dessa P.A: '))
termo = p
cont = 1
n = int(input('Escreva quantos termos você deseja ter nessa P.A: '))
while cont <= n:
   print(f'{termo:.2f}', end=' → ')
   termo += r
   cont += 1
print('...')
