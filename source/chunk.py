

from tile import Tile

import random

import pyglet

class Chunk:
    def __init__(self, pos:tuple, chunkmanager, chunkhash=None):
        self.chunkChanged = False
        self.batch = pyglet.graphics.Batch()
        self.chunkmanager = chunkmanager
        self.pos = pos[0]*16*21,pos[1]*16*21 #self.pos is in pixels, pos is in chunks!!!
        self._chunk = [None]*16

        for i in range(0,16):
            self._chunk[i] = [None]*16

        if not chunkhash: #if no chunkhash was passed, generate new chunk data

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

        else: # if chunkhash was passed, use chunkhash for chunk
            self.chunkChanged = True
            for x in range(0,16):
                for y in range(0,16):
                    self._chunk[x][y] = Tile(self.batch, pos=(x,y), tilehash=chunkhash[x*16+y])

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
        self.chunkChanged = True
        self.gettile(tilepos).flag()
        '''
        neightiles = self.chunkmanager.getneighbouringtiles(poschunk=self.pos, postile=tilepos)
        flags = self.getflagsandmines(neightiles)

        if tile.proximity == flags:
            #WARNING: RECURSIVE!
            for neightile in neightiles:
                chunk, tile = neightile
                if tile.isHidden and not tile.isFlagged:
                    # logging.debug("Chunk:76 Activiating Tile %s %s", tile, tile.pos)
                    tile.flag()
        '''

    def activatetile(self, tilepos=None, tile=None, explosion=False):
        self.chunkChanged = True
        if not tile:
            tile = self.gettile(tilepos)
        elif not tilepos:
            tilepos = tile.pos


        if tile.isHidden and (not tile.isFlagged or explosion):
            if tile.isMine:
                tile.triggermine()

                neightiles = self.chunkmanager.getneighbouringtiles(poschunk=self.pos, postile=tilepos)

                for neightile in neightiles:
                    chunk, tile = neightile
                    # logging.debug("Chunk:76 Activiating Tile %s %s", tile, tile.pos)
                    if tile.isMine:
                        chunk.activatetile(tile=tile, explosion=True)
                    else:
                        tile.triggermine()

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

        # if the tile is not hidden, if it has the same amount as flags as proximity, reveal the other tiles
        # REGARDLESS IF IT IS A BAD FLAG
        elif not tile.isHidden:
            neightiles = self.chunkmanager.getneighbouringtiles(poschunk=self.pos, postile=tilepos)
            flags = self.getflagsandmines(neightiles)

            if tile.proximity == flags:
                #WARNING: RECURSIVE!
                for neightile in neightiles:
                    chunk, tile = neightile
                    if tile.isHidden and not tile.isFlagged:
                        # logging.debug("Chunk:76 Activiating Tile %s %s", tile, tile.pos)
                        chunk.activatetile(tile=tile)





    @staticmethod
    def getmines(tiles:list) ->int:
        count = 0
        for tile in tiles:
            if tile[1].isMine:
                count+=1
        return count

    @staticmethod
    def getflagsandmines(tiles: list) -> int:
        count = 0
        for tile in tiles:
            if tile[1].isFlagged or (tile[1].isMine and not tile[1].isHidden):
                count += 1
        return count

