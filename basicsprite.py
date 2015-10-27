import pygame
from helper import *
"""this is the basic sprite inheriting from pygame Sprite model.inherits the pygame Sprite adding the image and position of the image mapping to the 2-d matrix"""
class sprite(pygame.sprite.Sprite):
    def __init__(self,centerPoint,image):
        pygame.sprite.Sprite.__init__(self)
        self.image=image
        self.rect=image.get_rect()
        self.rect.center=centerPoint
        """the coin class.the coins are 
        randomly generated and worth points"""
class coin(pygame.sprite.Sprite):
    def __init__(self,top_left,image=None):
        pygame.sprite.Sprite.__init__(self)
        if image == None:
            self.image,self.rect=load_image('coin.png',-1)
        else:
            self.image=image
            self.rect=image.get_rect()
        self.rect.topleft=top_left
        """the queen character or rather the princess"""
class Queen(pygame.sprite.Sprite):
    def __init__(self,top_left,image=None):
        pygame.sprite.Sprite.__init__(self)
        self.image=image
        self.rect=image.get_rect()
        self.rect.topleft=top_left
