


import pyglet
from scoremanager import ScoreManager

resources_folder = "resources/"
images_prox = [pyglet.resource.image(resources_folder + 'prox_0.png'),
               pyglet.resource.image(resources_folder + 'prox_1.png'),
               pyglet.resource.image(resources_folder + 'prox_2.png'),
               pyglet.resource.image(resources_folder + 'prox_3.png'),
               pyglet.resource.image(resources_folder + 'prox_4.png'),
               pyglet.resource.image(resources_folder + 'prox_5.png'),
               pyglet.resource.image(resources_folder + 'prox_6.png'),
               pyglet.resource.image(resources_folder + 'prox_7.png'),
               pyglet.resource.image(resources_folder + 'prox_8.png')
               ]

image_hidden = pyglet.resource.image(resources_folder + 'hidden.png')

image_mine = pyglet.resource.image(resources_folder + 'mine.png')
image_mine_hit = pyglet.resource.image(resources_folder + 'mine_hit.png')
image_tile_destroyed = pyglet.resource.image(resources_folder + 'destroyed.png')
image_flagged = pyglet.resource.image(resources_folder + 'flagged.png')




class Tile:





    def __init__(self, batch, pos:tuple, isMine=False, tilehash=None):
        self.pos = pos
        self.proximity = 0
        self.isHidden = True
        self.isFlagged = False
        self.isMine = isMine
        self.isDestroyed = False
        self.sprite = pyglet.sprite.Sprite(image_hidden, x=pos[0], y=pos[1],
                                       batch=batch )
        if tilehash:
            self.altinit(tilehash)

    def altinit(self, tilehash):

        prox = tilehash%10

        if tilehash//10 % 10 == 0:
            self.isHidden = True
        if tilehash//100 % 10 == 0:
            self.isFlagged = True
        if tilehash//1000 % 10 == 0:
            self.isMine = True
        if tilehash//10000 % 10 == 0:
            self.isDestroyed = True

        if not self.isHidden:
            if self.isMine:
                self.triggermine()
            else:
                self.reveal(prox=prox)
        elif self.isFlagged:
            self.flag()

    def __repr__(self):
        if self.isMine:
            return "X"
        else:
            if self.proximity == 0:
                return " "
            else:
                return str(self.proximity)

    def flag(self):
        if self.isHidden and not self.isFlagged:
            self.sprite.image = image_flagged
            self.isFlagged = True
        elif self.isHidden and self.isFlagged:
            self.sprite.image = image_hidden
            self.isFlagged = False

    def triggermine(self):
        if self.isMine:
            self.sprite.image = image_mine_hit
            self.isHidden = False
            ScoreManager.hitmine()
        else:
            self.sprite.image = image_tile_destroyed
            self.isHidden = False
            self.isDestroyed = True
            ScoreManager.losttile()



    def reveal(self,prox:int=0):
        self.sprite.image = images_prox[prox]
        self.proximity = prox
        self.isHidden = False
        ScoreManager.nomine()

    def updatepos(self, pos:tuple):
        self.sprite.update(x=pos[0],y=pos[1])