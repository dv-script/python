# Estrutura de Repetição While

cont = 1
while cont <= 10:
    print(cont)
    cont += 1
print('Fim!')

r = 'S'
while r == 'S':
    n = int(input('Escreva um valor: '))
    r = str(input('Deseja continuar [S] ou [N]')).strip().upper()
print('Fim!')