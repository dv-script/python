from datetime import date
ano = int(input('Escreva o ano em que você nasceu: '))
atual = date.today().year
idade = atual - ano
if idade <= 9:
    print('Categoria Mirim')
elif idade > 9 and idade <= 14:
    print('Categoria Infatil')
elif idade > 14 and idade <= 19:
    print('Categoria Junior')
elif idade > 19 and idade <= 25:
    print('Categoria Sênior')
else:
    print('Categoria Master')
