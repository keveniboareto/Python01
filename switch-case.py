# value=3
# match value:
#     case 1:
#         result='one'
#     case 2:
#         result='two'
#     case 3:
#         result='three'
#     case _:
#         result='default'          
# print(result) 
# ******************************************************************************
total=0
escolha=0
while(escolha!=5):
    print('Cardápio: ')
    print('1- calabresa com cebola -R$59,90\n2- camarão com catupiry - R$87,90\n3- frango com requeijão -R$ 60,50\n4- banana com chocolate - R$ 49,90')
    print('5- finalizar pedido')
    escolha=int(input('digite a opção escolhida (apenas números):'))
    match escolha:
        case 1:
            print("calabresa com cebola - R$ 59,90")
            total+=59.90
        case 2:
            print('camarão com catupiry - R$ 87,90')
            total+=87.90
        case 3:
            print('frango com requeijão - R$60,50 ')
            total+=60.50
        case 4:
            print('banana com chocolate - R$49,90')
            total+=49.90
        case 5:
            print(f'total do pedido: R${total}')
        case _:
           print("escolha uma opção valida")



