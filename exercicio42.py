lista=[]
for i in range(10):
    lista.append(int(input('digite um numero:')))
maior_que_dez= sum(1 for lista in lista if lista>10)
print(f'Quantidade de números maiores que dez:{maior_que_dez}')

