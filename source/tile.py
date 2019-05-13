


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
        self.proximity = 0 #indicates that proximity has not yet been updated, looks save, might break
        self.isHidden = True
        self.isFlagged = False
        self.isMine = isMine
        self.isDestroyed = False
        self.sprite = pyglet.sprite.Sprite(image_hidden, x=pos[0], y=pos[1],
                                       batch=batch )
        if tilehash:
            self.altinit(tilehash)

    def altinit(self, tilehash):

        prox = tilehash[0]
        self.isHidden = tilehash[1]
        self.isFlagged = tilehash[2]
        self.isMine = tilehash[3]
        self.isDestroyed = tilehash[4]

        if not self.isHidden:
            if self.isMine or self.isDestroyed:
                self.triggermine()
            else:
                self.reveal(prox=prox)
        if self.isFlagged:
            self.isFlagged = False
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
        if self.isHidden:
            ScoreManager.tilecleared()

        if self.isMine:
            self.sprite.image = image_mine_hit
            self.isHidden = False
            self.isFlagged = False
            ScoreManager.hitmine()
        else:
            self.sprite.image = image_tile_destroyed
            self.isHidden = False
            self.isFlagged = False
            self.isDestroyed = True
            ScoreManager.losttile()



    def reveal(self,prox:int=0):
        self.sprite.image = images_prox[prox]
        self.proximity = prox
        self.isHidden = False
        ScoreManager.nomine()
        ScoreManager.tilecleared()

    def updatepos(self, pos:tuple):
        self.sprite.update(x=pos[0],y=pos[1])

if __name__ == "__main__":
    import sys
    print("A single tile is", sys.getsizeof(Tile(None,(0,0),False)), "bytes")