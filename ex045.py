frase = input('Escreva uma frase: ').strip().upper()
splitado = frase.split()
junto = ''.join(splitado)
inverso = ''
for c in range(len(junto)-1,-1,-1):
    inverso += junto[c]
if inverso == junto:
    print(f'A sua frase é um palíndromo! {junto} ao inverso é {inverso}')
else:
    print('Sua frase não é um palíndromo!')