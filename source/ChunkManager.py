
from chunk import Chunk
from position import Position
import pyglet

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

    @classmethod
    def updategenchunks(cls, offset, windowsize:tuple):


        dots = [Position.pixtochunk( ( offset[0]-windowsize[0], offset[1]) ),
                Position.pixtochunk((offset[0] - windowsize[0] // 2, offset[1])),
                Position.pixtochunk(offset),
                P,
                P,
                P,
                P,
                P,
                P,
                P,
                P,
                P
                ]

        for dot in dots:
            if not cls.chunk_dict.get( dot ):
                cls.registerchunk(dot)
            


        dot =



        dot =

        if not cls.chunk_dict.get( dot ):
            cls.registerchunk(dot)

        '''
        dot = Position.pixtochunk( ( offset[0], offset[1]-windowsize[1]//2) )

        if not cls.chunk_dict.get( dot ):
            cls.registerchunk(dot)


        dot = Position.pixtochunk( ( offset[0]-windowsize[0]//2, offset[1]-windowsize[1]//2) )

        if not cls.chunk_dict.get( dot ):
            cls.registerchunk(dot)


        dot = Position.pixtochunk( ( offset[0]-windowsize[0], offset[1]-windowsize[1]//2) )

        if not cls.chunk_dict.get( dot ):
            cls.registerchunk(dot)


        dot = Position.pixtochunk( ( offset[0], offset[1]-windowsize[1]) )

        if not cls.chunk_dict.get( dot ):
            cls.registerchunk(dot)


        dot = Position.pixtochunk( ( offset[0]-windowsize[0]//2, offset[1]-windowsize[1]) )

        if not cls.chunk_dict.get( dot ):
            cls.registerchunk(dot)


        dot = Position.pixtochunk( ( offset[0]-windowsize[0], offset[1]-windowsize[1]) )

        if not cls.chunk_dict.get( dot ):
            cls.registerchunk(dot)
        '''