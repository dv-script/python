import math
catop = float(input('Escreva o valor do cateto oposto: '))
catad = float(input('Escreva o valor do cateto adjacente: '))
hip = math.sqrt(catop**2 + catad**2)
print(f'O valor da hipotenusa é de {hip}')