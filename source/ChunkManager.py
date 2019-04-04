
from chunk import Chunk
from position import Position
import pyglet

batch = pyglet.graphics.Batch()
sprites = list()

class ChunkManager:


    chunk_dict = dict()

    @classmethod
    def registerchunk(cls, pos:tuple):
        cls.chunk_dict[pos] = Chunk(pos,cls,batch=batch)

    offsets = [(-1, -1), (0, -1), (1, -1),
               (-1, 0), (1, 0),  # doesn't contain (0,0) because this is self
               (-1, 1), (0, 1), (1, 1)]

    @classmethod
    def getneighbouringmines(cls, poschunk:tuple, postile:tuple) ->int:
        poschunk = Position.pixtochunk(poschunk)
        count= 0

        for offset in cls.offsets:
            offsettile = Position.tupleadd(postile, offset)
            if 0 < offsettile[0] < 16 and 0 < offsettile[1] < 16:
                if cls.chunk_dict[poschunk].gettile(offsettile).isMine:
                    count+=1
            #what if the tile is outside the chunk?


        return count

    @classmethod
    def updatesprites(cls, offset):
        for key, value in cls.chunk_dict.items():
            value.updatesprites((offset[0]+value.pos[0],offset[1]+value.pos[1]))