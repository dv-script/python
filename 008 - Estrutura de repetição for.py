# Estrutura de repetição for

print('Oi!')
print('Oi!')
print('Oi!')

for c in range(1,4): # O último número não está incluso no número de repetições
    print('Oi!')
print('Até mais!')

for c in range(1,6): # Contador de números dentro do range
    print(c)

for c in range(6,0,-1): # Contador de números. O terceiro número indica qual será a sequência
    print(c)

for c in range(1,6,2):
    print(c)

p = int(input('Escreva um número: '))
for c in range(1,p):
    print(c)

n1 = int(input('Escreva o inicio: '))
f = int(input('Escreva o fim: '))
p = int(input('Escreva o passo: '))
for c in range(n1,f+1,p):
    print(c)

s = 0
for c in range(0,5):
    n = int(input('Escreva um valor: '))
    s += n
print(f'O somatório dos valores é de {s}!')

