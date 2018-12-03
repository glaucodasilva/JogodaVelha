mesa = [['#']*3,['#']*3,['#']*3]
jogador = ''
novamente = ''
inicio = True

def cls(): print("\n" * 50)

def imprime_mesa(mesa):
    global inicio
    if inicio == True:
        if jogador.upper() == 'X':
            print('A partir de agora você será representado na mesa por X e seu adversário por O.')
        else:
            print('A partir de agora você será representado na mesa por O e seu adversário por X.')
        print('Bom Jogo!')
        print('')
        inicio = False
    for i in range(3):

        print('     |     |     ')
        print('  ' + '  |  '.join(mesa[i]) + '  ')
        if i <= 1:
            print('_ _ _|_ _ _|_ _ _')
        else:
            print("     |     |     ")
    print('')

def jogada(jogador):
    global mesa
    print('Jogador %s efetue sua jogada: ' %jogador)
    jog = input()
    if jog.isdigit() == True and 0 < int(jog) <= 9:
        jog = int(jog)
        if jog <= 3:
            mesa[2][jog-1] = jogador
        elif jog <= 6:
            mesa[1][jog-4] = jogador
        elif jog <= 9:
            mesa[0][jog-7] = jogador
    else:
        print('POSIÇÃO INVÁLIDA, POR FAVOR SELECIONE UM NÚMERO ENTRE 1 E 9! \n')
        jogada(jogador)

def vencedor(mesa):
    x = ['X','X','X']
    o = ['O','O','O']
    for i in range(3):
        if mesa[i] == x or mesa[i] == o:
            continua(mesa[i][0])
    for i in range(3):
        linha = []
        for j in range(3):
            linha += mesa[j][i]
        if linha == x or linha == o:
            continua(mesa[j][i])
    if [mesa[0][0], mesa[1][1], mesa[2][2]] == x or [mesa[0][0], mesa[1][1], mesa[2][2]] == o or [mesa[0][2], mesa[1][1], mesa[2][0]] == x or [mesa[0][2], mesa[1][1], mesa[2][0]] == o:
        continua(mesa[1][1])

def continua(jogador):
    global novamente
    cls()
    imprime_mesa(mesa)
    print('O vencedor foi o jogador', jogador)
    print('')
    while novamente.capitalize() != 'Y' and novamente.capitalize() != 'N':
        print('Deseja jogar novamente? Digite Y para sim e N para não.')
        novamente = input()

def limpamesa(mesa):
    for i in range(3):
        for j in range(3):
            mesa[i][j] = '#'

def primeiro():
    global jogador
    while jogador.upper() != 'X' and jogador.upper() != 'O':
        cls()
        print('Escolha entre X e O para iniciar o jogo!')
        jogador = input().upper()

def empate(novamente, mesa):
    for i in range(3):
        for j in range(3):
            if mesa[i][j] == '#':
                return
    cls()
    imprime_mesa(mesa)
    print('Jogo Empatado!')
    while novamente.capitalize() != 'Y' and novamente.capitalize() != 'N':
        print('Deseja jogar novamente? Digite Y para sim e N para não.')
        novamente = input()
    limpamesa(mesa)

primeiro()
while True:
    cls()
    imprime_mesa(mesa)
    jogada(jogador)
    vencedor(mesa)
    empate(novamente, mesa)
    if novamente.capitalize() == 'N':
        break
    elif novamente.capitalize() == 'Y':
        jogador = 'O'
        novamente = ''
        limpamesa(mesa)
    if jogador == 'X':
        jogador = 'O'
    else:
        jogador = 'X'
