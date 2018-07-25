#！/user/bin/python
# -*- coding: UTF-8 -*-

import pygame
from setting import *

class GameWall():
    def __init__(self,screen):
        self.screen = screen
        self.area = []
        line = [WALL_BLANK_LABEL]*C_NUM
        for i in range(R_NUM):
            self.area.append(line[:])
    
    def print(self):
        print(len(self.area),"rows",len(self.area[0]),"column")
        for line in self.area:
            print(line)
    
    def add_to_wall(self):
        shape_turn = PIECES[piece.shape][piece.turn_times]
        for r in range(len(shape_turn)):
            for c in range(len(shape_turn)):
                if shape_turn[r][c] == 'O':
                    self.set_cell((piece.x + c,piece.y + r),piece.shape)
    
    def set_cell(self,position,shape_label):
        c,r = position
        self.area[r][c] = shape_label