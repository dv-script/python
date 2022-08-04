from math import sin
from math import cos
from math import tan
from math import radians
num = float(input('Escreva o valor do ângulo: '))
sin = sin(radians(num))
cos = cos(radians(num))
tan = tan(radians(num))
print(f'Seno de {num} = {sin:.2f}\nCos de {num} = {cos:.2f}\nTan de {num} = {tan:.2f}')