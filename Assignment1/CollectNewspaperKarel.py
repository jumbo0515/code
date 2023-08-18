"""
File: CollectNewspaperKarel.py
Name: Jumbo
--------------------------------
At present, the CollectNewspaperKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to walk to the door of its house, pick up the
newspaper (represented by a beeper, of course), and then return
to its initial position in the upper left corner of the house.
"""

from karel.stanfordkarel import *


def main():
    """
    pre-condition:karel is at Street4,Avenue3,facing East
    post-condition:karel is at Street4,Avenue3 with newspaper,facing East
    """
    go_out()
    pick_beeper()
    go_back()
    put_beeper()


def go_out():
    """
    pre-condition:karel is at Street4,Avenue3,facing East
    post-condition:karel is at Street3,Avenue6,facing East
    """
    turn_right()
    move()
    turn_left()
    move()
    move()
    move()


def turn_right():
    for i in range(3):
        turn_left()


def go_back():
    """
    pre-condition:karel is at Street3,Avenue6,facing East
    post-condition::karel is at Street4,Avenue3 with newspaper,facing East
    """
    turn_around()
    move()
    move()
    move()
    turn_right()
    move()
    turn_right()


def turn_around():
    turn_left()
    turn_left()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
