# function
#     DRY - Don't repeat yourself 
#criar uma funççao que soma varios numeros

def soma(*numeros):
    resultado = 0
    for num in numeros:
        resultado += num
    return resultado


x = soma(2,3,4,7)
print(x)





