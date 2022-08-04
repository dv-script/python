# Manipulando Texto

# Fatiamento
# frase[9]
# frase[0:13] - exclui o ultimo
# frase[9:21:2] - pulando de dois em dois
# frase[:5] - do inicio
# frase[15:] - até o final
# frase[9::2] - até o final de dois em dois

# Análise
# len(frase) - quantos caracteres possui
# frase.count('o') - contadores de 'o' na frase inteira
# frase.count('o',0,13) - contador de 'o' do inicio a decima terceira posição
# frase.find('deo') - quantas vezes é encontrado 'deo' na frase
# 'Curso' in frase - True ou False

# Transformação
# frase.replace(Python, Android) - substitui na frase a palavra 'Python' por 'Android'
# frase.upper() - coloca a frase toda em maiusculo
# frase.lower() - coloca a frase toda em minusculo
# frase.captalize() - coloca a primeira letra da frase em maiusculo
# frase.title() - coloca a primeira letra de cada palavra na frase em maiusculo
# frase.strip() - corta os espaços inuteis no inicio e no final da frase
# frase.rstrip() - corta os espaços inuteis no final da frase
# frase.lstrip() - corta os espaços inuteis no inicio da frase

# Divisão
# frase.split() - divide cada palavra da frase em uma nova frase, gerando uma lista com essas novas frases
# '-'.join(frase) - junta todas as frases com o termo entre as aspas

# Caso queira escrever quebrando as linhas com o enter, utilize """

frase = 'Curso em Video Python'
print(len(frase.strip()))
print(frase.count('o'))
print(frase.count('O'))
print(frase.upper().count('O'))
print(frase.find('o'))
print(frase.title())
print(frase[::2])
print(frase[:6])
print('-'.join(frase))
print(frase.split())
print(frase.replace('Python', 'Android'))
print('Curso' in frase)
print(frase.find('Curso'))
splitado = frase.split()
print(splitado[0])
print(splitado[0][3])

