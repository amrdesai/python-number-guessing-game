#Number Guessing Game:

# Imports
from random import randint

# Constants & Variables
EASY_LEVEL = 10
HARD_LEVEL = 5
turns = 0


# Function: Check user's guess with actual answer
def check_answer(guess, answer, turns):
    """
    Checks answers against guess. Returns no: of turns remaining.
    """
    # Check answer
    if guess > answer:
        print('Guess is too high.')
        return turns - 1
    elif guess < answer:
        print('Guess is too tow.')
        return turns - 1
    else:
        print(f'Congratulations, {guess} is the right answer!')


# Function: Set difficulty
def set_difficulty():
    """
    Set the difficulty of the game 'easy' = 10 attemps and 'hard' = 5 attempts
    """
    game_mode = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if (game_mode == 'easy'):
        return EASY_LEVEL
    else:
        return HARD_LEVEL

def game():
    # View welcome message
    print(
        "Welcome to the Number Guessing Game\nI'm thinking a number between 1 and 100."
    )

    # Choose number b/w 1 & 100
    answer = randint(1, 100)
    print(f'Answer: {answer}')

    #  Set game difficulty
    turns = set_difficulty()

    # Repeat game if user has attempts left
    guess = 0
    while guess != answer:
        # Print no:of attempts remaining
        print(f'You have {turns} attempts remaining to guess the number.')
        guess = int(input("Make a guess: "))
        #  Check Answer
        turns = check_answer(guess, answer, turns)
        # Check attempts left & finish game if no attempts left
        if turns == 0:
            game_over = True
            print(f'Game Over! You have no attempts left, the correct answer was {answer}.')
            return


# Run game
game()
