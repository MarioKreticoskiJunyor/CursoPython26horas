# Saudacao conforme o horario 
# Bom dia antes das 12pm
# Boa tarde antes das 18pm
# Boa noite depois 18 pm 

hora = int(input('Informe a hora:'))

if hora <= 12 :
    print('Bom dia')
elif hora<=18 :
    print('Boa tarde')
else: 
    print('Boa noite')