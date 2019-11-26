import pytest

from blackjack import cards


@pytest.fixture
def my_card():
    return cards.Card('D', 'A')


def test_card(my_card):
    assert repr(my_card) == 'D-A'


@pytest.fixture
def my_deck():
    deck = cards.Deck()
    deck.shuffle()
    return deck


def draw(my_deck, num):
    draw_cards = []
    for _ in range(num):
        draw_cards.append(repr(my_deck.draw()))

    return draw_cards


def test_deck(my_deck):
    num = len(cards.Card.SUITS) * len(cards.Card.RANKS)

    draw_cards1 = draw(my_deck, num)
    my_deck.shuffle()
    draw_cards2 = draw(my_deck, num)

    assert len(set(draw_cards1)) == num
    assert draw_cards2 != draw_cards1
