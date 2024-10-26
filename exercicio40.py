Lista=[]
soma=0
for i in range(10):
    Lista.append(int(input('digite um número:')))
    soma+=Lista[i]
print(f'soma:{soma}, Média:{soma/len(Lista)}')

      