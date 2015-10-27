import baselevel,random
from helper import load_image
"""The basic level layout for level-1"""
"""returs the layout and the set of images used based on indexing"""
class level(baselevel.level):
    def __init__(self):
        self.WALL=1
        self.PLAIN=9
        self.PLAYER=2
        self.COIN=0
        self.LADDER=3
        self.DONKEY=4
        self.FIREBALL=5
        self.QUEEN=6
    def getlayout(self):
        a=     [[1, 1, 1, 1, 3, 6, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9],\
                [9, 9, 9, 9, 3, 9, 9, 9, 9, 9, 9 ,9, 9, 9, 9, 9, 9, 9, 9, 9, 9],\
                [4, 9, 9, 9, 3, 9, 9, 9, 9, 9, 9 ,9, 9, 9, 9, 9, 9, 9, 9, 9, 9],\
                [9, 1, 1, 1, 3, 1, 3, 1, 1, 3, 1 ,1, 1, 3, 1, 9, 9, 9, 9, 9, 9],\
                [9, 9, 9, 9, 9, 9, 3, 9, 9, 9, 9 ,9, 9, 3, 9, 9, 9, 9, 9, 9, 9],\
                [9, 9, 9, 9, 9, 9, 3, 9, 9, 9, 9, 9, 9, 3, 9, 9, 9, 9, 9, 9, 9],\
                [9, 9, 9, 9, 9, 9, 3, 9, 9, 9, 9, 9, 9, 3, 9, 9, 9, 9, 9, 9, 9],\
                [9, 9, 9, 9, 9, 9, 3, 1, 1, 3, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 9],\
                [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 3, 9, 9, 9, 9, 9, 9],\
                [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 3, 9, 9, 9, 9, 9, 9],\
                [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 3, 9, 9, 9, 9, 9, 9],\
                [9, 1, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 3, 1, 3, 9, 9, 9, 9, 9, 9],\
                [9, 9, 9, 9, 9, 9, 3, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],\
                [9, 9, 9, 9, 9, 9, 3, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],\
                [1, 9, 9, 9, 9, 9, 3, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],\
                [1, 9, 9, 9, 9, 9, 1, 1, 1, 1, 3, 1, 3, 1, 3, 1, 1, 1, 1, 1, 9],\
                [1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 3, 9, 9, 9, 3, 9, 9, 9, 9, 9, 9],\
                [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 3, 9, 9, 9, 3, 9, 9, 9, 9, 9, 9],\
                [2, 9, 9, 9, 9, 9, 9, 9, 9, 9, 3, 9, 9, 9, 3, 9, 9, 9, 9, 9, 9],\
                [9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9, 9, 9, 9, 9, 9],\
                [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],\
                [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],\
                [9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
        
        for i in range(1,6):
            for j in range(0,5):
                if i %2:
                    num=random.randrange(0,15)
                    if a[4*i-2][num]==9:
                        a[4*i-2][num]=0
                else:
                    num=random.randrange(6,21)
                    if a[4*i-2][num]==9:
                        a[4*i-2][num]=0
        return a


    def getsprites(self):
        wall,rect=load_image('wall2.png')
        coin,rect=load_image('coin2.png',-1)
        player,rect=load_image('player2.png',-1)
        ladder,rect=load_image('ladder.png',-1)
        donkey,rect=load_image('donkey.png',-1)
        fireball,rect=load_image('fireball.png',-1)
        queen,rect=load_image('princess.png',-1)
        #plain,rect=load_image('plain.png',-1)
        return [coin,wall,player,ladder,donkey,fireball,queen]

