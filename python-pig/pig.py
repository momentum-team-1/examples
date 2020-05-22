"""
Gameplay
- pick a starting player (TODO)
- starting player rolls a die
    - if it's a 1, no points, turn over
    - if it's a 2-6, add roll to round points
        - ask if you want to continue
            - if so, repeat
            - else, add round points to total score
- does player have >= 50 points? they win
- other player rolls a die
    - if it's a 1, no points, turn over
    - if it's a 2-6, add roll to round points
        - ask if you want to continue
            - if so, repeat
            - else, add round points to total score
- does player have >= 50 points? they win
- repeat if no winner

Functions/things to implement

- roll a die
- handle a round (looping until exit)
    - human player -- ask for input
    - computer player -- display decisions
- handle whole game loop

Step 1: roll a die
Step 2: play one round
"""

import random


def roll_die():
    """Roll a six-sided die and return results."""
    return random.randint(1, 6)


def play_human_round():
    """
    Repeatedly roll a die.
    If you roll a 1, then return 0.
    Else, add to total and ask player whether to repeat.
    If not, return total.
    """
    total = 0

    while True:
        roll_result = roll_die()
        print(f"You rolled a {roll_result}!")

        if roll_result == 1:
            print("Too bad! You score nothing.")
            return 0

        total += roll_result
        print(f"Your total is {total}.")

        # TODO come back and improve with error-checking
        keep_going = input("Do you want to keep going [y/n]? ")
        if keep_going.lower() != "y":
            return total


def play_computer_round():
    """
    Repeatedly roll a die.
    If you roll a 1, then return 0.
    Else, add to total. If the total >= 20, return total.
    Else, keep going.    
    """

    total = 0
    while total < 20:
        roll_result = roll_die()

        if roll_result == 1:
            print("Computer rolled a 1! They receive no points.")
            return 0

        total += roll_result
        print(f"Computer rolled a {roll_result}. Their total is {total}.")

    print(f"Computer holds at {total}.")
    return total


def play_pig():
    """
    Run the game of Pig until either the human or computer gets 50 points.
    """

    human_score = 0
    computer_score = 0

    while True:
        print(f"Your current score is {human_score}.")
        human_score += play_human_round()
        print(f"Your new score is {human_score}.")
        if human_score >= 50:
            print("You win!")
            return
        print("\n")

        print(f"The computer's current score is {computer_score}.")
        computer_score += play_computer_round()
        print(f"The computer's new score is {computer_score}.")
        if computer_score >= 50:
            print("The computer wins!")
            return
        print("\n")


if __name__ == "__main__":
    play_pig()
