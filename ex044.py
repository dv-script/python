n = int(input('Escreva um número inteiro: '))
tot = 0
for c in range(1,n+1):
    if n % c == 0:
        tot += 1
if tot > 2:
    print('Seu número não é primo!')
else:
    print('Seu número é primo!')