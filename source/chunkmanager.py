
from chunk import Chunk
from position import Position
import pyglet

import logging

batch = pyglet.graphics.Batch()
sprites = list()

class ChunkManager:

    worldsize = [0,0,0,0] #minx, maxx, miny, maxy
    chunk_dict = dict()

    @classmethod
    def registerchunk(cls, pos:tuple):
        cls.worldsize[0] = min(cls.worldsize[0], pos[0])
        cls.worldsize[1] = max(cls.worldsize[1], pos[0])
        cls.worldsize[2] = min(cls.worldsize[2], pos[1])
        cls.worldsize[3] = max(cls.worldsize[3], pos[1])
        cls.chunk_dict[pos] = Chunk(pos,cls)

    offsets = [(-1, -1), (0, -1), (1, -1),
               (-1, 0), (1, 0),  # doesn't contain (0,0) because this is self
               (-1, 1), (0, 1), (1, 1)]


    @classmethod
    def getneighbouringtiles(cls, poschunk:tuple, postile:tuple) ->list:
        poschunk = Position.pixtochunk(poschunk)
        tiles=list()

        for offset in cls.offsets:
            offsettile = Position.tupleadd(postile, offset)

            if 0 < offsettile[0] < 16 and 0 < offsettile[1] < 16:
                tiles.append( cls.chunk_dict[poschunk].gettile(offsettile) )

            elif True:
                #what if the tile is outside the chunk?
                chunk_offset = [0,0]

                #Right
                if offsettile[0] < 0:
                    chunk_offset[0] = -1
                #Left
                elif offsettile[0] >= 16:
                    chunk_offset[0] = 1
                #Down
                if offsettile[1] < 0:
                    chunk_offset[1] = -1
                #Up
                elif offsettile[1] >= 16:
                    chunk_offset[1] = 1


                offset_chunk = Position.tupleadd(poschunk,tuple(chunk_offset))
                offsettile = list(offsettile)

                if offsettile[0] == -1:
                    offsettile[0] = 15
                elif offsettile[0] == 16:
                    offsettile[0] = 0

                if offsettile[1] == -1:
                    offsettile[1] = 15
                elif offsettile[1] == 16:
                    offsettile[1] = 0

                tiles.append( cls.chunk_dict[offset_chunk].gettile(offsettile) )

        return tiles

    @classmethod
    def updatesprites(cls, offset):
        for key, value in cls.chunk_dict.items():
            value.updatesprites((offset[0]+value.pos[0],offset[1]+value.pos[1]))

    @classmethod
    def updategenchunks(cls, offset, windowsize:tuple):

        screenzero = -offset[0], -offset[1]
        dots = {Position.pixtochunk((screenzero[0], screenzero[1])),
                Position.pixtochunk((screenzero[0]+windowsize[0]//2, screenzero[1])),
                Position.pixtochunk((screenzero[0]+windowsize[0], screenzero[1])),
                Position.pixtochunk((screenzero[0], screenzero[1]+windowsize[1]//2)),
                Position.pixtochunk((screenzero[0] + windowsize[0] // 2, screenzero[1]+windowsize[1]//2)),
                Position.pixtochunk((screenzero[0] + windowsize[0], screenzero[1]+windowsize[1]//2)),
                Position.pixtochunk((screenzero[0], screenzero[1]+windowsize[1])),
                Position.pixtochunk((screenzero[0] + windowsize[0] // 2, screenzero[1]+windowsize[1])),
                Position.pixtochunk((screenzero[0] + windowsize[0], screenzero[1]+windowsize[1])),
                }

        for dot in dots:
            if not cls.chunk_dict.get( dot ):
                cls.registerchunk(dot)

    @classmethod
    def screenspaceocclude_drawchunks(cls, offset, windowsize: tuple):

        screenzero = -offset[0], -offset[1]
        dots = {Position.pixtochunk((screenzero[0], screenzero[1])),
                Position.pixtochunk((screenzero[0] + windowsize[0] // 2, screenzero[1])),
                Position.pixtochunk((screenzero[0] + windowsize[0], screenzero[1])),
                Position.pixtochunk((screenzero[0], screenzero[1] + windowsize[1] // 2)),
                Position.pixtochunk((screenzero[0] + windowsize[0] // 2, screenzero[1] + windowsize[1] // 2)),
                Position.pixtochunk((screenzero[0] + windowsize[0], screenzero[1] + windowsize[1] // 2)),
                Position.pixtochunk((screenzero[0], screenzero[1] + windowsize[1])),
                Position.pixtochunk((screenzero[0] + windowsize[0] // 2, screenzero[1] + windowsize[1])),
                Position.pixtochunk((screenzero[0] + windowsize[0], screenzero[1] + windowsize[1])),
                }

        for dot in dots:
            chunk = cls.chunk_dict.get(dot, None)
            if chunk:
                chunk.batch.draw()