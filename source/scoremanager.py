

class ScoreManager:

    _score = 0

    @classmethod
    def changescore(cls,rhs:int):
        cls._score+=rhs


    @classmethod
    def hitmine(cls):
        cls._score-=100

    @classmethod
    def nomine(cls):
        cls._score+=1

    @classmethod
    def getscore(cls) -> int:
        return cls._score