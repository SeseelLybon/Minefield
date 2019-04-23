

from enum import Enum
from enum import auto


class ScreenStates(Enum):
    MainScreen = auto()
    MineField = auto()


class StateManager:
    Screenstate = ScreenStates.MineField