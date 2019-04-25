
import pyglet
#import logging



image_hidden = pyglet.resource.image("resources/button.png")

class Button:
    def __init__(self, text:str, pos:tuple):
        self.text = text
        self.position = pos
        self.label = pyglet.text.Label(text,
                        font_name='Times New Roman',
                        font_size=21,
                        x=pos[0], y=pos[1],
                        anchor_x='center', anchor_y='center')
        self.sprite = pyglet.sprite.Sprite(image_hidden, x=pos[0]-85, y=pos[1]-22)
        self.sprite.scale_x = 1.7
        self.sprite.scale_y = 2

    def draw(self, offset, window):
        self.sprite.draw()
        self.label.draw()

    def getcollision(self, pos:tuple):
        if self.sprite.x-4 < pos[0] < self.sprite.x+170:
            if self.sprite.y < pos[1] < self.sprite.y+40:
                return True
        return False