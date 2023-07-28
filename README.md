#**Pygame Hangman Game with MVC Model**#
This is a Pygame implementation of the popular Hangman game, following the Model-View-Controller (MVC) design pattern.

*Description*
In this game, the player must guess a secret word by suggesting letters, one at a time. The game provides a hint in the form of a series of underscores, each representing a letter in the secret word. For each correct guess, the corresponding underscore is replaced by the guessed letter. For each incorrect guess, a part of the hangman is drawn. The player has a limited number of attempts to guess the word before the hangman is fully drawn, and if they fail to guess the word, they lose the game.

The project follows the MVC design pattern, with each component responsible for a specific task:

- Model: contains the game's data and logic, such as the secret word, the player's guesses, and the state of the game (e.g., whether the game is won or lost).
- View: handles the game's presentation and user interface, such as rendering the game graphics and handling user input.
- Controller: handles user input and communicates with the model and view to update the game state and graphics.
*Dependencies*
This project requires the following dependencies:

- Python 3.x
- Pygame library
*Installation*
To install the project, first make sure you have Python 3.x installed. You can download Python from the official website at https://www.python.org/downloads/.

Next, install the Pygame library by running the following command in your terminal or command prompt:
`pip install pygame`
*Usage*
To start the game, navigate to the project directory and run the following command in your terminal or command prompt:

`python main.py`
The game should start, and you can use the keyboard to guess letters. The game provides feedback on whether the guessed letter is correct or incorrect and updates the hangman accordingly. If you guess the word correctly, you win the game, but if the hangman is fully drawn before you guess the word, you lose.

