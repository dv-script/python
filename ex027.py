salario = float(input('Escreva o seu salário : R$'))
if salario <= 1250:
    print(f'Seu salário após o aumento de 15% será de R${salario*1.15:.2f}!')
else:
    print(f'Seu salário após o aumento de 10% será de R${salario*1.1:.2f}')
