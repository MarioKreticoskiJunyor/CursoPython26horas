# function
#     DRY - Don't repeat yourself 
# realiza uma tarefa 
#calcula e retorna um valor 

def cliente1(nome):
    print(f'Olá {nome}')


def cliente2(nome):
    return f'Olá {nome}'


x = cliente1('Maria')
y = cliente2('Jose')

print(x)
print(y)
