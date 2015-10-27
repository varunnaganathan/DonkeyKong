import os,sys,random,time
from playerSprite import player,DEAD,WIN,BL
import pygame
import level1,level2
from donkey import donkey
import basicsprite
from pygame.locals import *
from helper import *
from fireball import *
"""Description of this file is the running of the game.Details of this can be found in readme.txt"""
BLACK=(0,0,0)
WHITE=(255,255,255)
if not pygame.mixer:
    print"SOUND DISABLED"
if not pygame.font:
    print "FONT NOT AVAILABLE"
clock=pygame.time.Clock()
BLOCK_SIZE=24
gameover = False
newball=WIN+1
class gamemain:
    def __init__(self,width=640,height=480):
        pygame.init()
        self.width=width
        self.gameover=False
        self.height=height
        self.level=1
        self.screen=pygame.display.set_mode((self.width,self.height))
    
    def addball(self):
        if self.level==1:
            level01=level1.level()
        else:
            level01=level2.level()
        layout=level01.getlayout()
        img_list=level01.getsprites()
        x_offset=BLOCK_SIZE/2
        y_offset=BLOCK_SIZE/2
        centerpoint=[(2*BLOCK_SIZE)+x_offset,(3*BLOCK_SIZE)+y_offset]
        ball=fireball(centerpoint,img_list[level01.FIREBALL])
        self.fireball_sprites.add(ball)
    def mainloop(self,level):
        """Main game-loop"""
        self.level=level
        self.LoadSprites()
        self.background=pygame.Surface(self.screen.get_size())
        self.background=self.background.convert()
        self.background.fill(BLACK)
        self.background.fill(WHITE)
        self.wall_sprites.draw(self.background)
        self.coin_sprites.draw(self.background)
        self.fireball_sprites.draw(self.background)
        self.queen_sprites.draw(self.background)
        if self.level==1:
            pygame.time.set_timer(newball,5000)
        else:
            pygame.time.set_timer(newball,3000)
        flag=True
        self.player.j=False
        while 1:
            rectangle=self.player.rect
            rectangle2=self.donkey.rect
            rectangle.clamp_ip(self.screen.get_rect())
            rectangle2.clamp_ip(self.screen.get_rect())
            if self.player.j==False:
                prev=self.player.rect.top
            self.player_sprites.clear(self.screen,self.background)
            self.fireball_sprites.clear(self.screen,self.background)
            while self.gameover == True: 
                """If game is over """
                self.screen.fill(WHITE)
                font=pygame.font.SysFont(None,25)
                text=font.render("GAME OVER!!  Press q to quit",True,(255,0,0))
                textpos=text.get_rect(centerx=self.background.get_width()/2,centery=self.background.get_height()/2)
                self.screen.blit(text,textpos)
                pygame.display.flip()
                """All event based reactions of the game"""
                for event in pygame.event.get():
                    if event.type==pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            gameover=False
                            sys.exit()
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    sys.exit()
                elif event.type==newball:
                    self.addball()
                    self.fireball_sprites.draw(self.background)
                    pygame.display.flip()
                elif event.type==KEYDOWN:
                    if ((event.key == K_RIGHT)
                    or (event.key == K_LEFT)
                    or (event.key == K_UP)
                    or (event.key == K_DOWN)):
                        self.player.MoveKeyDown(event.key,self.ladder_sprites)
                    elif event.key == K_SPACE:
                        if self.player.j==False and flag==True:
                            prev=self.player.rect.top
                        self.player.j=True
                        self.player.yvel=-20
                        """self.player.yMove+= -10
                        self.player.rect.move_ip(self.player.xMove,self.player.yMove)
                        self.player_sprites.draw(self.screen)
                        pygame.display.flip()
                        time.sleep(1)"""

                elif event.type==KEYUP:
                    if ((event.key == K_RIGHT)
                    or (event.key == K_LEFT)
                    or (event.key == K_UP)
                    or (event.key == K_DOWN)):
                        self.player.MoveKeyUp(event.key,self.ladder_sprites)
                    elif event.key==K_SPACE:
                        continue
                        #self.player.rect.move_ip(0,-self.player.yvel)
                        """self.player.yMove+= 10
                        self.player.rect.move_ip(self.player.xMove,self.player.yMove)
                        self.player_sprites.draw(self.screen)
                        pygame.display.flip()"""
                if event.type == DEAD:
                    """self.screen.fill(WHITE)
                    font=pygame.font.SysFont(None,36)
                    text=font.render("GAME OVER!!  Press q to quit",True,(255,0,0))
                    textpos=text.get_rect(centerx=self.background.get_width()/2,centery=self.background.get_height()/2)"""
                    self.gameover=True
                if event.type==WIN:    
                    self.screen.fill(WHITE)
                    font=pygame.font.SysFont(None,25)
                    if self.level==1:
                        text=font.render("CONGRATS!!Press q to quit..PRESS l for next level",True,(255,0,0))
                    else:
                        text=font.render("YOU HAVE WON THE GAME!!  Press q to quit!!",True,(255,0,0))
                    textpos=text.get_rect(centerx=self.background.get_width()/2,centery=self.background.get_height()/2)
                    self.screen.blit(text,textpos)
                    pygame.display.flip()
                    time.sleep(3)
                    if self.level>=2:
                        self.gameover=True
                    else:
                        for event1 in pygame.event.get():
                            print event1
                            if event1.type==pygame.KEYDOWN:
                                if event1.key == pygame.K_q:
                                    self.gameover=True
                                elif event1.key==pygame.K_l:
                                    self.mainloop(2)
                    #sys.exit()
            """if self.player.yMove==prev:
                print "TRUE"
            else:"""
            if (self.player.j==True):
                if self.player.rect.top<=prev:
                    #self.player.yMove+=self.player.yvel
                    self.player.yvel+=self.player.g
                    self.player.rect.move_ip(1,self.player.yvel)
                    self.player_sprites.draw(self.screen)
                    pygame.display.flip()
                else:
                    self.player.j=False
                    flag=False
                    self.player.yMove=0
                    self.player.rect.move_ip(self.player.xMove,-self.player.yvel)
                    self.player_sprites.draw(self.screen)
                    pygame.display.flip()

            
