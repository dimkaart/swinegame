from random import shuffle
from card_class import Card

class Deck:
    def __init__(self):
        self.cards = []
        card_id = 0
        for i in range(2, 15):
            for j in range(4):
                self.cards.append(Card(i, j, card_id))
                card_id += 1
        shuffle(self.cards)

    def rm_card(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()