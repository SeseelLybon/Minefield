

from tile import Tile

import random
#random.seed(50)

import pyglet

import logging

class Chunk:
    def __init__(self, pos:tuple, chunkmanager):
        self.batch = pyglet.graphics.Batch()
        self.chunkmanager = chunkmanager
        self.pos = pos[0]*16*21,pos[1]*16*21 #self.pos is in pixels, pos is in chunks!!!
        self._chunk = [None]*16
        for i in range(0,16):
            self._chunk[i] = [None]*16

        #generate the data structure
        for x in range(0,16):
            for y in range(0,16):
                self._chunk[x][y] = Tile(self.batch, pos=(x,y))

        #populate the data structure with mines
        for x in range(0,16):
            for y in range(0,16):
                isMine = False
                if random.random() > 0.83:
                    isMine = True
                self._chunk[x][y].isMine = isMine

    def __repr__(self):
        temp = ""
        for x in self._chunk:
            temp += str(x)+"\n"
        return temp

    def draw(self):
        self.batch.draw()

    def updatesprites(self, pos:tuple):
        for x in range(0,16):
            for y in range(0,16):
                self._chunk[x][y].updatepos( (x*21+pos[0], y*21+pos[1]) )

    def gettile(self, pos):
        return self._chunk[pos[0]][pos[1]]


    def flagtile(self, tilepos:tuple):
        self.gettile(tilepos).flag()

    def activatetile(self, tilepos=None, tile=None):

        if not tile:
            tile = self.gettile(tilepos)
        elif not tilepos:
            tilepos = tile.pos


        if tile.isHidden and not tile.isFlagged:
            if tile.isMine:
                tile.reveal()
            else:
                neightiles = self.chunkmanager.getneighbouringtiles(poschunk=self.pos, postile=tilepos)

                mines = self.getmines( neightiles )

                tile.reveal(prox=mines)

                if mines == 0 and True: # True = use recursion
                    #WARNING: RECURSIVE!
                    #logging.warning("Chunk:74 Start of using a recursive function!")
                    for neightile in neightiles:
                        chunk, tile = neightile
                        if tile.isHidden and not tile.isFlagged:
                            #logging.debug("Chunk:76 Activiating Tile %s %s", tile, tile.pos)
                            chunk.activatetile(tile=tile)

    @staticmethod
    def getmines(tiles:list) ->int:
        count = 0
        for tile in tiles:
            if tile[1].isMine:
                count+=1
        return count