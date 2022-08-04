sexo = input('Informe seu sexo. [M/F]: ').strip().upper()[0]
while not sexo != 'M' or sexo != 'F':
    sexo = input('Erro! Escreva corretamente [M/F]:  ').strip().upper()
print('Ok!')