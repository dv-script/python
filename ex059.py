produto = continuar = menorproduto = ''
preço = tot = maisdemil = preçobarato = 0
while True:
    produto = str(input('Qual produto o senhor(a) deseja? ')).strip().capitalize()
    preço = float(input('Qual o valor do produto? R$'))
    continuar = input('Deseja continuar? [S/N]: ').upper().strip()
    tot += preço
    if preço > 1000:
        maisdemil += 1
    if preçobarato <= preço:
        menorproduto = produto
    if continuar == 'N':
        break
print(f'O valor total foi de R${tot:.2f}')
print(f'Há {maisdemil} produtos que custam mais de R$1000.00')
print(f'O {menorproduto} é o produto mais barato!')