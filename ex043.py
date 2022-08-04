soma = 0
for c in range(1,7):
    n = int(input(f'Escreva o {c}° valor: '))
    if n % 2 == 0:
        soma += n
print(f'A soma dos números pares que você informou é de {soma}!')