# =========  porcentagem de desconto ============

preco = float(input('Qual o preço do produto?: '))
desconto = 5 #valor do desconto por %
precofinal = preco - (desconto / 100) * preco
print (f' O valor do produto com desconto de 5% é: {precofinal:.2f} ')