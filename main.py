from player import HumanPlayer, BotPlayer
from game import GameEngine

def setup_and_play():
    print("=== Welcome to Tic-Tac-Toe ! ===")

    player_symbol = ""
    while player_symbol not in ["X", "O"]:
        player_symbol = input("Choose your symbol (X or O) : ").upper()
    
    bot_symbol = "O" if player_symbol == "X" else "X"

    human = HumanPlayer("Player", player_symbol)
    bot = BotPlayer("Computer", bot_symbol)

    BOARD_SIZE = 3
    WIN_CONDITION = 3

    while True:
        game = GameEngine(human, bot, board_size=BOARD_SIZE, win_condition=WIN_CONDITION)
        game.play_game()

        replay = input("\nDo you want to play again? (Y/N) : ").upper()
        if replay != "Y":
            print("Thank you for playing! See you soon at Easi.")
            break

if __name__ == "__main__":
    setup_and_play()