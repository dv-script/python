# Arrays (Listas)

lanche = ['Hambúrger', 'Pizza', 'Japa', 'Refri', 'Suco']

lanche.insert(0,'Cachorro-Quente') # Adiciona na posição em que você escolheu e arrasta os demais para a direita
# lanche.append('Costela') - Adiciona o item ao final da array
print(lanche)

del(lanche[3])  # Deleta o n° item da array
print(lanche)

lanche.pop(3) # Deleta o n° item da array
lanche.pop()
print(lanche)

lanche.remove('Pizza') # Deleta o item da array
# Caso possua mais de um '3' na array, del(lanche[3] irá deletar apenas o primeiro da lista!
print(lanche)

if 'Pizza' in lanche:
    lanche.remove('Pizza')

valores = list(range(1,11)) # Cria uma array com a sequência dentro do range
print(valores)

numbers = [8,3,2,1,7,6,5,9,0]
nomes = ['Davi', 'Isabella', 'Douglas', 'Enzo']
nomes.sort() # Colocamos em ordem alfabética
numbers.sort() # Colocamos em ordem crescente
print(numbers, nomes)

nomes.sort(reverse=True) # Colocamos em ordem alfabética de trás para frente
numbers.sort(reverse=True) # Colocamos em ordem decrescente
print(numbers, nomes)

print(len(numbers)) # Quantidade de elementos dentro da array

lista = []
for c in range(0,5):
    lista.append(int(input('Escreva um valor: ')))
print(lista)

array = []
while True:
    if 999 not in array:
        array.append(int(input('Escreva um valor: ')))
    else:
        array.pop()
        break
print(array)

a = [1,2,3,4,5]
b = a # Dessa forma quando alteramos algo em b, iremos alterar em a juntamente
b[2] = 8
print(a,b)

c = [1,2,3,4,5]
d = c[:] # Dessa forma iremos apenas copiar os itens de dentro de c para d. Dessa forma, não será alterado em a quando alterarmos em d
d[2] = 8
print(c,d)
