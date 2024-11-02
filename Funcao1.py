def ProgramaInfantis():
    lista1=['Peppa Pig', 'Chaves', 'Pantera cor de Rosa','Tom e Jerry']
    print(lista1) 
    return
def Carros():
    carro=[
        {
        "modelo":'Jeep Renegade',
        "preço":120000
    },
    {
        "modelo":'Amarok',
        "preço":350000
    },
    {
        "modelo":'Hb20',
        "preço":100000
    },
    {
        "modelo":'Mobi',
        "preço":70000
    }
    ]
    for c in carro:
         print(f'{c["modelo"]} Preço: R${c["preço"]}')
    return
    # lista2=['Jeep Renegade - R$ 120.000', 'Amarok - R$350.000',"Hb20 - R$100.000",'Mobi - R$ 70.000']
    # print(lista2)
idade=int(input('digite sua idade:'))
if (idade>=18):
    Carros()
else:
    ProgramaInfantis()




    
    