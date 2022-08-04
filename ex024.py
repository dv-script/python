trip = int(input('Quantos kilometros é a sua viagem? '))
if trip <= 200:
    cost = trip * 0.5
    print(f'Sua viagem custará R${cost}')
else:
    cost = trip * 0.45
    print(f'Sua viagem custará R${cost}')
