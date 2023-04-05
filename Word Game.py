import Spellcheck
import random

def random_valid_word(wordfile: str, length: int) -> str:
    f = open(wordfile, "r")
    t = f.readlines()
    valid_words = []
    for w in t:
        stripped_word = w.strip()
        if len(stripped_word) == length:
            valid_words.append(stripped_word)
    while True:
        r = int(random.random() * len(valid_words))
        word = valid_words[r]
        if word:
            return word


def main():
    print_rules()
    print('')

    again = True
    while again:
        level = set_level()
        play_game(level, 'english3.txt')
        again = play_again()
        print('')


def print_rules():
    print('Welcome to the word game "Hangman"!')
    print('This game has only a few rules:')
    print('    Hangman is a simple word guessing game. Players try to figure out an unknown word by guessing letters.')
    print('    If too many letters which do not appear in the word are guessed, the player is hanged (and loses).')
    print('    You have 6 (six) one letter guesses.')
    print('    However, you can choose the length of the word depending on the difficulty of your choosing.')
    input('Press "enter" when you are ready to play! ')


def set_level() -> int:
    easy = 7
    medium = 5
    hard = 4
    print('You can choose from three different levels, those being:')
    print(f'Easy: the mystery word will be {easy} characters long.')
    print(f'Medium: the mystery word will be {medium} characters long.')
    print(f'Hard: the mystery word will be {hard} characters long.')
    while True:
        level = input('At what difficulty would you like to play at? ').lower()
        print('')
        if level == 'easy':
            return easy
        elif level == 'medium':
            return medium
        elif level == 'hard':
            return hard
        else:
            print('')
            print('The input you have provided is invalid. Please enter one of "easy", "medium", or "hard".')


def get_letter_input():
    while True:
        guess = input('Enter a letter: ').lower()
        if len(guess) != 1 or not guess.isalpha():
            print('Invalid input. Please enter a single letter.')
        else:
            return guess


def play_game(level: int, wordfile: str):
    word = Spellcheck.random_valid_word(wordfile, level)
    word_length = len(word)
    current_word = ['_'] * word_length
    print(' '.join(current_word))
    guesses = 0
    wrong_guesses = []
    max_wrong_guesses = 6

    while True:
        guess = get_letter_input()

        if guess in word:
            print('Correct guess!')
            for i in range(word_length):
                if word[i] == guess:
                    current_word[i] = guess
            print(' '.join(current_word))
        else:
            print('Wrong guess!')
            wrong_guesses.append(guess)
            print_hangman(len(wrong_guesses))
            print(f"Guesses: {', '.join(wrong_guesses)}")
            print(' '.join(current_word))

        guesses += 1
        if ''.join(current_word) == word:
            print('Congratulations, you guessed the word!')
            print(f'You made {guesses} guesses.')
            return False

        if len(wrong_guesses) == max_wrong_guesses:
            print(f'You lost. The word was: {word}')
            return False



def print_hangman(incorrect_guesses):
    stages = [
        # Stage 0 (empty gallows)
        '''
        ________
               |          
               |         
        ''',
        # Stage 1 (head)
        '''
        ________
               |          
               |           
            (O, _ O)
        ''',
        # Stage 2 (body)
        '''
        ________
               |          
               |           
            (O, _ O)
               |
               |
               |
               |
        ''',
        # Stage 3 (one arm)
        '''
        ________
               |          
               |           
            (O, _ O)
               |
             \ |
               |
               |
        ''',
        # Stage 4 (other arm)
        '''
        ________
               |          
               |           
            (O, _ O)
               |
             \ | / 
               |
               |
        ''',
        # Stage 5 (one leg)
        '''
        ________
               |          
               |           
            (O, _ O)
               |
             \ | / 
               |
               |
              / 
        ''',
        # Stage 6 (other leg)
        '''
        ________
               |          
               |           
            (O, _ O)
               |
             \ | / 
               |
               |
              / \ 
            You Lose
        ''',
    ]
    print(stages[incorrect_guesses])


def play_again():
    while True:
        play = input('Do you want to play again? (y/n): ').lower()
        if play == 'y':
            return True
        elif play == 'n':
            return False
        else:
            print('Invalid input. Please enter either "y" or "n".')


main()

# This is probably the hardest game of hangman that anyone could play because the possible words that the user
# can guess spans almost 10,000 words...They will have to know a lot of words, and many
# variations of those words.

# That being said, it is a working game of Hangman. To adjust the difficulty, I could add in a function
# that is similar to the lab we did with the Caesar Cypher. Somehow, getting a list of the
# most common words used in the english lexicon, then cross-referencing that with the available dictionary...
# However, I feel like that is above the scope of the lab.

# Another point that I wanted to make, is how easy it is to change this game into a two-player mode.
# Literally, just changing the "def random_valid_word()" function to not take in the "english.txt"
# file, you can add a word yourself. I'm sure with some additional tweaking such as: changing
# the possible difficulties, adding a sentence mode instead of just a single word, etc.
# You could spice up the challenge, and make it more similar to the Hangman most humans play with
# each other.
