import random
def Game(numero):
    player2=random.randint(0,5)
    if(numero+player2)%2==0:
        return 'PAR - Player1 venceu'
    else:
        return 'ÍMPAR - Player2 venceu'
print('Jogo - Par ou Ímpar')
print('Número permetidos - 0, 1, 2, 3, 4 ou 5')
print()
print('--------------------------------------------')
print()

jogadas=int(input('Digite quantas vezes você quer jogar'))
for i in range(jogadas):
    player1=int(input('Insira sua jogada:'))
    print(f'{Game(player1)}')

