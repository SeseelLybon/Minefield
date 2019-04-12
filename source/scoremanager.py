

class ScoreManager:

    _score = 0

    @classmethod
    def changescore(cls,rhs:int):
        cls._score+=rhs

    @classmethod
    def getscore(cls) -> int:
        return cls._score