"""
開発するブラックジャックのルール

- 初期カードは52枚。引く際にカードの重複は無いようにする
- プレイヤーとディーラーの2人対戦。プレイヤーは実行者、ディーラーは自動的に実行
- 実行開始時、プレイヤーとディーラーはそれぞれ交互にカードを2枚引く
    引いたカードは画面に表示する。ただし、ディーラーの2枚目のカードは分からないようにする
- その後、先にプレイヤーがカードを引く
    プレイヤーが21を超えていたらバースト、その時点でゲーム終了
- プレイヤーは、カードを引くたびに、次のカードを引くか選択できる
- プレイヤーが引き終えたら、その後ディーラーは、自分の手札が17以上になるまで引き続ける
- プレイヤーとディーラーが引き終えたら勝負
    より21に近い方の勝ち
- JとQとKは10として扱う
- ダブルダウンなし、スプリットなし、サレンダーなし、その他特殊そうなルールなし
- ゲームを何ゲームも続けられるようにする
"""
from .cards import Deck
from .players import Dealer
from .players import Player


def main():
    game = BlackJack()
    game.play()


class BlackJack:
    """
    :type deck: Deck
    :type player: Player
    :type dealer: Dealer
    """

    def __init__(self):
        self.deck = Deck()
        self.player = Player()
        self.dealer = Dealer()

    def play(self):
        print('\n<----------- Deal ----------->')
        self.dealer.deal(self.deck, self.player)
        print('<---------------------------->\n')

        self.player.hit(self.deck)

        if self.player.score <= Player.MAX_SCORE:
            self.dealer.hit(self.deck)

        print('<---------------------------->')
        self.player.show()
        self.dealer.show()
        print('<---------------------------->')

        print(f"\n{self.judge()}\n")

    def judge(self):
        """
        :rtype: str
        """
        if self.player.score > Player.MAX_SCORE:
            return 'Dealer Win'

        if self.dealer.score > Dealer.MAX_SCORE:
            return 'Player Win'

        if self.player == self.dealer:
            return 'Draw'

        if self.player > self.dealer:
            return 'Player Win'

        if self.player < self.dealer:
            return 'Dealer Win'

        raise ValueError


if __name__ == '__main__':
    main()
