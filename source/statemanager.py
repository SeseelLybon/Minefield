

from enum import Enum
from enum import auto
import pyglet

from chunkmanager import ChunkManager
from scoremanager import ScoreManager
from configmanager import ConfigManager


class MineField:
    window_size = ConfigManager.config_dict.get("window_size")
    score_label = pyglet.text.Label('score: ' + str(0),
                                        font_name='Times New Roman',
                                        font_size=12,
                                        x=50, y=window_size[1] - 50,
                                        anchor_x='left', anchor_y='center')
    clearedtiles_label = pyglet.text.Label('Tiles cleared: ' + str(0),
                                       font_name='Times New Roman',
                                       font_size=12,
                                       x=50, y=window_size[1] - 75,
                                       anchor_x='left', anchor_y='center')

    @classmethod
    def draw(cls, offset, window):
        cls.score_label.text = 'score: ' + str(ScoreManager.getscore())
        cls.clearedtiles_label.text = 'Tiles cleared: ' + str(ScoreManager.getclearedtiles())

        ChunkManager.screenspaceocclude_drawchunks(offset, (window.width, window.height))
        ChunkManager.updategenchunks(offset, (window.width, window.height))

        cls.score_label.draw()
        cls.clearedtiles_label.draw()

class MainMenu:
    window_size = ConfigManager.config_dict.get("window_size")

    button_New_label = pyglet.text.Label("New game",
                            font_name='Times New Roman',
                            font_size=20,
                            x=window_size[0]//2, y=window_size[1] - 200,
                            anchor_x='center', anchor_y='center')

    button_Load_label = pyglet.text.Label("Load existing game",
                            font_name='Times New Roman',
                            font_size=20,
                            x=window_size[0]//2, y=window_size[1] - 250,
                            anchor_x='center', anchor_y='center')

    button_Exit_label = pyglet.text.Label("Exit game",
                            font_name='Times New Roman',
                            font_size=20,
                            x=window_size[0]//2, y=window_size[1] - 300,
                            anchor_x='center', anchor_y='center')

    @classmethod
    def draw(cls, offset, window):
        cls.button_New_label.draw()
        cls.button_Load_label.draw()
        cls.button_Exit_label.draw()


    @classmethod
    def getbuttonclicked(cls, mouse_pos, window):
        print("x Expect", cls.button_New_label.x, cls.button_New_label.x+110, "Got", mouse_pos[0])
        print("y Expect", cls.button_New_label.y-50, cls.button_New_label.y, "Got", mouse_pos[1])

        if cls.button_New_label.x-50 < mouse_pos[0] < cls.button_New_label.x+60:
            if cls.button_New_label.y-15 < mouse_pos[1] < cls.button_New_label.y+15:
                print("New game clicked"+str(mouse_pos))

state_dict = {"MineField":MineField,
              "MainMenu":MainMenu}