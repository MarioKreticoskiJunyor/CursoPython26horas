# # While loops
# Excelente para loops dependentes de uma condição
#Publicar um produto com comçissao de 10% se for acima de R$20

valor = int(input('Digite o valor do seu produto:'))

while valor > 20:
    valor = (valor * 0.10) + valor
    print(f'O valor final do seu produto sera de R${valor}')
    break

