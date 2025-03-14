import random

class Card:
    """Klasa reprezentująca pojedynczą kartę."""
    
    def __init__(self, value, suit):
        """
        Inicjalizuje kartę z podaną wartością i figurą.
        
        :param value: Wartość karty (np. '9', 'A', 'K').
        :param suit: Figura karty (np. 'Hearts', 'Diamonds').
        """
        self.value = value
        self.suit = suit

    def __repr__(self):
        """Zwraca reprezentację karty w postaci stringa."""
        return f"{self.value} of {self.suit}"


class Deck:
    """Klasa reprezentująca talię kart."""
    
    def __init__(self):
        """
        Inicjalizuje talię kart z wszystkimi możliwymi kombinacjami wartości i figur.
        """
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.cards = [Card(value, suit) for value in values for suit in suits]

    def shuffle(self):
        """Losowo tasuje karty w talii."""
        random.shuffle(self.cards)

    def deal(self):
        """
        Usuwa i zwraca ostatnią kartę z talii.
        
        :return: Ostatnia karta z talii lub None, jeśli talia jest pusta.
        """
        return self.cards.pop() if self.cards else None

    def __repr__(self):
        """Zwraca reprezentację talii w postaci stringa."""
        return f"Deck of {len(self.cards)} cards"


# Przykład użycia
if __name__ == "__main__":
    # Utwórz nową talię kart
    my_deck = Deck()
    print("Initial deck:", my_deck)

    # Tasuj karty
    my_deck.shuffle()
    print("Shuffled deck:", my_deck)

    # Rozdaj jedną kartę
    dealt_card = my_deck.deal()
    print("Dealt card:", dealt_card)
    print("Deck after dealing a card:", my_deck)
    
