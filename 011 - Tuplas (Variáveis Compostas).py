# Tuplas (Variáveis Compostas)

# A Tupla é uma variável composta

lanche = ('Hambúrger', 'Suco', 'Ovo', 'Pudim')
# lanche: tuple[str, str, str, str] = ('Hambúrger', 'Suco', 'Ovo', 'Pudim')

print(lanche[3])
print(lanche[1:3])
print(lanche[2:])
print(lanche[:2])
print(lanche[-2:])

# Tuplas são IMUTÁVEIS!
# lanche[1] = 'Refrigerante'
# print(lanche[1]) - ERRO!
print('=-'*20)

c : str # Nova atualização devemos definir qual tipo de string é a variável
for c in lanche:
    print(c)
print('=-'*20)

for c in range(len(lanche)): # Não é necessario citar o 0 no range(0,len(lanche))
    print(f'Eu vou comer {lanche[c]} na {c+1}ª posição!')
print('=-'*20)

for pos, c in enumerate(lanche):
    print(f'Eu vou comer {c} na {pos+1}ª posição!')
print('=-'*20)

print(sorted(lanche)) # Acaba se tornando uma lista!
                      # () = Tuplas
                      # [] = Listas
                      # {} = Dicionários
print('=-'*20)

a: tuple[int, int, int] = (2, 5, 4)
b: tuple[int, int, int, int] = (5, 8, 1, 2)
c: tuple = a + b
print(c)
print(c.count(5))
print(len(c))
print(c.index(8)) # Posição na Tupla
print('=-'*20)

pessoa: tuple[int, str, int, int] = (2, 'Davi', 0 , 3)
print(pessoa)
del(pessoa) # Exclui qualquer tipo de dado anterior que citava PESSOA
