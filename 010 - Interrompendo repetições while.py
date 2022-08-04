# Interrompendo repetições while

cont = 1
while True:
    print(cont)
    cont += 1
    if cont == 100:
        break
print('Fim!')

n = 0
soma = 0
while True:
    n = int(input('Escreva um valor: '))
    if n == 999:
        break
    soma += n
print(f'A soma vale {soma}')

