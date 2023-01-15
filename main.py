from game_class import Game
import pandas as pd
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    df = pd.DataFrame({}, columns=["Winner", "Turns", "P1_Max_Deck", "P2_Max_Deck", "Max_Open_Deck"])
    for _ in range(1000):
        game = Game()
        winner, turns, p1_max_deck, p2_max_deck, max_open_deck = game.play_game()
        df = df.append({"Winner":winner, "Turns":turns, "P1_Max_Deck":p1_max_deck, "P2_Max_Deck":p2_max_deck, "Max_Open_Deck":max_open_deck}, ignore_index=True)
    print(df)

