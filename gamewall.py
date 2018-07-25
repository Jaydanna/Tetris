#！/user/bin/python
# -*- coding: UTF-8 -*-

import pygame
import setting

class GameWall():
    def __init__(self,screen):
        self.screen = screen
        self.area = []
        line = [WALL_BLANK_LABEL]*COLUMN_NUM
        for i in range(R_NUM):
            self.area.append(line[:])
    
    def print(self):
        print(len(self.area),"rows",len(self.area[0]),"column")
        for line in self.area:
            print(line)