# function
#     DRY - Don't repeat yourself 
#     Varios argumentos(xargs) identificando o Parametro 
#Criar uma função que armazena numeros e strings (dados)

def agencia(**carro):
    return carro


print(agencia(marca = 'Gol', cor = 'Branco', motor = 1.0, placa=1234))
print(agencia(marca = 'Gol', cor = 'azul', motor = 1.0))
print(agencia(marca = 'Gol', cor = 'Preto', motor = 1.0, placa=1444))