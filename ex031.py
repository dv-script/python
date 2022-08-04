n1 = int(input('Escreva um valor: '))
n2 = int(input('Escreva outro valor: '))
if n1 > n2:
    print(f'{n1} é maior que {n2}')
elif n2 > n1:
    print(f'{n2} é maior que {n1}')
else:
    print(f'{n1} é igual a {n2}')
