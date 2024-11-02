nome_mais_novo=''
idade_mais_nova=float('inf')
for i in range(10):
    nome=input(f'Digiteo nome da pessoa {i+1}:')
    idade=int(input(f'Digite a idade do {nome}'))
if idade < idade_mais_nova: idade_mais_nova = idade 
nome_mais_novo = nome
print(f'A pessoa mais nova é {nome_mais_novo}com {idade_mais_nova}')
