# Erros
#     excelente para testes
#     não realiza o 'stop' no programa
#     mensagens customizadas quando encontra o erro 

try:
    letras = ['a','b','c']

    print(letras[3])
except IndexError:
    print(f'Index nao existe')