#            print self.player.rect.top
            num=random.randrange(0,100)
            self.donkey.move(num%2)
            self.donkey_sprites.update(self.wall_sprites)
            self.player_sprites.update(self.wall_sprites,self.ladder_sprites,self.fireball_sprites,self.queen_sprites)
            self.fireball_sprites.update(self.wall_sprites,self.ladder_sprites)
            cols=pygame.sprite.spritecollide(self.player,self.coin_sprites,True)
            self.player.points+=(5*(len(cols)))
            self.screen.blit(self.background,(0,0))
            self.background.fill(BLACK)
            self.background.fill(WHITE)
            self.wall_sprites.draw(self.background)
            self.coin_sprites.draw(self.background)
            self.queen_sprites.draw(self.background)
            if pygame.font:
                font=pygame.font.Font(None,25)
                text=font.render("points %s"% self.player.points,1,(255,0,0))
                text2=font.render("LIVES %s"% self.player.lives,1,(255,0,0))
                text3=font.render("LEVEL %s"% self.level,1,(255,0,0))
                textpos=text.get_rect(centerx=self.background.get_width()/2)
                textpos2=text.get_rect(centerx=self.background.get_width()/2+100)
                textpos3=text.get_rect(centerx=self.background.get_width()/2+200)
                self.screen.blit(text,textpos)
                self.screen.blit(text2,textpos2)
                self.screen.blit(text3,textpos3)
            self.coin_sprites.draw(self.screen)
            self.ladder_sprites.draw(self.screen)
            self.wall_sprites.draw(self.background)
            self.donkey_sprites.draw(self.screen)
            self.player_sprites.draw(self.screen)
            self.fireball_sprites.draw(self.screen)
            self.queen_sprites.draw(self.screen)
#            print self.donkey.xmove
            pygame.display.flip()
            if self.level==1:
                clock.tick(10)
            else:
                clock.tick(20)
    def LoadSprites(self):
        x_offset=BLOCK_SIZE/2
        y_offset=BLOCK_SIZE/2
        if self.level==1:
            level01=level1.level()
        else:
            level01=level2.level()
        layout=level01.getlayout()
        img_list=level01.getsprites()
        self.coin_sprites=pygame.sprite.RenderUpdates()
        self.queen_sprites=pygame.sprite.RenderUpdates()
        self.wall_sprites=pygame.sprite.RenderUpdates()
        self.ladder_sprites=pygame.sprite.RenderUpdates()
        self.fireball_sprites=pygame.sprite.RenderUpdates()
        for y in xrange(len(layout)):
            """Select the layout based on 2-d matrix in the level file"""
            for x in xrange(len(layout[y])):
                centerpoint=[(x*BLOCK_SIZE)+x_offset,(y*BLOCK_SIZE)+y_offset]
                if layout[y][x]==level01.WALL:
                    wall=basicsprite.sprite(centerpoint,img_list[level01.WALL])
                    self.wall_sprites.add(wall)
                elif layout[y][x]==level01.PLAYER:
                    self.player=player(centerpoint,img_list[level01.PLAYER])
                elif layout[y][x]==level01.COIN:
                    coin=basicsprite.sprite(centerpoint,img_list[level01.COIN])
                    self.coin_sprites.add(coin)
                elif layout[y][x]==level01.LADDER:
                    ladder=basicsprite.sprite(centerpoint,img_list[level01.LADDER])
                    self.ladder_sprites.add(ladder)
                elif layout[y][x]==level01.DONKEY:
                    self.donkey=donkey(centerpoint,img_list[level01.DONKEY])
                elif layout[y][x]==level01.FIREBALL:
                    ball=fireball(centerpoint,img_list[level01.FIREBALL])
                    self.fireball_sprites.add(ball)
                elif layout[y][x]==level01.QUEEN:
                    queen=basicsprite.sprite(centerpoint,img_list[level01.QUEEN])
                    self.queen_sprites.add(queen)
        self.player_sprites=pygame.sprite.RenderUpdates((self.player))
        self.donkey_sprites=pygame.sprite.RenderPlain((self.donkey))
MainWindow=gamemain(500,575)
MainWindow.mainloop(1)
"""if __name__=="__main__":
    MainWindow=gamemain(500,575)
    MainWindow.mainloop()"""
