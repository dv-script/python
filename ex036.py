peso = float(input('Escreva seu peso, em kilogramas: '))
altura = float(input('Escreva sua altura, em metros: '))
imc = peso / altura ** 2
if imc < 18.5:
    print(f'Seu IMC é de {imc:.1f}. Você está abaixo do peso!')
elif imc >= 18.5 and imc < 25:
    print(f'Seu IMC é de {imc:.1f}. Você está no peso ideal!')
elif imc >= 25 and imc < 30:
    print(f'Seu IMC é de {imc:.1f}. Você está no sobrepeso!')
elif imc >= 30 and imc < 40:
    print(f'Seu IMC é de {imc:.1f}. Você está obeso!')
else:
    print(f'Seu IMC é de {imc:.1f}. Você está com obesidade mórbida!')
