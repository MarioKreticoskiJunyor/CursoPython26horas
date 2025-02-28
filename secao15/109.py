from sys import getsizeof
# Generator expressions
#     uma forma mais rapida para listas, dicionarioos e etc 
#     menos memoria alocada 
#     Valores em bytes



numeros = [x * 10 for x in range(1000000)]
print(type(numeros))
# print(numeros)
print(getsizeof(numeros))

print()

numeros = (x * 10 for x in range(1000000))
print(type(numeros))
# print(list(numeros))
print(getsizeof(numeros))
