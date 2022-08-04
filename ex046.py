mediaidade = 0
quantf = 0
nomevelho = ''
maioridadehomem = 0
for c in range(1, 5):
    nome = input(f'Escreva o nome da {c}° pessoa: ').strip()
    sexo = input(f'Escreva qual o sexo da {c}° pessoa - [M] ou [F]: ').upper().strip()
    idade = int(input(f'Escreva a idade da {c}° pessoa: '))
    mediaidade += idade / 4
    if sexo == 'F' and idade < 20:
        quantf += 1
    if c == 1 and sexo == 'M':
        maioridadehomem = idade
        nomevelho = nome
    if sexo == 'M' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
print(f'A média das idades é de {mediaidade}')
if quantf == 1:
    print(f'Existe {quantf} mulher com menos de 20 anos')
elif quantf == 0:
    print(f'Não há mulheres com menos de 20 anos!')
else:
    print(f'Existe {quantf} mulheres com menos de 20 anos')
print(f'O nome do homem mais velho é {nomevelho}, com {maioridadehomem} anos!')
