class TicTacToe:
    def __init__(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.players = ["X", "O"]
        self.turn = 0
    
    def print_board(self):
        for row in self.board:
            print(" | ".join(row))
            print("-" * 9)
    
    def check_winner(self, player):
        for i in range(3):
            if all(cell == player for cell in self.board[i]) or all(self.board[j][i] == player for j in range(3)):
                return True
        if all(self.board[i][i] == player for i in range(3)) or all(self.board[i][2 - i] == player for i in range(3)):
            return True
        return False
    
    def is_full(self):
        return all(cell in ("X", "O") for row in self.board for cell in row)
    
    def play(self):
        while True:
            self.print_board()
            player = self.players[self.turn % 2]
            
            try:
                row, col = map(int, input(f"Player {player}, enter row and column (0-2, space-separated): ").split())
                if self.board[row][col] != " ":
                    print("Cell is already taken. Try again.")
                    continue
            except (ValueError, IndexError):
                print("Invalid input. Please enter two numbers between 0 and 2.")
                continue

            
            self.board[row][col] = player
            
            if self.check_winner(player):
                self.print_board()
                print(f"Player {player} wins!")
                break
            
            if self.is_full():
                self.print_board()
                print("It's a draw!")
                break
            
            self.turn += 1


if __name__ == "__main__":
    game = TicTacToe()
    game.play()
