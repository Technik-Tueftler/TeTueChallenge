def print_field(field):
    for row in field:
        print(' '.join([str(pos) for pos in row]))


sizeX = int(input('width: '))
sizeY = int(input('height: '))

# sizeX, sizeY = 6, 5

field = [[0] * (sizeX) for i in range((sizeY))]
print_field(field)

playing = True
while playing:
    posX = int(input(f'attack x (0-{sizeX-1}): '))
    posY = int(input(f'attack y (0-{sizeY-1}): '))
    field[posY][posX] = 'X'

    print_field(field)

    playerinput = input('want to fire again?(Y/n): ')

    if playerinput.lower() == 'y' or playerinput == '':
        playing = True
    else:
        playing = False
        print('\nso long, and thanks for all the fish')


