# function
#     DRY - Don't repeat yourself 

def boa_vindas(nome, quantidade):
    print(f'Olá {nome}')
    print(f'Temos {str(quantidade)} laptops em estoque')


boa_vindas('Marcos' ,  3)
boa_vindas('Ronaldo' ,  2)
boa_vindas('Linda' ,  1)

'''
def boas_vindas_Marcos():
    print('Ola marcos!')
    print('Temos 5 laptops em estoque')


def boas_vindas_Ronaldo():
    print('Ola marcos!')
    print('Temos 5 laptops em estoque')


def boas_vindas_Linda():
    print('Ola marcos!')
    print('Temos 5 laptops em estoque')


boas_vindas_Marcos()
boas_vindas_Ronaldo()
boas_vindas_Ronaldo()

'''