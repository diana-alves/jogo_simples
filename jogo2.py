from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')

print('SUA ESCOLHA:')
print('[0] PEDRA\n[1] PAPEL\n[2] TESOURA')

jogador = int(input('Digite sua jogada: '))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('POW')
sleep(1)

print('-=-' * 11)

computador = randint(0, 2)

print('O computador escolheu -->', itens[computador])
print('O jogador escolheu -->', itens[jogador])

if 0 <= jogador <= 2:
    if computador == jogador:
        print('Empate')
    elif (jogador - computador) % 3 == 1:
        print('Jogador Venceu!')
    else:
        print('Computador Venceu!')
else:
    print('Jogada Inválida')
