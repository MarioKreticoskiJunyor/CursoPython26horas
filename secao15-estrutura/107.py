# List comprehension 
#     mais simples de escrever 
#     utilizando qunado voce precisa criar uma nova lista a partir de uma existente
#     [expressao for iten in itens]


frutas1 = ['abacate','banana', 'morango', 'kiwi', 'abacaxi']
# frutas2 = []

# for iten in frutas1:
#     if 'n' in iten:
#         frutas2.append(iten)

frutas2 = [iten for iten in frutas1 if 'k' in iten]

print(frutas2)