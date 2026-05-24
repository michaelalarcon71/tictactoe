class Board:
    def __init__(self, size=3):
        self.size = size
        self.grid = [[" " for _ in range(size)] for _ in range(size)]

    def display(self):
        print("\n" + "---" * self.size + "-")
        for row in self.grid:
            print("| " + " | ".join(row) + " |")
            print("---" * self.size + "-")

    def is_cell_empty(self, row, col):
        if 0 <= row < self.size and 0 <= col < self.size:
            return self.grid[row][col] == " "
        return False

    def place_symbol(self, row, col, symbol):
        if self.is_cell_empty(row, col):
            self.grid[row][col] = symbol
            return True
        return False

    def get_empty_cells(self):
        empty_cells = []
        for r in range(self.size):
            for c in range(self.size):
                if self.grid[r][c] == " ":
                    empty_cells.append((r, c))
        return empty_cells

    def is_full(self):
        return len(self.get_empty_cells()) == 0