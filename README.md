
# __SOS Game__

Video Demo: 

## __Definition__
   This is a Python implementation of the classic SOS game, where players take turns placing the letters 'S' and 'O' on a grid, aiming to create sequences of "SOS" either vertically, horizontally, or diagonally.
   
   Project structure:
   
   * project.py
   * test_project.py
   * requirements.txt
   * README.md
   
## __Libraries__
   __Colorama__ = Colorama is a Python package enabling terminal text colorization, enhancing readability and interaction through cross-platform color support.
   
   __Pytest__ = Pytest is a Python testing framework, simplifying test creation and execution, ensuring code reliability through concise and intuitive syntax.
   
   __Re__ = The re module in Python offers regex-based string manipulation for efficient pattern matching and substitution.
   
## __Installation__

	You can install all of the libraries used in this project by using this pip command:
	```pip install -r requirements.txt```

## __Features__

- Interactive command-line interface with colorful output using the `colorama` library.
- Tracks player scores and game patterns (vertical, horizontal, diagonal).
- Implements game rules to check for winning patterns and end-of-game conditions.
- Validates user input for moves and letters.
	
## __Game Rules__

- Players take turns placing either 'S' or 'O' on an empty cell.
- The goal is to create sequences of "SOS" either vertically, horizontally, or diagonally.
- Players earn points for creating sequences.
- The game ends when all cells are filled, and the player with the most points wins.


## __Usage__

   Run the game by executing the `sos_game.py` script:

   ```bash
   python project.py
   ```

Follow the prompts to make your moves.


## __Functioning__
	The project.py contains 1 class and 12 functions including the main and init functions.
	
	### __SosGame__ __Class__ :
	This is the main class that manages the game.

1.  **`__init__(self)`**:
    Initializes the game's variables.

2.  **`run(self)`**:
    Starts the game by calling the board method.

3.  **`board(self)`**:
    Displays the game board and scores, and then calls get_input_ml to get the player's move.

4.  **`get_move(self, move, test_=0)`**:
    Handles player input for moves . Validates the input and calls get_input_ml for further input.

5.  **`get_letter(self, letter, move, test_=0)`**:
    Handles player input for letters ('S' or 'O'). Validates the input and calls play to update the game board.

6.  **`play(self, move, letter, test_=0)`**:
    Updates the game board with the player's move, marks cells with 'S' or 'O'. Calls score and end_game methods to check for "SOS" patterns and game completion.

7.  **`score_table(self, player)`**:
    Updates the score for the specified player when they complete an 'SOS' pattern.

8.  **`score(self, player)`**:
    Scans the game board for 'SOS' patterns vertically, horizontally, and diagonally. Calls score_table to update player scores.

9.  **`end_game(self)`**:
    Checks if the game has ended due to a full board and determines the winner or declares a draw.

10. **`exit_game(self, message)`**:
    Exits the game with a specified message.

11. **`get_input_ml(self, prompt, variable=None)`**:
    Handles user input prompts for moves and letters, calling the appropriate functions accordingly.


### Author: Eray Semiz


