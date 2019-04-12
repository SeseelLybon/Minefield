
import pyglet
from pyglet.window import key
from pyglet.window import mouse

import logging
logging.basicConfig(level=logging.DEBUG)

from position import Position

from chunkmanager import ChunkManager
from scoremanager import ScoreManager

resources_folder = "resources/"

logging.critical("Booting...")
logging.info("Root... %s", __file__ )

#fps_display = pyglet.clock.ClockDisplay()
window = pyglet.window.Window()

score = 0
label = pyglet.text.Label('score: '+str(score),
                        font_name='Times New Roman',
                        font_size=12,
                        x=50, y=window.height-50,
                        anchor_x='left', anchor_y='center')

chunk_dict = ChunkManager.chunk_dict



offset = [0,0]

@window.event
def on_draw():
    global offset
    global window
    window.clear()
    label.text = 'score: '+str(ScoreManager.getscore())
    ChunkManager.updatesprites(offset)

    #TODO: ambiant occlusion to tiles
    ChunkManager.screenspaceocclude_drawchunks(offset, (window.width, window.height))

    #Check per chunk if its tiles have to be drawn - easier than asking every tile
    #for chunk in chunk_dict.values():
    #    chunk.draw()


    label.draw()
    #fps_display.draw()
    ChunkManager.updategenchunks(offset, (window.width, window.height))

@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.UP:
        print("Hello world")


@window.event
def on_mouse_release(x, y, button, modifiers):
    global offset

    x = x-offset[0]
    y = y-offset[1]

    tilepos = Position.pixtotile((x,y))
    chunkpos = Position.pixtochunk((x,y))

    if button == mouse.LEFT:
        logging.debug('Clicked at (%d, %d), %s, %s, %s', x, y, chunkpos, tilepos, offset)
        #print('Clicked at', x, y, chunkpos, tilepos)
        chunk = chunk_dict.get(chunkpos, None)
        if chunk:
            chunk.activatetile(tilepos=tilepos)
    if button == mouse.RIGHT:
        logging.debug('Clicked at (%d, %d), %s, %s, %s', x, y, chunkpos, tilepos, offset)
        #print('Clicked at', x, y, chunkpos, tilepos)
        chunk = chunk_dict.get(chunkpos, None)
        if chunk:
            chunk.flagtile(tilepos)


@window.event
def on_mouse_scroll(x, y, scroll_x, scroll_y):
    pass

@window.event
def on_mouse_drag(x, y, dx, dy, buttons, modifiers):
    global offset
    if buttons == mouse.MIDDLE:
        offset[0] += dx
        offset[1] += dy


logging.critical("Pyglet.run()")
pyglet.app.run()

logging.critical("End of main")
