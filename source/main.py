
import pyglet
from pyglet.window import key
from pyglet.window import mouse

import logging
logging.basicConfig(level=logging.DEBUG)
import random
from position import Position
import os
from chunkmanager import ChunkManager
from scoremanager import ScoreManager
from savemanager import SaveManager
from configmanager import ConfigManager
from statemanager import ScreenStates
from statemanager import StateManager

resources_folder = "resources/"

logging.critical("Booting...")
logging.info("Root... %s", __file__ )

if not os.path.exists("resources\\config.json"):
    ConfigManager.createdefaultconfig()
else:
    logging.debug("Config already exists")
    ConfigManager.loadexistingconfig()

windowsize = ConfigManager.config_dict.get("window_size")

#fps_display = pyglet.clock.ClockDisplay()
window = pyglet.window.Window(width=windowsize[0],height=windowsize[1])

score_label = pyglet.text.Label('score: ' + str(0),
                                font_name='Times New Roman',
                                font_size=12,
                                x=50, y=window.height-50,
                                anchor_x='left', anchor_y='center')

clearedtiles_label = pyglet.text.Label('Tiles cleared: '+str(0),
                        font_name='Times New Roman',
                        font_size=12,
                        x=50, y=window.height-75,
                        anchor_x='left', anchor_y='center')

chunk_dict = ChunkManager.chunk_dict


offset = [0,0]

#generate a 'spawn area'
gen_static_starting_area = False# If true; generate a static area, if False the area on the screen)
if gen_static_starting_area:
    for x in range(-6,8):
        for y in range(-6, 8):
            ChunkManager.registerchunk((x,y))
else:
    if os.path.isfile('resources\savefile.dat'):
        seed, randomstate = SaveManager.loadpicklejarfromfile()
        random.seed(seed)
        print("seed is %s", seed)
        if randomstate:
            random.setstate(randomstate)
    else:
        from chunkmanager import seed
        random.seed(seed)
        print("seed is %s", seed)
        ChunkManager.updategenchunks(offset, (window.width, window.height))

@window.event
def on_draw():
    global offset
    global window
    window.clear()

    if StateManager.Screenstate == ScreenStates.MineField
        score_label.text = 'score: ' + str(ScoreManager.getscore())
        clearedtiles_label.text = 'Tiles cleared: ' + str(ScoreManager.getclearedtiles())


        #ChunkManager.updatesprites(offset)

        #Screenspace occlusion of the chunks
        ChunkManager.screenspaceocclude_drawchunks(offset, (window.width, window.height))


        score_label.draw()
        clearedtiles_label.draw()
        #fps_display.draw()
        ChunkManager.updategenchunks(offset, (window.width, window.height))
    elif StateManager.Screenstate == ScreenStates.MainScreen:
        logging.critical("Screenstate MainScreen is empty!!!")

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

#import cProfile
#cProfile.run('pyglet.app.run()')

pyglet.app.run()

logging.info("Saving map to file")

SaveManager.savepicklejartofile()

logging.critical("End of main")
