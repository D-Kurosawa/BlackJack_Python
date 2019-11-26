import pytest

from blackjack import cards


@pytest.fixture
def my_card():
    return cards.Card('D', 'A')


def test_card(my_card):
    assert repr(my_card) == 'D-A'
