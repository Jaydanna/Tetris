#!/usr/bin/python
# -*- coding: UTF-8 -*-

from setting import *
import pygame
from pygame import *
from gamedisplay import *


class Piece():
    def __init__(self,shape,screen):
        self.x = 4
        self.y = 0
        self.shape = shape
        self.turn_times = 0
        self.screen = screen 
        self.is_on_buttom = False

    def paint(self):
        shape_template = PIECES[self.shape]
        shape_turn = shape_template[self.turn_times]

        for r in range(len(shape_turn)):
            for c in range(len(shape_turn[0])):
                if shape_turn[r][c] == 'O':
                    self.draw_cell(self.x + c,self.y + r)

    def draw_cell(self,x,y):
        # cell_position = (x * CELL_WIDTH + GAME_AREA_LEFT + 1 ,
        #                  y * CELL_WIDTH + GAME_AREA_TOP + 1)
        # cell_wide_height = (CELL_WIDTH - 2  ,CELL_WIDTH - 2)
        # cell_rect = pygame.Rect(cell_position,cell_wide_height)
        # pygame.draw.rect(self.screen,PIECE_COLORS[self.shape],cell_rect)           
        GameDisplay.draw_cell(self.screen, x, y, PIECE_COLORS[self.shape])

    def move_right(self):
        if self.can_move_right():
            self.x += 1
    
    def move_left(self):
        if self.can_move_left():
            self.x -= 1

    def move_down(self):
        if self.can_move_button():
            self.y += 1
        else:
            self.is_on_buttom = True
    
    def fall_down(self):
        while not self.is_on_buttom:
            self.move_down()

    def can_move_right(self):
        shape_mtx = PIECES[self.shape][self.turn_times]
        for r in range(len(shape_mtx)):
            for c in range(len(shape_mtx[0])):
                if shape_mtx[r][c] == 'O':
                    if self.x + c >= C_NUM - 1:
                        return False
        return True

    def can_move_left(self):
        shape_mtx = PIECES[self.shape][self.turn_times]
        for r in range(len(shape_mtx)):
            for c in range(len(shape_mtx[0])):
                if shape_mtx[r][c] == 'O':
                    if self.x + c <= 0:
                        return False
        return True
    
    def can_move_button(self):
        shape_mtx = PIECES[self.shape][self.turn_times]
        for r in range(len(shape_mtx)):
            for c in range(len(shape_mtx[0])):
                if shape_mtx[r][c] == 'O':
                    if self.y + r >= R_NUM - 1:
                        return False
        return True
    
    def turn(self):
        shape_list_len = len(PIECES[self.shape])
        if self.can_turn():
            self.turn_times = (self.turn_times + 1) % shape_list_len
    
    def can_turn(self):
        shape_list_len = len(PIECES[self.shape])
        turn_times = (self.turn_times + 1) % shape_list_len
        shape_mtx = PIECES[self.shape][turn_times]
        for r in range(len(shape_mtx)):
            for c in range(len(shape_mtx[0])):
                if shape_mtx[r][c] == 'O':
                    if (self.x + c < 0 or self.x + c >= C_NUM) or (self.y + r < 0 or self.y + r >= R_NUM):
                        return False
        return True

