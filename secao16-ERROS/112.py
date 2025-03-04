# Erros
#     excelente para testes
#     não realiza o 'stop' no programa
#     mensagens customizadas quando encontra o erro 

try:
    valor = int(input('Digite o valor do seu produto:'))
    print(valor)
except ValueError:
    print('Favoir digitar um valor em numeros')


print('mais codigos abaixo')