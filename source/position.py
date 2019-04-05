



class Position:

    tilesize = 21
    chunksize = 16

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
    def tupleadd(cls, posa:tuple, posb:tuple) -> tuple:
        return posa[0]+posb[0],posa[1]+posb[1]