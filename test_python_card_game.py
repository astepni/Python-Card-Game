
from main import Card, Deck

def test_card_creation():
    """Testuje tworzenie karty."""
    card = Card('A', 'Hearts')
    assert card.value == 'A'
    assert card.suit == 'Hearts'

def test_deck_creation():
    """Testuje tworzenie talii."""
    deck = Deck()
    assert len(deck.cards) == 52

def test_deck_shuffle():
    """Testuje tasowanie talii."""
    deck = Deck()
    initial_cards = deck.cards.copy()
    deck.shuffle()
    assert deck.cards != initial_cards

def test_deck_deal():
    """Testuje rozdawanie karty."""
    deck = Deck()
    dealt_card = deck.deal()
    assert dealt_card is not None
    assert len(deck.cards) == 51

def test_deck_deal_empty():
    """Testuje rozdawanie karty z pustej talii."""
    deck = Deck()
    for _ in range(52):
        deck.deal()
    assert deck.deal() is None

def test_card_repr():
    """Testuje reprezentację karty."""
    card = Card('K', 'Spades')
    assert repr(card) == "K of Spades"

def test_deck_repr():
    """Testuje reprezentację talii."""
    deck = Deck()
    assert repr(deck) == "Deck of 52 cards"
