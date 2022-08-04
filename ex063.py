n: tuple = (int(input('Escreva um valor: ')),
            int(input('Escreva outro valor: ')),
            int(input('Escreva outro valor: ')),
            int(input('Escreva outro valor: ')),
            int(input('Escreva outro valor: ')))
print(f'Você digitou os valores {n}')
print(f'O valor 9 apareceu {n.count(9)} vezes')
if 3 in n:
    print(f'O valor 3 apareceu a primeira vez na {n.index(3)+1}ª posição')
else:
    print(f'O valor 3 não apareceu!')
print('Os valores pares digitados foram: ', end='')
for c in n:
    if n % 2 == 0:
        print(c)