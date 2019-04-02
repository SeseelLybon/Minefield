



class Position:

    @classmethod
    def pixtopos(cls, pix : tuple) -> tuple:
        pos = pix[0]//21,pix[1]//21
        return pos

    @classmethod
    def pixtotile(cls, pix : tuple) -> tuple:
        tile = pix[0]//21%16,pix[1]//21%16
        return tile

    @classmethod
    def pixtochunk(cls, pix : tuple) -> tuple:
        pos = pix[0]//21//16,pix[1]//21//16
        return pos

    @classmethod
    def postopix(cls, pos : tuple) -> tuple:
        pix = pos[0]*21,pos[1]*21
        return pix