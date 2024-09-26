# ========= exercicio 13 ==== porcentagem de aumento de salário

salario = float(input('Qual o valor do seu salário?: '))
aumento = 15
novosalario = salario + (aumento / 100) * salario
print (f'Seu novo salário com aumento de 15% é {novosalario:.2f}')