from setting import *
import pygame

class Piece():
    def __init__(self,shape,screen):
        self.x = 3
        self.y = 0
        self.shape = shape
        self.screen = screen 

    def paint(self):
        shape_template = PIECES[self.shape]

        for r in range(len(shape_template)):
            for c in range(len(shape_template[0])):
                if shape_template[r][c] == 'O':
                    self.draw_cell(self.x + c,self.y + r)

    def draw_cell(self,x,y):
        cell_position = (x * CELL_WIDTH + GAME_AREA_LEFT + 1 ,
                         y * CELL_WIDTH + GAME_AREA_TOP + 1)
        cell_wide_height = (CELL_WIDTH - 2  ,CELL_WIDTH - 2)
        cell_rect = pygame.Rect(cell_position,cell_wide_height)
        pygame.draw.rect(self.screen,CELL_COLOR,cell_rect)           

    def move_right(self):
        if self.can_move_right():
            self.x += 1
    
    def move_left(self):
        if self.can_move_left():
            self.x -= 1

    def move_down(self):
        if self.can_move_button():
            self.y += 1

    def can_move_right(self):
        shape_mtx = PIECES[self.shape]
        for r in range(len(shape_mtx)):
            for c in range(len(shape_mtx[0])):
                if shape_mtx[r][c] == 'O':
                    if self.x + c >= C_NUM - 1:
                        return False
        return True

    def can_move_left(self):
        shape_mtx = PIECES[self.shape]
        for r in range(len(shape_mtx)):
            for c in range(len(shape_mtx[0])):
                if shape_mtx[r][c] == 'O':
                    if self.x + c <= 0:
                        return False
        return True
    
    def can_move_button(self):
        shape_mtx = PIECES[self.shape]
        for r in range(len(shape_mtx)):
            for c in range(len(shape_mtx[0])):
                if shape_mtx[r][c] == 'O':
                    if self.y + r >= R_NUM - 1:
                        return False
        return True


