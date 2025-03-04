# lista
#     Armazenar mais de uma informaçao em variaveis 
#     Manter a sequencia dos dados em uma variavel


cores = ['amarelo','verde','azul','vermelho']
cor_cliente = input('Informe a cor desejada: ')


if cor_cliente.lower() in cores:
    print('Em estoque')
else:
    print('Não temos esta cor em estoque')