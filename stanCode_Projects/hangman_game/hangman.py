"""
File: hangman.py
Name:Jumbo (feat. Panda)
-----------------------------
This program plays hangman game.
Users see a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    Hangman man game: Guess the word in random_word(),and you will lose one chance if you make a mistake.There are
    seven times in total. If there is no chance, the game will end.
    """

    guesses = random_word()
    n_ans = ''
    for i in range(len(guesses)):  # 打上底線
        n_ans += '_'

    turns = N_TURNS
    while True:
        print('The word looks like ' + n_ans)
        print("You have " + str(turns) + " wrong guesses left.")
        if turns == 0:  # boundary condition (邊界條件)
            print('You are completely hung : (')
            print('The word was: ' + str(guesses))
            break
        if n_ans == guesses:  # finish
            print('You win!!')
            print('The word was: ' + str(guesses))
            break
        guess = input("Your guess: ").upper()
        if guess.isalpha() and len(guess) == 1:
            if guess in guesses:
                print("You are correct!")
                nn = ''
                for i in range(len(guesses)):
                    ch = guesses[i]
                    if guess == ch:
                        nn += guess    # 猜對後串底線
                    else:
                        nn += n_ans[i]  # 猜對串上去
                n_ans = nn
            else:
                print("There is no " + str(guess) + "'s in the word.")
                turns -= 1
        else:
            print('illegal format')


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
