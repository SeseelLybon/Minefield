

class ScoreManager:

    _score = 0
    _clearedtiles = 0

    @classmethod
    def changescore(cls,rhs:int):
        cls._score+=rhs

    @classmethod
    def clearscore(cls):
        cls._score=0
        cls._clearedtiles=0

    @classmethod
    def tilecleared(cls):
        cls._clearedtiles+=1

    @classmethod
    def loadscore(cls, a):
        cls._score=a

    @classmethod
    def loadtilescleared(cls, a):
        cls._clearedtiles=a

    @classmethod
    def hitmine(cls):
        cls._score-=50

    @classmethod
    def nomine(cls):
        cls._score+=1

    @classmethod
    def clearedchunk(cls):
        pass

    @classmethod
    def losttile(cls):
        cls._score-=10

    @classmethod
    def getscore(cls) -> int:
        return cls._score

    @classmethod
    def getclearedtiles(cls) -> int:
        return cls._clearedtiles