# JOGO PEDRA, PAPEL, TESOURA
jogador1=input('escolha sua opção entre pedra, papel e tesoura:')
jogador2=input('escolha sua opção entre pedra, papel e tesoura:')
if(jogador1==jogador2):
    print("empate")
elif((jogador1=='pedra' and jogador2=='tesoura') or (jogador1=='papel'and jogador2=='pedra') or (jogador1=='tesoura' and jogador2=='papel')):
    print(f'jogador1 venceu!({jogador1} venceu do {jogador2})')
else:
    print(f'jogador2 venceu!({jogador2} venceu do {jogador1})')
    