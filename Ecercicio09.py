# ========= exercicio  porcentagem de aumento de salário feito pelo patão

salario = float(input('Qual o valor do salário do funcionário?: '))
aumento = float(input('Qual a porcentagem do aumento do salário você quer dar?: '))
novosalario = salario + (aumento / 100) * salario
print (f'O novo salário com aumento de {aumento:.0f}% é {novosalario:.2f}')
