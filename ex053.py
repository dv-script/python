soma = n = cont = 0
while n != 999:
    n = int(input('Escreva um valor [Digite 999 para parar]: '))
    soma += n
    cont += 1
soma -= 999
print(f'Você digitou {cont} números e a soma entre eles é de {soma}')