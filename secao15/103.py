# Lambda 
#     e uma função (pequena) sem nome
#     pode ter varios argumentos mas somente 1 expressao 
#     muito utilizada dentro de outras funções
#     codigo mais 'clean'



def somar(x):
    func2 = lambda x: x + 10
    return func2(x) * 4


print(somar(2))