import random,sys
import pygame
import basicsprite
import time
"""The fireball class.Also inherits from basic sprite.Player has to dodge fireballs or will lose life"""
class fireball(basicsprite.sprite):
    def __init__(self,centerpoint,image):
        basicsprite.sprite.__init__(self,centerpoint,image)
        self.image=image
        self.direction=random.randint(1,2)
        """select random moving direction"""
        self.dist=8
        self.moves=random.randint(10,100)
        """select a random no of moves"""
        self.movecount=0
        """To update position of fireball and check collison with player"""
    def update(self,block_group1,block_group2):
        xmove=0
        ymove=0
        if self.direction ==1:
            xmove= -self.dist
        elif self.direction ==2:
            xmove = +self.dist
        elif self.direction ==3:
            ymove= self.dist
        elif self.direction ==4:
            ymove= -self.dist
        self.rect.move_ip(xmove,ymove)
        self.movecount+=1
        if pygame.sprite.spritecollideany(self,block_group1) and not pygame.sprite.spritecollideany(self,block_group2):
            self.rect.move_ip(0,-ymove)
            self.direction=random.randint(1,2)
        elif not pygame.sprite.spritecollideany(self,block_group2) and not pygame.sprite.spritecollideany(self,block_group1):
            self.rect.move_ip(0,self.dist)
        elif  pygame.sprite.spritecollideany(self,block_group2) and pygame.sprite.spritecollideany(self,block_group1):
            self.rect.move_ip(0,self.dist)
        elif pygame.sprite.spritecollideany(self,block_group1) and pygame.sprite.spritecollideany(self,block_group2):
            self.rect.move_ip(0,self.dist)
        elif self.moves == self.movecount:
            self.direction=random.randint(1,2)
            self.moves=random.randint(10,100)
            self.movecount=0


        





