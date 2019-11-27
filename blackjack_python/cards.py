"""Card module"""
import random


class Card:
    """
    :type SUITS: tuple[str]
    :type RANKS: tuple[str]
    :type _VALUES: list[int]
    :type suit: str
    :type rank: str
    :type value: int
    """
    SUITS = ('S', 'C', 'D', 'H')
    RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')
    _VALUES = [min(i + 1, 10) for i in range(len(RANKS))]

    def __init__(self, suit, rank):
        """
        :type suit: str
        :type rank: str
        """
        self.suit = suit
        self.rank = rank
        self.value = Card._VALUES[Card.RANKS.index(rank)]

    def __repr__(self):
        return f"{self.suit}-{self.rank}"


class Deck:
    """
    :type _CARDS: list[Card]
    :type cards: list[Card]
    """
    _CARDS = [Card(s, r) for s in Card.SUITS for r in Card.RANKS]

    def __init__(self):
        self.cards = []

    def shuffle(self):
        self.cards = Deck._CARDS[:]
        random.shuffle(self.cards)

    def draw(self):
        """
        :rtype: Card
        """
        try:
            return self.cards.pop()
        except IndexError:
            print('>> Deck is empty!!')
            raise IndexError
