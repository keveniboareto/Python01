nota1=float(input("digite a primeira nota:"))
nota2=float(input("digite a segunda nota:"))
nota3=float(input("digite a terceira nota:"))
nota4=float(input("digite a quarta nota:"))
media=(nota1+nota2+nota3+nota4)/4
print(f"média: {media}")

if(media<6):
    print("aluno reprovado")
else:
    print("aluno aprovado")
    

