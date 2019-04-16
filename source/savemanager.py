

from chunkmanager import ChunkManager
from scoremanager import ScoreManager

import logging
import random
import pickle

class SaveManager:

    @classmethod
    def chunkdict_depointer(cls)-> dict:
        #go through each chunk
        depointered_chunk_dict = dict()

        for chunk_pos, chunk_p in ChunkManager.chunk_dict.items():
        #chunk_pos, chunk_p = (0,0), ChunkManager.chunk_dict.get((0,0))
            chunkhash = list()

            #go  through all of each chunk's tiles
            for x in range(0,16):
                for y in range(0,16):
                    chunkhash.append( cls.hashtile( chunk_p.gettile((x,y)) ))
            logging.debug("%s", chunkhash)

            depointered_chunk_dict[chunk_pos] = chunkhash

        return depointered_chunk_dict

    @classmethod
    def savepicklejartofile(cls):
        # saving
        with open("resources\savefile.dat", 'wb') as outfile:
            pickle.dump([random.getstate(),
                         cls.chunkdict_depointer(),
                         ScoreManager.getscore()], outfile, protocol=2)



    @classmethod
    def picklejar_loadchunks(cls, chunkdict:dict):
        #go through each chunk

        for chunk_pos, chunk_p in ChunkManager.chunk_dict.items():
            ChunkManager.loadchunk(chunk_pos, chunk_p)

    @classmethod
    def loadpicklejarfromfile(cls):
        # loading
        with open('resources\savefile.dat', 'rb') as infile:
            randomstate, depointered_chunkdict, score = pickle.load(infile)

        random.setstate(randomstate)
        ScoreManager.loadscore(score)
        cls.picklejar_loadchunks(depointered_chunkdict)



    @classmethod
    def hashtile(cls, tile):
        boolhash = int()

        boolhash+=tile.proximity

        if tile.isHidden:
            boolhash+=10
        if tile.isFlagged:
            boolhash+=100
        if tile.isMine:
            boolhash+=1000
        if tile.isDestroyed:
            boolhash+=10000
        return boolhash






if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    logging.warning("Starting savemanager.py as main")

    logging.warning("Generating new chunk")
    ChunkManager.registerchunk((0, 0))

    logging.warning("Saving chunk to file")
    SaveManager.savepicklejartofile()

    logging.warning("Loading chunk from savefile")
    SaveManager.loadpicklejarfromfile()

    logging.warning("Saving chunk to file")
    SaveManager.savepicklejartofile()

    logging.warning("Done with savemanager.py as main")