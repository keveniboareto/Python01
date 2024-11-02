def Media(n1,n2,n3,n4):
    media=(n1+n2+n3+n3)/4
    if(media>=7):
        return f"APROVADO COM {media}"
    elif(media<7 and media>4):
        return f"RECUPERAÇÃO COM {media}"
    else:
        return f"REPROVADO COM {media}"

def Definemedia(nome):
    notas=[]
    for i in range(4):
        notas.append(float(input(f'Digite a {i+1}º nota:')))
    print(f'O aluno {nome} está: {Media(notas[0],notas[1],notas[2],notas[3])}')

for i in range(5):
        nomeAluno=input('Digite o nome do aluno:')
        Definemedia(nomeAluno)
    
