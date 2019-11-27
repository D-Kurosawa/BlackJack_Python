import pytest

from blackjack_python.cards import Deck
from blackjack_python.players import Dealer
from blackjack_python.players import Player


class MyDeck(Deck):
    def shuffle(self):
        self.cards = Deck._CARDS[:]
        self.cards = self.cards[::-1]


@pytest.fixture()
def my_deck():
    deck = MyDeck()
    deck.shuffle()
    return deck


def test_player(my_deck, capsys):
    player = Player()

    player.draw(my_deck)
    player.draw(my_deck)
    player.show()
    out, err = capsys.readouterr()
    assert out == 'Player(13) : S-A, S-2\n'

    player.draw(my_deck)
    player.draw(my_deck)
    player.show()
    out, err = capsys.readouterr()
    assert out == 'Player(20) : S-A, S-2, S-3, S-4\n'

    player.draw(my_deck)
    player.show()
    out, err = capsys.readouterr()
    assert out == 'Player(15) : S-A, S-2, S-3, S-4, S-5\n'


def test_dealer(my_deck, capsys):
    dealer = Dealer()
    player = Player()

    dealer.deal(my_deck, player)
    out, err = capsys.readouterr()
    assert out == 'Player(14) : S-A, S-3\nDealer(--) : S-2, ***\n'

    dealer.hit(my_deck)
    dealer.show()
    out, err = capsys.readouterr()
    assert out == 'Dealer(17) : S-2, S-4, S-5, S-6\n'


if __name__ == '__main__':
    pass
