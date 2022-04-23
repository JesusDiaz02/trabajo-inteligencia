"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card):
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card. 'J', 'Q', 'K' = 10; 'A' = 1; numerical value otherwise.
    """
    '''Calculate the value of a card
You can use the equality comparison operator == to determine if a card is an ace card: card == 'A'.

You can use the containment operator in to determine if a substring is contained inside a string: 'Q' in 'KJQ'.

You can use the int constructor to convert a str of an int to an int: int('13').'''
    if card in ('K','J','Q'):
        value = 10
    elif card == 'A':
        value = 1
    else:
        value=int(card)
    return value
    


def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

    :param card_one, card_two: str - cards dealt. 'J', 'Q', 'K' = 10; 'A' = 1; numerical value otherwise.
    :return: higher value card - str. Tuple of both cards if they are of equal value.
    """
    if value_of_card(card_one)> value_of_card(card_two):
        return card_one
    elif value_of_card(card_one)< value_of_card(card_two):
        return card_two
    else:
        return card_one, card_two
    pass


def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for the ace card.

    :param card_one, card_two: str - card dealt. 'J', 'Q', 'K' = 10;
           'A' = 11 (if already in hand); numerical value otherwise.

    :return: int - value of the upcoming ace card (either 1 or 11).
    """
    
    if 'A' in (card_one, card_two):
        return 1
    else:
        value_at_hand = 0
        for card in (card_one, card_two):
            value_at_hand += value_of_card(card)
        return 1 if value_at_hand >= 11 else 11
    


def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: str - cards dealt. 'J', 'Q', 'K' = 10; 'A' = 11; numerical value otherwise.
    :return: bool - if the hand is a blackjack (two cards worth 21).
    """
    cards = (card_one, card_two)
    if 'A' in cards:
        indexA = cards.index('A')
        otherIndex = 1 - indexA
        if value_of_card(cards[otherIndex]) == 10:
            return True
    return False


def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.

    :param card_one, card_two: str - cards dealt.
    :return: bool - if the hand can be split into two pairs (i.e. cards are of the same value).
    """
    return value_of_card(card_one) == value_of_card(card_two)


def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - if the hand can be doubled down (i.e. totals 9, 10 or 11 points).
    """
    valueAtHand = 0
    for card in(card_one, card_two):
        valueAtHand += value_of_card(card)

    return 9 <= valueAtHand <= 11