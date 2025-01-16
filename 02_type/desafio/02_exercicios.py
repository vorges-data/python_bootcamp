# #### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
# numero_1 = int(input('Digite o primeiro número: '))
# numero_2 = int(input('Digite o segundo número: '))
# soma = numero_1 + numero_2
# print(f'A soma dos números é: {soma}')


# 2. Crie um programa que receba um número do usuário e calcule o resto d6a divisão desse número por 5.
# numero = int(input('Digite um número: '))
# resto = numero % 5
# print(f'O resto da divisão por 5 é: {resto}')

# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
# numero_1 = int(input('Digite o primeiro número: '))
# numero_2 = int(input('Digite o segundo número: '))
# multiplicacao = numero_1 * numero_2
# print(f'A multiplicação dos números é: {multiplicacao}')

# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
# numero_1 = int(input('Digite o primeiro número: '))
# numero_2 = int(input('Digite o segundo número: '))
# divisao = numero_1 // numero_2
# print(f'A divisão inteira dos números é: {divisao}')


# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
# numero = int(input('Digite um número: '))
# quadrado = numero ** 2
# print(f'O quadrado do número é: {quadrado}')

# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
# numero_1 = float(input('Digite o primeiro número: '))
# numero_2 = float(input('Digite o segundo número: '))
# soma = numero_1 + numero_2
# print(f'A soma dos números é: {soma}')


# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
# numero_1 = float(input('Digite o primeiro número: '))
# numero_2 = float(input('Digite o segundo número: '))
# media = (numero_1 + numero_2) / 2
# print(f'A média dos números é: {media}')

# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
# base = float(input('Digite a base: '))
# expoente = float(input('Digite o expoente: '))
# potencia = base ** expoente
# print(f'{base} elevado a {expoente} é igual a: {potencia}')

# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
# celsius = float(input('Digite a temperatura em Celsius: '))
# fahrenheit = (celsius * 9/5) + 32
# print(f'A temperatura em Fahrenheit é: {fahrenheit}')

# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
# import math
# raio = float(input('Digite o raio do círculo: '))
# area = math.pi * raio ** 2
# print(f'A área do círculo é: {area}')

# #### Strings (`str`)
# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
# string = input('Digite uma string: ')
# string_maiuscula = string.upper()
# print(f'A string em maiúsculas é: {string_maiuscula}')

# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
# nome = input('Digite seu nome completo: ')
# nome_minusculo = nome.lower()
# print(f'O nome em minúsculas é: {nome_minusculo}')

# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
# frase = input('Digite uma frase: ')
# frase_sem_espacos = frase.strip()
# print(f'A frase sem espaços em branco no início e no final é: {frase_sem_espacos}')

# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
# data = input('Digite uma data no formato "dd/mm/aaaa": ')
# dia, mes, ano = data.split('/')
# print(f'Dia: {dia}')
# print(f'Mês: {mes}')
# print(f'Ano: {ano}')

# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.
# string_1 = input('Digite a primeira string: ')
# string_2 = input('Digite a segunda string: ')
# concatenacao = string_1 + string_2
# print(f'A concatenação das strings é: {concatenacao}')

# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
# expressao_1 = True
# expressao_2 = False
# resultado = expressao_1 and expressao_2
# print(f'O resultado da operação AND é: {resultado}')


# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
# expressao_1 = True
# expressao_2 = False
# resultado = expressao_1 or expressao_2
# print(f'O resultado da operação OR é: {resultado}')

# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
# valor = True
# valor_invertido = not valor
# print(f'O valor invertido é: {valor_invertido}')

# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
# numero_1 = int(input('Digite o primeiro número: '))
# numero_2 = int(input('Digite o segundo número: '))
# iguais = numero_1 == numero_2
# print(f'Os números são iguais? {iguais}')


# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
# numero_1 = int(input('Digite o primeiro número: '))
# numero_2 = int(input('Digite o segundo número: '))
# diferentes = numero_1 != numero_2
# print(f'Os números são diferentes? {diferentes}')

# #### try-except e if

# 21: Conversor de Temperatura
# try:
#     celsius = float(input('Digite a temperatura em Celsius: '))
#     fahrenheit = (celsius * 9/5) + 32
#     print(f'A temperatura em Fahrenheit é: {fahrenheit}')
# except ValueError:
#     print('Digite um valor numérico válido.')

# 22: Verificador de Palíndromo
# palavra = input('Digite uma palavra: ')
# if isinstance(palavra, str):
#     formatado = palavra.lower().replace(' ', '')
#     if formatado == formatado[::-1]:
#         print('A palavra é um palíndromo.')
#     else:
#         print('A palavra não é um palíndromo.')
# else:
#     print('Digite uma palavra válida.')

# 23: Calculadora Simples
# 


# 24: Classificador de Números
# try:
#     numero = int(input('Digite um número: '))
#     if numero > 0:
#         print('O número é positivo.')
#     elif numero < 0:
#         print('O número é negativo.')
#     else:
#         print('Zero')
#     if numero % 2 == 0:
#         print('O número é par.')
#     else:
#         print('O número é ímpar.')
# except ValueError:
#     print('Digite um valor numérico válido.')

# 25: Conversão de Tipo com Validação
# entrada = input('Digite um número inteiro separado por vírgula: ')
# numeros_str = entrada.split(',')
# numeros_int = []
# try:
#     for numero in numeros_str:
#         numeros_int.append(int(numero.strip()))
#     print(f'Os números inteiros são: {numeros_int}')
# except ValueError:
#     print('Digite um valor numérico válido.')