num = int(input('Escreva um valor: '))
print('''Escolha uma das bases para conversão:
[1] BINÁRIO
[2] OCTAL
[3] HEXADECIMAL''')
opc = int(input('Sua opção: '))
if opc == 1:
    print(f'Transformando esse valor em binário -> {bin(num)[2:]}')
elif opc == 2:
    print(f'Transformando esse valor em octal -> {oct(num)[2:]}')
elif opc == 3:
    print(f'Transformando esse valor em hexadecimal -> {hex(num)[2:]}')
else:
    print(f'{opc} NÃO É UMA OPÇÃO! TENTE NOVAMENTE!')