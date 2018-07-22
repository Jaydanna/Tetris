SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 720
CELL_WIDTH = 40
R_NUM = 18
C_NUM = 10
GAME_AREA_WIDTH = CELL_WIDTH * C_NUM
GAME_AREA_HEIGHT = CELL_WIDTH * R_NUM
GAME_AREA_LEFT = (SCREEN_WIDTH - GAME_AREA_WIDTH)//2
GAME_AREA_TOP = 0
EDGE_COLOR = (0,0,0)
CELL_COLOR = (100,100,100)
BG_COLOR = (230,230,230)

##Shape
S_SHAPE_TEMPLATE = ['.OO.',
                    'OO..',
                    '....']

Z_SHAPE_TEMPLATE = ['OO..',
                    '.OO.',
                    '....']

I_SHAPE_TEMPLATE = ['.O..',
                    '.O..',
                    '.O..',
                    '.O..']

O_SHAPE_TEMPLATE = ['OO',
                    'OO']

J_SHAPE_TEMPLATE = ['..O.',
                    '..O.',
                    '.OO.']

L_SHAPE_TEMPLATE = ['.O..',
                    '.O..',
                    '.OO.']

T_SHAPE_TEMPLATE = ['.O..',
                    'OOO.',
                    '....']

PIECES = {'S': S_SHAPE_TEMPLATE,
          'Z': Z_SHAPE_TEMPLATE,
          'J': J_SHAPE_TEMPLATE,
          'L': L_SHAPE_TEMPLATE,
          'I': I_SHAPE_TEMPLATE,
          'O': O_SHAPE_TEMPLATE,
          'T': T_SHAPE_TEMPLATE}                       