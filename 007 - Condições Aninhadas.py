# Condições Aninhadas
# Utiliza-se elif para uma condição múltipla

name = input('Escreva seu nome: ').capitalize()
if name == 'Davi':
    print('Que nome lindo você tem!')

elif name == 'Pedro' or name == 'João':
    print('Seu nome é bem comum no Brasil!')

elif name in 'Isabella Ana Claúdia Joana Márcia':
    print('Que belo nome feminino!')

else:
    print('Que nome horrível você tem!')
print(f'Bom dia, {name}!')
