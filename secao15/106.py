# Filter function
#     muito utilizado com listas
#     Aplicar uma funcao a um iterable, por item. (list, tupla, dic, etc.)


valores = [10, 12, 34, 44, 57]


# def remover20(x):
#     return x > 20

# print(list(filter(remover20, valores)))

print(list(filter(lambda x: x > 20, valores)))
