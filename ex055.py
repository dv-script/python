n = 0
cont = 0
soma = 0
while True:
    n = int(input('Escreva um valor: '))
    if n == 999:
        break
    cont += 1
    soma += n
print(f'Você digitou {cont} números! E a soma deles é {soma}')