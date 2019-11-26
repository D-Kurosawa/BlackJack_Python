"""Card module"""


class Card:
    """
    :type SUITS: tuple[str]
    :type RANKS: tuple[str]
    :type VALUES: list[int]
    :type suit: str
    :type rank: str
    :type value: int
    """
    SUITS = ('S', 'C', 'D', 'H')
    RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')
    VALUES = [min(i + 1, 10) for i in range(len(RANKS))]

    def __init__(self, suit, rank):
        """
        :type suit: str
        :type rank: str
        """
        self.suit = suit
        self.rank = rank
        self.value = Card.VALUES[Card.RANKS.index(rank)]

    def __repr__(self):
        return f"{self.suit}-{self.rank}"
