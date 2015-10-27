import pygame
import basicsprite
from helper import *
WIDTH=640
"""The donkey class.Inherits from self defined basic sprite model.this refers to the villain or the Donkey Kong"""
class donkey(basicsprite.sprite):
    def __init__(self,centerpoint,image=None):
        basicsprite.sprite.__init__(self,centerpoint,image)
        self.x_dist=10
        self.xmove=0
        self.ymove=0
    def move(self,flag=1):
        if flag==0:
            if self.xmove<=WIDTH/6:
                self.xmove+= self.x_dist
            else:
                self.xmove+= -self.x_dist
        else:
            if self.xmove>=0:
                self.xmove+= -self.x_dist
    """function to update position of donkey kong"""
    def update(self,block_group):
        self.rect.move_ip(self.xmove,self.ymove)
        if not pygame.sprite.spritecollide(self,block_group,False):
            self.rect.move_ip(-self.xmove,-self.ymove)

    
