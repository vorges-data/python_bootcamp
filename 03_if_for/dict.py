texto = "Python é uma linguagem de programação de alto nível."
palavras = texto.split()

# Cria um dicionário vazio
dicionario = {}

# Conta a quantidade de vezes que cada palavra aparece no texto
for palavra in palavras:
    if palavra in dicionario:
        dicionario[palavra] += 1
    else:
        dicionario[palavra] = 1

# Imprime o dicionário
print(dicionario)