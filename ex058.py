sexo = cont = ''
idade = maioridade = menormulher = homem = 0
while True:
    sexo = input(f'Escreva o sexo da pessoa [M/F]: ').strip().upper()
    idade = int(input(f'Escreva a idade da pessoa: '))
    cont = input('Deseja continuar? [S/N]: ').strip().upper()
    if idade > 18:
        maioridade += 1
    elif sexo == 'M':
        homem += 1
    elif idade < 20 and sexo == 'F':
        menormulher += 1
    if cont == 'N':
        break
print(f'A quantidade de pessoas com mais de 18 anos é de {maioridade}.')
print(f'A quantidade de homens é de {homem}')
print(f'A quantidade de mulheres com menos de 20 anos é de {menormulher}')
