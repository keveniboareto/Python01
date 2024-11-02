pessoas=[]
for i in range(10):
    nome=input(f'Digite o nome da pessoa{i+1}:')
    bairro=input(f'Digite o bairro da pessoa{i+1}:')
    pessoas.append((nome,bairro))
pessoas.sort(key=lambda x: x[0])
print("\nLista de pessoas em ordem alfabética:")
for nome,bairro in pessoas:
    print(f"Nome:{nome},Bairro:{bairro}")
    