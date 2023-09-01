"""
SOS Game
Name: Eray Semiz
From: Zonguldak/Turkey
"""
import colorama
from colorama import Fore
import re
colorama.init(autoreset=True)


class SosGame:
    def __init__(self):
        self.cells = {}
        for col in ["A", "B", "C", "D", "E", "F", "∅", "∅"]:
            for row in range(1, 9):
                self.cells[col + str(row)] = "|   |"
        self.players = ["Player1", "Player2"]
        self.current_player = 0
        self.player1_score = 0
        self.player2_score = 0
        self.patterns_vertical = set()
        self.patterns_diagonal_rd = set()
        self.patterns_diagonal_ld = set()
        self.patterns_horizontal = set()
        self.full_cells = set()
        self.empty_spaces = 36

    def run(self):
        self.board()

    def board(self):
        outline = "=" * 30
        lines = "-" * 30
        letters = "[ A ][ B ][ C ][ D ][ E ][ F ]"
        whitespace = " " * 4
        print(whitespace, Fore.LIGHTRED_EX + outline, " " * 3, Fore.LIGHTYELLOW_EX + "Scores:")
        print(Fore.LIGHTBLUE_EX + "|SOS|", Fore.GREEN + letters, " " * 5, Fore.LIGHTCYAN_EX + f"Player1 = {self.player1_score}", sep="")
        print(whitespace, lines, " " * 3, Fore.LIGHTGREEN_EX + f"Player2 = {self.player2_score}")
        for board_row in range(1, 7):
            print(Fore.GREEN + f"[ {board_row} ]", end="")
            for board_col in ["A", "B", "C", "D", "E", "F"]:
                print(self.cells[board_col + str(board_row)],  end="")
            print()
            print(whitespace, lines)
        print(whitespace, Fore.LIGHTRED_EX + outline)
        print()
        self.get_input_ml("move")

    def get_move(self, move, test_=0):
        if move.lower() == "exit":
            self.exit_game("Game exited.")
        elif move.lower() == "endgame":
            if self.player1_score > self.player2_score:
                self.exit_game("Player1 wins.")
            elif self.player1_score < self.player2_score:
                self.exit_game("Player2 wins.")
            else:
                self.exit_game("Draw.")
        elif re.search(r"^[A-F][1-6]$", move, re.IGNORECASE):
            if self.cells[move.upper()] != "|   |":
                print(Fore.MAGENTA + f"{move.upper()} is already filled.")
                self.get_input_ml("move")
            else:
                self.get_input_ml("letter", move)

        else:
            print(Fore.MAGENTA + "Please structure your input using letters from A to F and numbers from 1 to 6.")
            if test_ == 1:
                ...
            else:
                self.get_input_ml("move")

    def get_letter(self, letter, move, test_=0):
        if letter.lower() == "exit":
            self.exit_game("Game exited.")
        elif letter.lower() == "endgame":
            if self.player1_score > self.player2_score:
                self.exit_game("Player1 wins.")
            elif self.player1_score < self.player2_score:
                self.exit_game("Player2 wins.")
            else:
                self.exit_game("Draw.")
        if letter != "S" and letter != "O":
            print(Fore.MAGENTA + "Invalid letter.")
            if test_ == 1:
                ...
            else:
                self.get_input_ml("letter", move)

        else:
            self.current_player = (self.current_player + 1) % 2
            self.play(move.upper(), letter)

    def play(self, move, letter, test_=0):
        self.cells[move] = f"| {letter} |"
        if test_ == 1:
            ...
        else:
            if self.current_player == 0:
                self.score(self.players[1])
            else:
                self.score(self.players[0])
            self.end_game()
            self.board()      # ?

    def score_table(self, player):
        if player == "Player1":
            self.player1_score += 1
        else:
            self.player2_score += 1

    def score(self, player):
        columns = ["A", "B", "C", "D", "E", "F", "∅", "∅"]
        for column in columns:
            for row in range(1, 7):
                if (
                    self.cells.get(column + str(row)) == "| S |" and
                    self.cells.get(column + str(row + 1)) == "| O |" and
                    self.cells.get(column + str(row + 2)) == "| S |"
                ):
                    pattern = (column, row)
                    if pattern not in self.patterns_vertical:
                        self.patterns_vertical.add(pattern)
                        self.score_table(player)

                if (
                    self.cells.get(column + str(row)) == "| S |" and
                    self.cells.get(columns[columns.index(column) + 1] + str(row + 1)) == "| O |" and
                    self.cells.get(columns[columns.index(column) + 2] + str(row + 2)) == "| S |"
                ):
                    pattern = (column, row)
                    if pattern not in self.patterns_diagonal_rd:
                        self.patterns_diagonal_rd.add(pattern)
                        self.score_table(player)

                if (
                    self.cells.get(column + str(row)) == "| S |" and
                    self.cells.get(columns[columns.index(column) + 1] + str(row)) == "| O |" and
                    self.cells.get(columns[columns.index(column) + 2] + str(row)) == "| S |"
                ):
                    pattern = (column, row)
                    if pattern not in self.patterns_horizontal:
                        self.patterns_horizontal.add(pattern)
                        self.score_table(player)

                if (
                    self.cells.get(column + str(row)) == "| S |" and
                    self.cells.get(columns[columns.index(column) - 1] + str(row + 1)) == "| O |" and
                    self.cells.get(columns[columns.index(column) - 2] + str(row + 2)) == "| S |"
                ):
                    pattern = (column, row)
                    if pattern not in self.patterns_diagonal_ld:
                        self.patterns_diagonal_ld.add(pattern)
                        self.score_table(player)

    def end_game(self):
        for column in ["A", "B", "C", "D", "E", "F"]:
            for row in range(1, 7):
                if self.cells.get(column + str(row)) == "| O |" or self.cells.get(column + str(row)) == "| S |":
                    pattern = (column, row)
                    if pattern not in self.full_cells:
                        self.full_cells.add(pattern)
                        self.empty_spaces -= 1

        if self.empty_spaces == 0:
            if self.player1_score > self.player2_score:
                self.exit_game("Player1 wins")
            elif self.player1_score < self.player2_score:
                self.exit_game("Player2 wins")
            else:
                self.exit_game("Draw")

    def exit_game(self, message):
        raise SystemExit(message)

    def get_input_ml(self, prompt, variable=None):
        if prompt == "move":
            self.get_move(input(Fore.LIGHTWHITE_EX + f"{self.players[self.current_player]}, what's your move?: "))
        elif prompt == "letter":
            self.get_letter(input("Choose a letter( S or O ): ").upper(), variable)

    @staticmethod
    def main():
        sos = SosGame()
        sos.run()


if __name__ == '__main__':
    SosGame.main()
