



class Position:

    tilesize = 21
    chunksize = 16
    scale = 1
    world_offset = [0,0]

    @classmethod
    def pixtopos(cls, pix : tuple) -> tuple:
        pos = pix[0]//cls.tilesize,\
              pix[1]//cls.tilesize
        return pos

    @classmethod
    def pixtotile(cls, pix : tuple) -> tuple:
        tile = pix[0]//cls.tilesize%cls.chunksize,\
               pix[1]//cls.tilesize%cls.chunksize
        return tile

    @classmethod
    def pixtochunk(cls, pix : tuple) -> tuple:
        pos = pix[0]//cls.tilesize//cls.chunksize,\
              pix[1]//cls.tilesize//cls.chunksize
        return pos

    @classmethod
    def postochunk(cls, pos : tuple) -> tuple:
        pix = pos[0]*cls.tilesize,\
              pos[1]*cls.tilesize
        return pix

    @classmethod
    def tupleadd(cls, lhs:tuple, rhs:tuple) -> tuple:
        return lhs[0]+rhs[0],lhs[1]+rhs[1]