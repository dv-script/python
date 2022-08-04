name = input('Escreva seu nome completo: ').strip().title()
splitado = name.split()
print(f'Seu primeiro nome é {splitado[0]}')
print(f'Seu último nome é {splitado[len(splitado)-1]}')

