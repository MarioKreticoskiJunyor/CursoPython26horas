# For loop nested 
#     outer loop 
#         inner loop
# Gerar um retangulo
# 
# @@@@@@
# @@@@@@
# @@@@@@
# @@@@@@
# @@@@@@
# @@@@@@
#  


linhas = 6
colunas = 6
simbolo = '@'


for l in range(linhas):
    for c in range(colunas):
        print(simbolo, end='')
    print()
    