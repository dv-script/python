# Operadores Aritmeticos
# + Adicão
# - Subtração
# * Multiplicação
# / Divisão
# ** Potência
# // Divisão inteira
# % Resto da divisão

# Ordem de Precedência
# 1° ()
# 2° **
# 3° * / // %
# 4° + -

print('='*20)
print('Olá Mundo!')
print('='*20)

n1 = int(input('Insira um valor: '))
n2 = int(input('Insira outro valor: '))
s = n1 + n2
dif = n1 - n2
mult = n1 * n2
div = n1 / n2
pot = n1 ** n2
rest = n1 % n2
divint = n1 // n2
print(f'A soma de {n1} e {n2} é de {s}!')
print(f'A diferença de {n1} e {n2} é de {dif}!')
print(f'A multiplicação de {n1} e {n2} é de {mult}!')
print(f'A divisão de {n1} e {n2} é de {div}!')
print(f'A potência de {n1} elevado a {n2} é de {pot}!')
print(f'O resto da divisão entre {n1} e {n2} é de {rest}!')
print(f'A divisão inteira entre  {n1} e {n2} é de {divint}!')

# end('') para continuar na mesma linha
# \n para quebrar a linha