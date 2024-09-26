n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2 #soma
a = n1 - n2 #adição
m = n1 * n2 #multiplicação
d = n1 / n2 #divisão
di = n1 // n2 # divisão inteira
po = n1 ** n2 #potencia

print(f'A soma dos número é  {s}. O produto é {a}.',end=' ')
print(f' A divisão inteira é {di}, A multiplicação é {m} \n A apotenciação é {po} e a divisão é {d:.2f}')