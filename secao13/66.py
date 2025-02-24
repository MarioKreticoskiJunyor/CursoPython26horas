#enviar um email com os detalhe da compra online (maximo 3 tentativas) para compras confirmada

compra_confirmada = True
dados_compra =  'Compra no valor de R$12,50 e entrega confirmada'


for enviar in range(3):
    if compra_confirmada:
        print(dados_compra)
        print('Detalhes enviado para seu emial.')
        break 
    else:
        print('Falha na compra')
        break 
