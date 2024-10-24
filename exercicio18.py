nota1=float(input("digite a primeira nota:"))
nota2=float(input("digite a segunda nota:"))
media=(nota1+nota2)/2
print(f'a media do aluno é: {media}')
if(media<4):
    print("aluno reprovado!")
elif(media>7):
    print("aluno aprovado direto!")
else:
        print("aluno em recuperação!")
        recuperação=float(input('digite a nota de recuperação'))
        if(recuperação<5):
             print("reprovado na recuperação")
        else:
             print('aprovado na recuperação')
             
        