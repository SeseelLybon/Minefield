


import pyglet


class Tile:

    resources_folder = "resources/"
    images_prox = [pyglet.resource.image(resources_folder+'prox_0.png'),
                   pyglet.resource.image(resources_folder+'prox_1.png'),
                   pyglet.resource.image(resources_folder+'prox_2.png'),
                   pyglet.resource.image(resources_folder+'prox_3.png'),
                   pyglet.resource.image(resources_folder+'prox_00.png'),
                   pyglet.resource.image(resources_folder+'prox_00.png'),
                   pyglet.resource.image(resources_folder+'prox_00.png'),
                   pyglet.resource.image(resources_folder+'prox_00.png'),
                   pyglet.resource.image(resources_folder+'prox_00.png'),
                   pyglet.resource.image(resources_folder+'prox_00.png')]

    image_hidden = pyglet.resource.image(resources_folder+'hidden.png')

    image_mine = pyglet.resource.image(resources_folder+'mine.png')
    image_mine_hit = pyglet.resource.image(resources_folder+'mine_hit.png')
    image_flagged = pyglet.resource.image(resources_folder+'flagged.png')



    def __init__(self, pos:tuple, isMine=False):
        self.pos = pos
        self.isMine = isMine
        self.proximity = 0
        self.isHidden = True
        self.isFlagged = False
        self.sprite = pyglet.sprite.Sprite(self.image_hidden, x=pos[0], y=pos[1] )

    def __repr__(self):
        if self.isMine:
            return "X"
        else:
            if self.proximity == 0:
                return " "
            else:
                return str(self.proximity)

    def draw(self, offset:tuple):
        self.sprite.update(x=self.pos[0]+offset[0],y=self.pos[1]+offset[1])
        self.sprite.draw()
        pass

    def flag(self):
        if self.isHidden and not self.isFlagged:
            self.sprite.image = self.image_flagged
            self.isFlagged = True
        elif self.isHidden and self.isFlagged:
            self.sprite.image = self.image_hidden
            self.isFlagged = False

    def reveal(self,prox:int=0):
        if self.isMine:
            self.sprite.image = self.image_mine_hit
            self.isHidden = False
        else:
            self.sprite.image = self.images_prox[prox]
            self.isHidden = False
