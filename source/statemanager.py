

from enum import Enum
from enum import auto
import pyglet

from button import Button

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

    buttons_dict = {"button_New":  Button("New game", pos=(window_size[0]//2, window_size[1]-150)),
                    "button_Load": Button("Load game", pos=(window_size[0]//2, window_size[1]-200)),
                    "button_Save": Button("Save game", pos=(window_size[0]//2, window_size[1]-250)),
                    "button_Exit": Button("Exit game", pos=(window_size[0]//2, window_size[1]-300))}

    @classmethod
    def draw(cls, offset, window):
        ChunkManager.screenspaceocclude_drawchunks(offset, (window.width, window.height))
        for button in cls.buttons_dict.values():
            button.draw(offset, window)


    @classmethod
    def getbuttonclicked(cls, mouse_pos, window):
        #TODO: rewrite to ask button for collision

        for button in cls.buttons_dict.values():
            if button.getcollision(mouse_pos):
                return button
        return None

class OptionsMenu:
    window_size = ConfigManager.config_dict.get("window_size")

    buttons_dict = {"button_New":  Button("New game", pos=(window_size[0]//2, window_size[1]-150)),
                    "button_Load": Button("Load game", pos=(window_size[0]//2, window_size[1]-200)),
                    "button_Save": Button("Save game", pos=(window_size[0]//2, window_size[1]-250)),
                    "button_Exit": Button("Exit game", pos=(window_size[0]//2, window_size[1]-300))}

    @classmethod
    def draw(cls, offset, window):
        ChunkManager.screenspaceocclude_drawchunks(offset, (window.width, window.height))
        for button in cls.buttons_dict.values():
            button.draw(offset, window)


    @classmethod
    def getbuttonclicked(cls, mouse_pos, window):
        #TODO: rewrite to ask button for collision

        for button in cls.buttons_dict.values():
            if button.getcollision(mouse_pos):
                return button
        return None

state_dict = {"MineField":MineField,
              "MainMenu":MainMenu,
              "OptionsMenu":OptionsMenu}