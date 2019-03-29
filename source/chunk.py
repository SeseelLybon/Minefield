

from tile import Tile

from random import random

import logging
logging.basicConfig(level=logging.DEBUG)

class Chunk:
    def __init__(self, pos:tuple):
        self.pos = pos[0]*16*21,pos[1]*16*21
        self._chunk = [None]*16
        for i in range(0,16):
            self._chunk[i] = [None]*16

        #generate the data structure
        for x in range(0,16):
            for y in range(0,16):
                self._chunk[x][y] = Tile(pos=(x*21,y*21))

        #populate the data structure with mines
        for x in range(0,16):
            for y in range(0,16):
                isMine = False
                if random() > 0.80:
                    isMine = True
                self._chunk[x][y].isMine = isMine

        #populate non-mines with proximity

        offsets = [(-1,-1),(0,-1),(1,-1),
                   (-1,0),(1,0),   #doesn't contain (0,0) because this is self
                   (-1,1),(0,1),(1,1)]

        for x in range(0,16):
            for y in range(0,16):
                count = 0
                for offset in offsets:
                    try:
                        if self._chunk[x+offset[0]][y+offset[1]].isMine:
                            count+=1
                    except IndexError:
                        pass
                self._chunk[x][y].proximity = count


    def __repr__(self):
        temp = ""
        for x in self._chunk:
            temp += str(x)+"\n"
        return temp

    def draw(self, offset:tuple):
        for y in self._chunk:
            for tile in y:
                tile.draw(offset+self.pos)