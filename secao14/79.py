# function
#     DRY - Don't repeat yourself 
# paranetro ---> Argumento
# Default = aquele que voce define o valor no parametro
# non-default = aquele que voce nao define o valor no parametro

def boa_vindas(quantidade, nome='linda'):
    print(f'Olá {nome}')
    print(f'Temos {str(quantidade)} laptops em estoque')

boa_vindas(1)