pessoas=[]
for i in range(10):
    nome=input(f'Digite o nome da pessoa{i+1}:')
    telefone=input(f'Digite o telefone da pessoa{i+1}:')
    cidade=input(f'Digite a cidade da pessoa{i+1}:')
    pessoas.append({"nome":nome,"telefone":telefone,"cidade":cidade})
print("\nPessoas que moram em 'Campo Grande':" )
for pessoa in pessoas:
    if pessoa['cidade'].lower()=="campo grande":
        print(f"Nome:{pessoa['nome']},Telefone:{pessoa['telefone']}")
