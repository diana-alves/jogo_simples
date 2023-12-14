from random import randint

print('Adivinhe o número...')
print('=-=' * 20)

for c in range(0, 3):
    s = randint(1, 100)
    
    if 1 <= s <= 33:
        print('Número baixo... (1-33)')
    elif 34 <= s <= 66:
        print('Número Médio... (34-66)')
    else:
        print('Número Alto... (67-100)')

    n = int(input('Digite sua sorte: '))

    if n == s:
        print('Você acertou!!')
    else:
        print('Você errou, tente novamente...')
        print(f'O número da sorte era: {s}')
        print('=-=' * 10)
