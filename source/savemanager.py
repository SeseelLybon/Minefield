

from chunkmanager import ChunkManager
from scoremanager import ScoreManager

import logging
import random
import pickle

import os

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
                    chunkhash.append( cls.hashtile( chunk_p._chunk[x][y] ))


            depointered_chunk_dict[chunk_pos] = chunkhash

        return depointered_chunk_dict

    @classmethod
    def savepicklejartofile(cls):
        print("Saving to picklejar")
        # saving
        with open("resources\savefile.temp", 'wb') as outfile:
            pickle.dump([random.getstate(),
                         cls.chunkdict_depointer(),
                         ScoreManager.getscore()], outfile, protocol=2)
        if os.path.isfile('resources\savefile.dat'):
            os.remove('resources\savefile.dat')
        os.rename("resources\savefile.temp", "resources\savefile.dat")
        print("Done saving to picklejar")



    @classmethod
    def picklejar_loadchunks(cls, chunkdict:dict):
        #go through each chunk

        for chunk_pos, chunkhash in chunkdict.items():
            ChunkManager.loadchunk(chunk_pos, chunkhash)

    @classmethod
    def loadpicklejarfromfile(cls) -> bool:
        # loading

        if os.path.isfile('resources\savefile.dat'):
            print("Loading from picklejar")
            with open('resources\savefile.dat', 'rb') as infile:
                randomstate, depointered_chunkdict, score = pickle.load(infile)

            random.setstate(randomstate)
            ScoreManager.loadscore(score)
            cls.picklejar_loadchunks(depointered_chunkdict)

            print("Done loading from picklejar")
            return True # Did load from savefile
        else:
            print("No savefile to load from")
            return False # Did NOT load from savefile



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
    print("Starting savemanager.py as main")

    logging.warning("Generating new chunk")
    ChunkManager.registerchunk((0, 0))
    print(ChunkManager.chunk_dict[(0,0)])

    print("Saving chunk to file")
    SaveManager.savepicklejartofile()

    print("Destroying chunk dict")
    ChunkManager.chunk_dict = dict()

    print("Loading chunk from savefile")
    SaveManager.loadpicklejarfromfile()
    print(ChunkManager.chunk_dict[(0,0)])

    print("Saving chunk to file")
    SaveManager.savepicklejartofile()

    print("Done with savemanager.py as main")