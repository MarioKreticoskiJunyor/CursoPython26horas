from array import array

# array (Matriz)

# Similar a listas 
# melhor performance


letras = ['a','b','c', 'd']
numeros_i = [10,20,30,40]
numeros_f = [1.2,2.2,3.2]


print(letras)
print(numeros_i)
print(numeros_f)

print()



letras = array('u',['a','b','c', 'd'])
numeros = array('i',[10,20,30,40])
numeros = array('f',[1.2,2.2,3.2])


print(letras)
print(numeros)
