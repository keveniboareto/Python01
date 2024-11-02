import random
lista= ["pedra","papel","tesoura"]
player1=input('Escolha sua opção entre pedra, papel, tesoura:')
player2=random.choice(lista)
# print(f'player1: {player1} vs player2 {player2}')
if(player1==player2):
    print('Empate')
elif((player1=='pedra' and player2=='tesoura') or (player1=='papel' and player2=='pedra') or (player1=='tesoura' and player2=='papel')):
    print(f'O player1 venceu!!! ({player1} venceu de {player2})')
else:
    print(f'O player2 venceu!!! ({player2} venceu de {player1})')
