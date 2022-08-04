valor = float(input('Valor do produto: R$'))
quant = int(input('Quantidade de parcelas: '))
forma = str(input('Escreva a forma de pagamento: ')).upper().strip()
if quant == 1 and forma in 'DINHEIRO CHEQUE':
    print(f'Você receberá 10% de desconto!.')
elif quant == 1 and forma in 'CARTAO CARTÃO':
    print(f'Você receberá 5% de desconto!')
elif quant == 2 and forma in 'CARTAO CARTÃO':
    print(f'Você não receberá desconto!')
elif quant >= 3 and forma in 'CARTAO CARTÃO':
    print(f'Você receberá juros de 20%!')
else:
    print('ERRO! DIGITE NOVAMENTE!')