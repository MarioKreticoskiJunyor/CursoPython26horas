# usuárioo tem que entrar com o valor da compra 
# Compra de qualquer valor = 5% de desconto 
# Acima de R$100 = desconto 10%
# Acima de R$200 = desconto 20%

compra = float(input('Informe o valor da compra R$'))
desconto = compra
if compra > 200 :
    desconto = (desconto * 1.20) - compra
    compra = compra -desconto
    print(f'valor do desconto foi de:{desconto:.2f}')
    print(f'valor da compra com desconto:{compra:.2f}')
elif compra >100 :
    desconto = (desconto * 1.10) - compra
    compra = compra -desconto
    print(f'valor do desconto foi de:{desconto:.2f}')
    print(f'valor da compra com desconto:{compra:.2f}')
else: 
    desconto = (desconto * 1.05) - compra
    compra = compra -desconto
    print(f'valor do desconto foi de:{desconto:.2f}')
    print(f'valor da compra com desconto:{compra:.2f}')
    