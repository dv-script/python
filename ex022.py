vel = int(input('Escreva a velocidade, em Km/hr, do carro: '))
if vel > 80:
    print('Você foi multado! A velocidade máxima é de 80Km/hr!')
    print(f'A multa é de R${(vel-80)*7}!')
else:
    print('Você está dentro do limite de velocidade da pista!')