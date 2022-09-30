from enum import Enum, auto

class Card:
    @property
    def card_value(self) -> int:
        raise NotImplementedError()

    def __lt__(self, other):
        return self.card_value < other.card_value

class Suit(Enum):
    CLUBS = auto()
    DIAMONDS = auto()
    HEARTS = auto()
    SPADES = auto()

class PlayingCard(Card):
    """
    PlayingCard.SUITS
    {'Clubs': <Suit.CLUBS: 1>, 'Diamonds': <Suit.DIAMONDS: 2>, 'Hearts': <Suit.HEARTS: 3>, 'Spades': <Suit.SPADES: 4>}
    
    PlayingCard.SUIT_NAMES
    {<Suit.CLUBS: 1>: 'Clubs', <Suit.DIAMONDS: 2>: 'Diamonds', <Suit.HEARTS: 3>: 'Hearts', <Suit.SPADES: 4>: 'Spades'}
    
    PlayingCard.VALUES
    {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13}
    
    PlayingCard.VALUE_NAMES
    {1: 'A', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: '10', 11: 'J', 12: 'Q', 13: 'K'}

    """
    SUITS = {
        "Clubs": Suit.CLUBS,
        "Diamonds": Suit.DIAMONDS,
        "Hearts": Suit.HEARTS,
        "Spades": Suit.SPADES,
    }
    SUIT_NAMES = {e: n for n, e in SUITS.items()}
    VALUES = {
        "A": 1,
        **{str(i): i for i in range(2, 11)},
        "J": 11,
        "Q": 12,
        "K": 13,
    }
    VALUE_NAMES = {e: n for n, e in VALUES.items()}

    def __init__(self, suit: str, value: str):
        super().__init__()
        self.__suit = self.SUITS[suit]
        self.__value = self.VALUES[value]

    @property
    def card_value(self) -> int:
        # 这个用作 pc_c3 = PlayCard('Clubs', '3')
        # pc_c3.card_value  
        return self.__value

    def __str__(self) -> str:
        # 这个用作print(PlayCard('Clubs', '3'))
        value = self.VALUE_NAMES[self.__value]
        suit = self.SUIT_NAMES[self.__suit]
        return f'{value} of {suit}'

class JokerColor(Enum):
    RED = auto()
    BLACK = auto()

class Joker(Card):
    COLORS = {
        "Red": JokerColor.RED,
        "Black": JokerColor.BLACK,
    }

    COLOR_NAMES = {e: n for n, e in COLORS.items()}

    def __init__(self, color: str):
        super().__init__()
        self.__color = self.COLORS[color]

    @property
    def card_value(self):
        return 14

    def __str__(self) -> str:
        return f"{self.COLOR_NAMES[self.__color]} Joker"

class Game:
    def __init__(self):
        self.__cards: list[Card] = []

    def add_card(self, suit: str, value: str) -> None:
        self.__cards.append(PlayingCard(suit, value))

    def card_string(self, card: int) -> str:
        return str(self.__cards[card])

    def card_beats(self, card_a: int, card_b: int) -> bool:
        return self.__cards[card_a] > self.__cards[card_b]

    def add_joker(self, color: str) -> None:
        self.__cards.append(Joker(color))

if __name__ == '__main__':
    # pc_c3 = PlayingCard('Clubs', '3')
    # pc_s4 = PlayingCard('Spades', '4')
    # print(pc_c3.card_value)
    # print(pc_c3)
    # print(pc_s4.card_value)

    game = Game()
    # suit, value = input().split()
    # example input
    # Clubs 3
    # Diamonds 4
    suit = 'Clubs'
    value = '3'
    game.add_joker(value) if suit == "Joker" else game.add_card(suit, value)
    print(game.card_string(0))

    #suit, value = input().split()
    suit = 'Hearts'
    value = 'J'
    game.add_joker(value) if suit == "Joker" else game.add_card(suit, value)
    print(game.card_string(1))
    print("true" if game.card_beats(0, 1) else "false")
    print(game.__dict__)
    print(game._Game__cards)
