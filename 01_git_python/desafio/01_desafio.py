nome = input('Digite seu nome: ')
salario = float(input('Digite seu salário: '))
bonus = float(input('Digite o valor do bônus: '))
constante = 1000

salario_bonus = constante + salario * bonus

print(f'{nome} seu salário com bônus é de R$ {salario_bonus:.2f}')
