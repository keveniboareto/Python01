alunos=[]
for i in range(5):
    nome=input(f'Digite o nome do aluno{i+1}:')
    while True:
        try:
            media=float(input(f"Digite a média do aluno {nome} (entre 0 e 10):"))
            if 0 <= media<=10:
                break
            else:
                print("A média deve estar entre 0 e 10. Tente Novamente.")
        except:
            print("Entrada inválida. Por Favor, digite um número.")
            alunos.append((nome, media))
        print('\nLista de alunos e suas médias:')
        for nome, media in alunos:
            print(f"Nome:{nome}, Média:{media:.2f}")
