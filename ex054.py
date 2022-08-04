maior = menor = media = soma = cont = n = 0
continuar = ''
while continuar in 'S':
    n = int(input('Escreva um valor: '))
    cont += 1
    soma += n
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
    continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()
media = soma / cont
print(f'A média dos valores é de {media}. O menor valor é de {menor} e o maior é de {maior}!')
