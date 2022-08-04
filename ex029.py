valor = float(input('Escreva o valor da casa: R$'))
salario = float(input('Escreva seu salário: R$'))
anos = int(input('Escreva em quantos anos irá pagar a casa: '))
prest = valor / (anos * 12)
print(f'Para pagar uma casa de {valor:.2f} em {anos} anos, a prestação será de {prest:.2f}')
min = 0.3 * salario
if prest > min:
    print('Empréstimo negado!')
else:
    print('Empréstimo concedido!')
