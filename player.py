import random

class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def get_move(self, board):
        raise NotImplementedError("This method should be implemented by subclasses.")

class HumanPlayer(Player):
    def get_move(self, board):
        while True:
            try:
                move = input(f"{self.name} ({self.symbol}), enter your move (row,column) e.g., '1,2' : ")
                row, col = map(int, move.split(","))
                if board.is_cell_empty(row - 1, col - 1):
                    return row - 1, col - 1
                else:
                    print("This square is already occupied or out of bounds. Please try again.")
            except (ValueError, IndexError):
                print("Invalid format. Please enter two numbers separated by a comma (e.g., 1,2).")

class BotPlayer(Player):
    def get_move(self, board):
        empty_cells = board.get_empty_cells()
        if empty_cells:
            return random.choice(empty_cells)
        return None
    