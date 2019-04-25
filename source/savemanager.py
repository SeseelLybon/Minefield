

from chunkmanager import ChunkManager
from scoremanager import ScoreManager

import logging
import random
import pickle

import os

from chunkmanager import seed

class SaveManager:

    @classmethod
    def chunkdict_depointer(cls)-> dict:
        #go through each chunk
        depointered_chunk_dict = dict()

        for chunk_pos, chunk_p in ChunkManager.chunk_dict.items():
        #chunk_pos, chunk_p = (0,0), ChunkManager.chunk_dict.get((0,0))
            if chunk_p.chunkChanged:
                chunkhash = list()

                #go  through all of each chunk's tiles
                for x in range(0,16):
                    for y in range(0,16):
                        chunkhash.append( cls.hashtile( chunk_p._chunk[x][y] ))


                depointered_chunk_dict[chunk_pos] = chunkhash

        #print(depointered_chunk_dict[(0,0)])
        return depointered_chunk_dict

    @classmethod
    def savepicklejartofile(cls):
        print("Saving to picklejar")
        # saving
        with open("resources\savefile.temp", 'wb') as outfile:
            pickle.dump([random.getstate(),
                         cls.chunkdict_depointer(),
                         ScoreManager.getscore(),
                         ScoreManager.getclearedtiles(),
                         seed],
                         outfile, protocol=2)
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
    def loadpicklejarfromfile(cls):
        # loading

        if os.path.isfile('resources\savefile.dat'):
            print("Loading from picklejar")
            with open('resources\savefile.dat', 'rb') as infile:
                randomstate, depointered_chunkdict, score, tilescleared, seed = pickle.load(infile)

            #random.setstate(randomstate)
            cls.picklejar_loadchunks(depointered_chunkdict)
            ScoreManager.loadscore(score)
            ScoreManager.loadtilescleared(tilescleared)

            print("Done loading from picklejar")
            return seed, randomstate # Did load from savefile
        else:
            print("No savefile to load from")
            return False # Did NOT load from savefile



    @classmethod
    def hashtile(cls, tile):
        tilehash = [False]*5

        tilehash[0]=tile.proximity

        if tile.isHidden:
            tilehash[1]=True
        if tile.isFlagged:
            tilehash[2]=True
        if tile.isMine:
            tilehash[3]=True
        if tile.isDestroyed:
            tilehash[4]=True

        return tilehash



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