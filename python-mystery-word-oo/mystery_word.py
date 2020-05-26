import random


class DictionaryReader:
    """
    Reads the file words.txt from disk and parses it to get all words.
    """
    def __init__(self):
        self.words = []
        self.read_words_from_file()
        self.remove_proper_nouns()

    def read_words_from_file(self):
        """
        Read all words from words.txt.
        """
        file = open("words.txt")
        lines = file.readlines()
        file.close()

        self.words = [line.strip() for line in lines]

    def remove_proper_nouns(self):
        self.words = [word for word in self.words if not word[0].isupper()]

    def pick_random_word(self):
        return random.choice(self.words)


class WordDisplay:
    """
    Displays our word for the player based on their guesses.
    """
    def __init__(self, word):
        self.word = word

    def get_display(self, guesses):
        chars = []
        for char in self.word:
            if char in guesses:
                chars.append(char.upper())
            else:
                chars.append("_")
        return " ".join(chars)


def is_letter(a_string):
    return len(a_string) == 1 and a_string.isalpha()


class Game:
    def __init__(self):
        self.guesses = []
        self.bad_guesses_allowed = 8

    def count_guesses_left(self):
        bad_guesses = [
            guess for guess in self.guesses if guess not in self.word
        ]
        num_bad_guesses = len(bad_guesses)
        return self.bad_guesses_allowed - num_bad_guesses

    def ask_user_for_guess(self):
        while True:
            guess = input("Guess a letter: ")

            if not is_letter(guess):
                print("Please enter a letter.")
            elif guess.lower() in self.guesses:
                print("You have already guessed that letter.")
            else:
                self.guesses.append(guess.lower())
                return

    def check_game_over(self):
        return self.count_guesses_left() == 0 or self.check_word_guessed()

    def check_word_guessed(self):
        letters_left_to_guess = []
        for letter in self.word:
            if letter not in self.guesses:
                letters_left_to_guess.append(letter)

        return len(letters_left_to_guess) == 0

    def play(self):
        reader = DictionaryReader()
        self.word = reader.pick_random_word()
        display = WordDisplay(self.word)

        while not self.check_game_over():
            print(display.get_display(self.guesses))
            print(f"You have {self.count_guesses_left()} guesses left.")
            self.ask_user_for_guess()

        if self.check_word_guessed():
            print("You guessed it!")
        else:
            print(f"The word was {self.word.upper()}. Better luck next time!")


if __name__ == "__main__":
    play_again = True
    while play_again:
        game = Game()
        game.play()
        user_input = input("Do you want to play again [y/N]? ")
        play_again = user_input.upper() == "Y"
