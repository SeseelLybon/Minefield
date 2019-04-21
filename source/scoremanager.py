

class ScoreManager:

    _score = 0
    _clearedtiles = 0

    @classmethod
    def changescore(cls,rhs:int):
        cls._score+=rhs

    @classmethod
    def tilecleared(cls):
        cls._clearedtiles+=1
    @classmethod
    def loadscore(cls, newscore):
        cls._score=newscore

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