import Spellcheck


def main():
    print_rules()

    again = True
    while again:
        level = set_level()
        play_game(level, 'english3.txt')
        # again = play_again()


def print_rules():
    print('Welcome to the word game known as "Hangman"!')
    print('This game has only a few rules:')
    print('Hangman is a simple word guessing game. Players try to figure out an unknown word by guessing letters.')
    print('If too many letters which do not appear in the word are guessed, the player is hanged (and loses).')
    print('You have 6 (six) one letter guesses.')
    print('However, you can choose the length of the word depending on the difficulty of your choosing.')
    input('Press "enter" when you are ready to play! ')


def set_level() -> int:
    easy = 4
    medium = 6
    hard = 7
    print('You can choose from three different levels, those being:')
    print(f'Easy: the mystery word will be {easy} characters long.')
    print(f'Medium: the mystery word will be {medium} characters long.')
    print(f'Hard: the mystery word will be {hard} characters long.')
    while True:
        level = input('At what difficulty would you like to play at? ').lower()
        if level == 'easy':
            return easy
        elif level == 'medium':
            return medium
        elif level == 'hard':
            return hard
        else:
            print('The input you have provided is invalid. Please enter one of "easy", "medium", or "hard".')


def play_game(level: int, wordfile: str):
    word = Spellcheck.random_valid_word(wordfile, level)
    guesses = 0
    wrong_guesses = 0
    max_wrong_guesses = 6


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

main()