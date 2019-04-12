

from tile import Tile

from random import random

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
                if random() > 0.80:
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

    def activatetile(self, tilepos:tuple):

        tile = self.gettile(tilepos)

        if tile.isHidden and not tile.isFlagged:
            if tile.isMine:
                tile.reveal()
            else:
                neightiles = self.chunkmanager.getneighbouringtiles(poschunk=self.pos, postile=tilepos)
                mines = self.getmines( neightiles )
                tile.reveal(prox=mines)
                if mines == 0 and False: # True = use recursion
                    #WARNING: RECURSIVE!
                    logging.warning("Chunk:68 Start of using a recursive function!")
                    for tile in neightiles:
                        pass
                        self.activatetile_recursive(tile)

    def activatetile_recursive(self, tile:Tile):
        tilepos = tile.pos

        if not tile.isFlagged:
            if tile.isMine:
                tile.reveal()
            else:
                #TODO: sends wierd postile
                #logging.debug("chunk:81 %s, %s", self.pos, tilepos)
                neightiles = self.chunkmanager.getneighbouringtiles(poschunk=self.pos, postile=tilepos)
                mines = self.getmines( neightiles )
                tile.reveal(prox=mines)
                if mines == 0 and False: # True = use recursion
                    #WARNING: RECURSIVE!
                    logging.warning("Chunk:87 Continues use of a recursive function!")
                    for tile in neightiles:
                        pass
                        self.activatetile_recursive(tile)

    @staticmethod
    def getmines(tiles:list) ->int:
        count = 0
        for tile in tiles:
            if tile.isMine:
                count+=1
        return count