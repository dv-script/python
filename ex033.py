n1 = float(input('Insira sua primeira nota: '))
n2 = float(input('Insira sua segunda nota: '))
media = (n1 + n2) / 2
if media < 5:
    print('Você foi reprovado!')
elif media > 5 and media < 7:
    print('Você está em recuperação!')
else:
    print('Você está aprovado!')