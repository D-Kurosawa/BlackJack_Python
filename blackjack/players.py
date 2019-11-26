"""Players module"""
from functools import total_ordering


@total_ordering
class Player:
    """
    :type NAME: str
    :type MAX_SCORE: int
    :type hands: list[Card]
    :type score: int
    """
    NAME = 'Player'
    MAX_SCORE = 21

    def __init__(self):
        self.hands = []
        self.score = 0

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self.score == other.score

    def __lt__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self.score < other.score
