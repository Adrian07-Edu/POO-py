VACIO = ' '

# Piezas negras
CABALLO_N = '♞'
TORRE_N = '♜'
ALFIL_N = '♝'
REINA_N = '♛'
REY_N = '♚'
PEON_N = '♟'

# Piezas blancas
CABALLO_B = '♘'
TORRE_B = '♖'
ALFIL_B = '♗'
REINA_B = '♕'
REY_B = '♔'
PEON_B = '♙'


board = [[VACIO for x in range(8)] for y in range(8)]

board[0][0] = TORRE_B
board[1][0] = CABALLO_B
board[2][0] = ALFIL_B
board[3][0] = REINA_B
board[4][0] = REY_B
board[5][0] = ALFIL_B
board[6][0] = CABALLO_B
board[7][0] = TORRE_B

for x in range(8):
    board[x][1] = PEON_B
    board[x][6] = PEON_N

board[0][7] = TORRE_N
board[1][7] = CABALLO_N
board[2][7] = ALFIL_N
board[3][7] = REINA_N
board[4][7] = REY_N
board[5][7] = ALFIL_N
board[6][7] = CABALLO_N
board[7][7] = TORRE_N

for x in range(8):
    print(board[x])
