number = int(input('Escreva um número inteiro: '))
rest = number % 2
if number == 0:
    print('O número 0 não é par nem ímpar!')
elif rest == 0:
    print(f'O número {number} é par!')
else:
    print(f'O número {numer} é impar!')