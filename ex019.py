frase = input('Escreva uma frase: ').strip().upper()
print(f'Sua frase possui {frase.count("A")} letras "A"')
print(f'A primeira vez que a letra "A" apareceu foi na posição {frase.find("A")+1}')
print(f'A ultima vez que a letra "A" apareceu foi na posição {frase.rfind("A")+1}')