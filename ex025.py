year = int(input('Qual ano desejar analisar? '))
result = year % 4
if result == 0:
    print('Seu ano é bissexto!')
else:
    print('Seu ano não é bissexto!')