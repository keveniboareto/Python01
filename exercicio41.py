numeros=[]
for i in range(8):
    numeros.append(int(input('digite um numero:')))
numeros.sort()
print(f'O maior é:{numeros[len(numeros)-1]}) e o menor é:{numeros[0]}')

