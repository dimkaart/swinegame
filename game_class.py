from deck_class import Deck
from player_class import Player

class Game:
    def __init__(self):
        name1 = "p1"#input("p1 name ")
        name2 = "p2"#input("p2 name ")
        self.deck = Deck()
        self.cards_in_deck = len(self.deck.cards)
        self.p1 = Player(name1)
        self.p2 = Player(name2)

        self.current_player = 1

        self.end_game = False
        self.winner = None

        # Game Statistic
        self.turn = 0

    def check_winner(self, p1_deck, p2_deck):
        # Check if someone won
        if (self.cards_in_deck == 0) & (len(p1_deck) == 0):
            self.wins(self.p1.name)
            self.winner = self.p1.name
            self.end_game = True
        elif (self.cards_in_deck == 0) & (len(p2_deck) == 0):
            self.wins(self.p2.name)
            self.winner = self.p2.name
            self.end_game = True



    def wins(self, winner):
        w = f"{winner} wins this round"
        print(w)

    def play_game(self):
        cards = self.deck.cards
        p1_deck = self.p1.card
        p2_deck = self.p2.card

        open_card = cards.pop()
        open_deck = [open_card]
        max_len_open_deck = len(open_deck)

        while True:
            # Check for Winner
            self.check_winner(p1_deck, p2_deck)
            if self.end_game:
                break

            # Beginn next turn
            self.turn += 1

            # Player 2 turn
            if self.current_player == 1:
                if len(p2_deck) > 0:
                    p2_card = p2_deck.pop(0)
                else:
                    p2_card = cards.pop()
                    self.cards_in_deck = len(cards)

                #print("P2: ", len(p2_deck), " Open Deck: ", len(open_deck), " Deck: ", len(cards))

                open_deck.append(p2_card)
                # Statistic of largest deck on hand for Evaluation
                if len(open_deck) > max_len_open_deck:
                    max_len_open_deck = len(open_deck)

                if open_card.equal_suit(p2_card):
                    p2_deck = [*p2_deck, *open_deck]
                    # Statistic of largest deck on hand for Evaluation
                    if len(p2_deck) > self.p2.largest_deck_on_hand:
                        self.p2.largest_deck_on_hand = len(p2_deck)

                    open_card = p2_deck.pop(0)
                    open_deck = [open_card]
                    self.current_player = 2
                    continue
                else:
                    open_card = p2_card
                    self.current_player = 2

            # Check for Winner
            self.check_winner(p1_deck, p2_deck)
            if self.end_game:
                break

            # Beginn next turn
            self.turn += 1

            # Player 1 turn
            if self.current_player == 2:
                if len(p1_deck) > 0:
                    p1_card = p1_deck.pop(0)
                else:
                    p1_card = cards.pop()
                    self.cards_in_deck = len(cards)

                #print("P1: ", len(p1_deck), " Open Deck: ", len(open_deck), " Deck: ", len(cards))

                open_deck.append(p1_card)
                # Statistic of largest deck on hand for Evaluation
                if len(open_deck) > max_len_open_deck:
                    max_len_open_deck = len(open_deck)

                if open_card.equal_suit(p1_card):
                    p1_deck = [*p1_deck, *open_deck]
                    # Statistic of largest deck on hand for Evaluation
                    if len(p1_deck) > self.p1.largest_deck_on_hand:
                        self.p1.largest_deck_on_hand = len(p1_deck)

                    open_card = p1_deck.pop(0)
                    open_deck = [open_card]
                    self.current_player = 1
                    continue
                else:
                    open_card = p1_card
                    self.current_player = 1

            #TODO special case: len(p1_deck)=1, len(p2_deck)=1, len(open_deck)=1 and all three cards are of the same suit
            continue


        print(f"""Game finished after {self.turn} turns! 
              Player {self.p1.name} had maximum {self.p1.largest_deck_on_hand} cards on hand and player {self.p2.name} had maximum {self.p2.largest_deck_on_hand} cards on hand!
              The largest open deck was {max_len_open_deck}""")

        return self.winner, self.turn, self.p1.largest_deck_on_hand, self.p2.largest_deck_on_hand, max_len_open_deck
