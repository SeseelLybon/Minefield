


import pyglet


class Tile:

    resources_folder = "resources/"
    image_prox_0 = pyglet.resource.image(resources_folder+'prox_0.png')
    image_prox_1 = pyglet.resource.image(resources_folder+'prox_1.png')
    image_prox_2 = pyglet.resource.image(resources_folder+'prox_2.png')
    image_prox_3 = pyglet.resource.image(resources_folder+'prox_3.png')
    image_prox_4 = pyglet.resource.image(resources_folder+'prox_00.png')
    image_prox_5 = pyglet.resource.image(resources_folder+'prox_00.png')
    image_prox_6 = pyglet.resource.image(resources_folder+'prox_00.png')
    image_prox_7 = pyglet.resource.image(resources_folder+'prox_00.png')
    image_prox_8 = pyglet.resource.image(resources_folder+'prox_00.png')

    image_hidden = pyglet.resource.image(resources_folder+'hidden.png')

    image_mine = pyglet.resource.image(resources_folder+'mine.png')
    image_mine_hit = pyglet.resource.image(resources_folder+'mine_hit.png')
    image_flagged = pyglet.resource.image(resources_folder+'flagged.png')



    def __init__(self, pos:tuple, isMine=False):
        self.pos = pos
        self.isMine = isMine
        self.proximity = 0
        self.isVisible = False
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