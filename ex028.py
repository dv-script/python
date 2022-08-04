l1 = float(input('Escreva o valor do primeiro lado do triângulo: '))
l2 = float(input('Escreva o valor do segundo lado do triângulo: '))
l3 = float(input('Escreva o valor do terceiro lado do triângulo: '))
if l1 + l2 > l3 and l2 + l3 > l1 and l1 + l3 > l2:
    print(f'Os lados podem formar um triângulo!')
else:
    print(f'Os lados não podem formar um triângulo!')
