n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
resultado = 0
opc = 0
while opc != 5:
    print('=-' * 10)
    print('''MENU DE OPÇÕES
[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NÚMEROS
[5] SAIR''')
    print('=-' * 10)
    opc = int(input('Qual sua opção? '))
    if opc == 1:
        resultado = n1 + n2
        print(f'{n1} + {n2} = {resultado}')
    elif opc == 2:
        resultado = n1 * n2
        print(f'{n1} * {n2} = {resultado}')
    elif opc == 3:
        if n1 < n2:
            print(f'{n2} é maior que {n1}!')
        elif n2 < n1:
            print(f'{n1} é maior que {n2}!')
        else:
            print(f'{n2} é idêntico a {n1}!')
    elif opc == 4:
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
    elif opc == 5:
        print('Fim do programa!')
    else:
        print('Erro! Tente novamente!')
        opc = int(input('Qual sua opção? '))
