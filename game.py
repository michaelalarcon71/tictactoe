from board import Board

class GameEngine:
    def __init__(self, player1, player2, board_size=3, win_condition=3):
        self.board = Board(board_size)
        self.players = [player1, player2]
        self.win_condition = win_condition
        self.current_turn = 0  

    def switch_turn(self):
        self.current_turn = 1 - self.current_turn

    def get_current_player(self):
        return self.players[self.current_turn]

    def check_victory(self, symbol):
        size = self.board.size
        grid = self.board.grid
        k = self.win_condition

        for r in range(size):
            for c in range(size - k + 1):
                if all(grid[r][c + i] == symbol for i in range(k)):
                    return True

        for c in range(size):
            for r in range(size - k + 1):
                if all(grid[r + i][c] == symbol for i in range(k)):
                    return True

        for r in range(size - k + 1):
            for c in range(size - k + 1):
                if all(grid[r + i][c + i] == symbol for i in range(k)):
                    return True

        for r in range(k - 1, size):
            for c in range(size - k + 1):
                if all(grid[r - i][c + i] == symbol for i in range(k)):
                    return True

        return False

    def play_game(self):
        print("\n--- Start Game ---")
        while True:
            self.board.display()
            current_player = self.get_current_player()

            row, col = current_player.get_move(self.board)
            self.board.place_symbol(row, col, current_player.symbol)

            if self.check_victory(current_player.symbol):
                self.board.display()
                print(f"{current_player.name} won !")
                break

            if self.board.is_full():
                self.board.display()
                print("Game is a draw!")
                break

            self.switch_turn()