ano = int(input('Escreva o ano em que você nasceu: '))
idade = 2022 - ano
if idade == 18:
    print('Você deve se alistar esse ano!')
elif idade > 18:
    print(f'Você deveria ter se alistado há {idade-18}!')
elif idade < 18:
    print(f'Você irá se alistar daqui a {(idade-18)*(-1)} ano(s)!')