


class Tile:

    def __init__(self, isMine = False):
        self.isMine = isMine
        self.proximity = 0
        self.isVisible = False

    def __repr__(self):
        if self.isMine:
            return "isMine"
        else:
            return str(self.proximity)