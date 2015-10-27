import pygame,time
import basicsprite
from helper import *
"""The user defined events"""
DEAD=pygame.USEREVENT + 1
WIN=DEAD+1
BL=WIN+1
"""The player class.controls all activities of the player.Also inherits from basicsprite"""
class player(basicsprite.sprite):
    def __init__(self,centerpoint,image):
        basicsprite.sprite.__init__(self, centerpoint, image)
        """Initialize the number of coins taken"""
        self.points = 0
        """Set the number of Pixels to move each time"""
        self.x_dist = 10
        self.y_dist = 10
        """Initialize how much we are moving"""
        self.xMove = 0
        self.yMove = 0
        self.j=False
        self.g=4
        self.yvel=-20
        self.lives=3
    def MoveKeyDown(self,key,block_group):
        """Key down based reaction"""
        if (key == K_RIGHT):
            self.xMove += self.x_dist
        elif (key == K_LEFT):
            self.xMove += -self.x_dist
        elif (key == K_UP):
            if pygame.sprite.spritecollide(self,block_group,False):
                self.yMove += -self.y_dist
        elif (key == K_DOWN):
            if pygame.sprite.spritecollide(self,block_group,False):
                self.yMove += self.y_dist
    def MoveKeyUp(self,key,block_group):
        """KEy up event based reaction"""
        if (key == K_RIGHT):
            self.xMove += -self.x_dist
        elif (key == K_LEFT):
            self.xMove += self.x_dist
        elif (key == K_UP):
            if pygame.sprite.spritecollide(self,block_group,False):
                self.yMove += self.y_dist
        elif (key == K_DOWN):
            if pygame.sprite.spritecollide(self,block_group,False):
                self.yMove += -self.y_dist
    def update(self,block_group1,block_group2,fireball_group,queen_group):
        """Update position of player and check for collisions with ladder platform,fireball,princess"""
                
        self.rect.move_ip(self.xMove,self.yMove)
        if pygame.sprite.spritecollide(self,queen_group,False): 
            pygame.event.post(pygame.event.Event(WIN,{}))
        if pygame.sprite.spritecollide(self,block_group1,False) and not pygame.sprite.spritecollide(self,block_group2,False):
            self.rect.move_ip(-self.xMove,-self.yMove)
        if not pygame.sprite.spritecollide(self,block_group2,False): #    self.rect.move_ip(-self.xMove,0)
            self.rect.move_ip(0,-self.yMove)
        lst_fireball=pygame.sprite.spritecollide(self,fireball_group,True)
        if len((lst_fireball))>0:
            self.fireballcollide(lst_fireball)
    def fireballcollide(self,fireball_group):
        """The fireball collision check.if collision return no of lives-1.if lives =0 then game over"""
        if len(fireball_group)<=0:
            return
        else:
            if self.lives<=0:
                pygame.event.post(pygame.event.Event(DEAD,{}))
            else:
                self.lives-=1
                time.sleep(3)
