

from tile import Tile

from random import random


import logging
logging.basicConfig(level=logging.WARNING)

class Chunk:
    def __init__(self, pos:tuple, chunkmanager, batch):
        self.chunkmanager = chunkmanager
        self.pos = pos[0]*16*21,pos[1]*16*21 #self.pos is in pixels, pos is in chunks!!!
        self._chunk = [None]*16
        for i in range(0,16):
            self._chunk[i] = [None]*16

        #generate the data structure
        for x in range(0,16):
            for y in range(0,16):
                self._chunk[x][y] = Tile(batch, pos=(x*21*pos[0],y*21*pos[1]))

        #populate the data structure with mines
        for x in range(0,16):
            for y in range(0,16):
                isMine = False
                if random() > 0.90:
                    isMine = True
                self._chunk[x][y].isMine = isMine

        #populate non-mines with proximity
        '''
        offsets = [(-1,-1),(0,-1),(1,-1),
                   (-1,0),        (1,0),   #doesn't contain (0,0) because this is self
                   (-1,1), (0,1), (1,1)]

        for x in range(0,15):
            for y in range(0,15):
                count = 0
                for offset in offsets:
                    if 0 < x+offset[0] < len(self._chunk) and\
                            0 < y+offset[1] < len(self._chunk[x]):
                        if self._chunk[x+offset[0]][y+offset[1]].isMine:
                            count+=1
                self._chunk[x][y].proximity = count
        '''

    def __repr__(self):
        temp = ""
        for x in self._chunk:
            temp += str(x)+"\n"
        return temp

    def draw(self, offset:tuple):
        for y in self._chunk:
            for tile in y:
                tile.draw((offset[0]+self.pos[0],
                           offset[1]+self.pos[1]))

    def updatesprites(self, pos:tuple):
        for x in range(0,16):
            for y in range(0,16):
                self._chunk[x][y].updatepos( (x*21+pos[0], y*21+pos[1]) )

    def gettile(self, pos):
        return self._chunk[pos[0]][pos[1]]


    def flagtile(self, tilepos:tuple):
        self.gettile(tilepos).flag()

    def activatetile(self, tilepos:tuple):

        tile = self.gettile(tilepos)

        if tile.isHidden and not tile.isFlagged:
            if tile.isMine:
                tile.reveal()
            else:
                neightiles = self.chunkmanager.getneighbouringtiles(poschunk=self.pos, postile=tilepos)
                mines = self.getmines( neightiles )
                tile.reveal(prox=mines)
                if mines == 0:
                    #WARNING: RECURSIVE!
                    for tile in neightiles:
                        pass
                        #self.activatetile_recursive(tile=tile)

    def activatetile_recursive(self, tile:Tile):
        tilepos = tile.pos

        if tile.isHidden and not tile.isFlagged:
            if tile.isMine:
                tile.reveal()
            else:
                neightiles = self.chunkmanager.getneighbouringtiles(poschunk=self.pos, postile=tilepos)
                mines = self.getmines( neightiles )
                tile.reveal(prox=mines)
                if mines == 0:
                    #WARNING: RECURSIVE!
                    for tile in neightiles:
                        pass
                        #self.activatetile_recursive(tile)

    @staticmethod
    def getmines(tiles:list) ->int:
        count = 0
        for tile in tiles:
            if tile.isMine:
                count+=1
        return count