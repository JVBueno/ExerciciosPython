from random import randint
from time import sleep
itens = ('Pedra','Papel','Tesoura')
computador = randint (0 , 2)
print('[0] PEDRA\n[1] PAPEL\n[2] TESOURA')
humano = int(input('Digite sua jogada:'))
sleep(0.5)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO !!')
sleep(0.5)
print('-'* 30)
print('Computador escolheu: {}'.format(itens[computador]))
print('-'* 30)
print('Você escolheu: {}'.format(itens[humano]))
print('-'* 30)
if computador == 0: # PEDRA
    if humano == 0:
        print('Empate')
    elif humano == 1:
        print('Ganhou')
    elif humano == 2:
        print('Perdeu')
    else:
        print('Jogada Inválida')
elif computador == 1: #PAPEL
    if humano == 0:
        print('Perdeu')
    elif humano == 1:
        print('Empate')
    elif humano == 2:
        print('Vitória')
    else:
        print('Jogada Inválida')

elif computador == 2: #TESOURA
    if humano == 0:
        print('Vitória')
    elif humano == 1:
        print('Perdeu')
    elif humano == 2:
        print('Empate')
    else:
        print('Jogada Inválida')





