# o professor digita a nota e o sistema calcula de acordo:

# Maior ou iguial a 9, Execelente, Você tirou um A
# Maior ou iguial a 7, Bom trabalho, Você tirou um B
# Maior ou iguial a 5, Você passou mas precisa melhorar, Você tirou um C
# Qualquer nota abaixo,Reprovado!!

nota = float(input('Informe a nota: '))

if nota >= 9:
    print(f'Execelente, Você tirou um A')
elif nota >=8:
    print(f'Bom trabalho, Você tirou um B')
elif nota >=5:
    print(f'Você passou mas precisa melhorar, Você tirou um C')
else:
    print(f'Reprovado!!!')
