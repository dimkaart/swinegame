

class Player():
    def __init__(self, name):
        self.wins = 0
        self.card = []
        self.name = name
        self.largest_deck_on_hand = 0

    def draw_card(self, card):
        self.card.append(card)