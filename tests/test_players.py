import pytest

from blackjack.cards import Deck
from blackjack.players import Player


class MyDeck(Deck):
    def shuffle(self):
        self.cards = Deck._CARDS[:]


@pytest.fixture()
def my_deck():
    deck = MyDeck()
    deck.shuffle()
    deck.cards = deck.cards[::-1]
    return deck


def test_player(my_deck, capfd):
    player = Player()

    player.draw(my_deck)
    player.draw(my_deck)
    player.show()
    out, err = capfd.readouterr()
    assert out == 'Player(13) : S-A, S-2\n'

    player.draw(my_deck)
    player.draw(my_deck)
    player.show()
    out, err = capfd.readouterr()
    assert out == 'Player(20) : S-A, S-2, S-3, S-4\n'

    player.draw(my_deck)
    player.show()
    out, err = capfd.readouterr()
    assert out == 'Player(15) : S-A, S-2, S-3, S-4, S-5\n'
