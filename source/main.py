
import pyglet
from pyglet.window import key
from pyglet.window import mouse

from savemanager import SaveManager
from configmanager import ConfigManager
import logging
logging.basicConfig(level=logging.DEBUG)
import os

if not os.path.exists("resources\\config.json"):
    ConfigManager.createdefaultconfig()
else:
    logging.debug("Config already exists")
    ConfigManager.loadexistingconfig()


import random
from position import Position
from chunkmanager import ChunkManager
from statemanager import state_dict
from scoremanager import ScoreManager

import random
seed = random.random()*random.randint(1,99999999999999)
print("seed is %s", seed)
random.seed(seed)

resources_folder = "resources/"

logging.critical("Booting...")

windowsize = ConfigManager.config_dict.get("window_size")

#fps_display = pyglet.clock.ClockDisplay()
window = pyglet.window.Window(width=windowsize[0],height=windowsize[1])

chunk_dict = ChunkManager.chunk_dict


offset = [0,0]


'''
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
'''
ChunkManager.updategenchunks((0,0), (window.width, window.height))
Screenstate = "MainMenu"

@window.event
def on_draw():
    global offset
    global window
    window.clear()

    if Screenstate == "MineField":
        state_dict[Screenstate].draw(offset, window)
    elif Screenstate == "MainMenu":
        state_dict[Screenstate].draw(offset, window)


@window.event
def on_key_press(symbol, modifiers):
    global Screenstate

    if symbol == key.UP:
        print("Hello world")
    if Screenstate == "MineField":
        if symbol == key.BACKSPACE:
            Screenstate = "MainMenu"
    elif Screenstate == "MainMenu":
        if symbol == key.BACKSPACE:
            Screenstate = "MineField"


@window.event
def on_mouse_release(x, y, button, modifiers):
    global Screenstate

    if Screenstate == "MineField":
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
    elif Screenstate == "MainMenu":

        button = state_dict[Screenstate].getbuttonclicked(mouse_pos=(x,y), window=window)

        if not button:
            pass

        elif button.text == "New game":
            logging.debug("Clicked New game")
            ChunkManager.dump_chunks()
            ScoreManager.clearscore()
            from chunkmanager import seed
            random.seed(seed)
            print("seed is %s", seed)
            ChunkManager.updategenchunks(offset, (window.width, window.height))
            Screenstate = "MineField"

        elif button.text == "Load game":
            logging.debug("Clicked Load game")
            if os.path.isfile('resources\savefile.dat'):
                seed, randomstate = SaveManager.loadpicklejarfromfile()
                random.seed(seed)
                print("seed is %s", seed)
                if randomstate:
                    random.setstate(randomstate)
                Screenstate = "MineField"
            else:
                logging.critical("No savefile found!")

        elif button.text == "Save game":
            logging.debug("Clicked Save game")
            SaveManager.savepicklejartofile()

        elif button.text == "Exit game":
            logging.debug("Clicked Quit game")
            pyglet.app.exit()



@window.event
def on_mouse_scroll(x, y, scroll_x, scroll_y):
    pass

@window.event
def on_mouse_drag(x, y, dx, dy, buttons, modifiers):
    global offset
    if Screenstate == "MineField":
        if buttons == mouse.MIDDLE:
            offset[0] += dx
            offset[1] += dy


logging.critical("Pyglet.run()")

#import cProfile
#cProfile.run('pyglet.app.run()')

def falseupdate(dt):
    pass

pyglet.clock.schedule_interval_soft(falseupdate, 1//1)
pyglet.app.run()



logging.critical("End of main")
