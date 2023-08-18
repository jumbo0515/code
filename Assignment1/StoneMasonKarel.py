"""
File: StoneMasonKarel.py
Name: Jumbo
--------------------------------
At present, the StoneMasonKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to build a column (a vertical structure
that is 5 beepers tall) in each avenue that is either on the right
or left side of the arch, as described in the Assignment 1 handout. 
Karel should end on the last avenue, 1st Street, facing east. 
"""

from karel.stanfordkarel import *


def main():
    """
    pre-condition:karel is at Street1,Avenue1,facing East
    post-condition:karel is fix pillar finish at Street1,Avenue13,facing East
    """
    job()
    get_off_work()


def job():
    """
    pre-condition:karel is top at pillar,facing East
    post-condition:karel is top at next pillar,facing East
    """
    while front_is_clear():
        fix()
        next_pillar()
        go_bottom()


def fix():
    """
    pre-condition:karel is bottom at pillar,facing East
    post-condition:karel is top at pillar,facing East
    """
    turn_left()
    while front_is_clear():
        if on_beeper():
            move()
        else:
            put_beeper()
            move()
    if not on_beeper():
        put_beeper()
    turn_right()
    # facing East


def next_pillar():
    """
    pre-condition:karel is top at pillar,facing East
    post-condition:karel is top at next pillar,facing East
    """
    move()
    while left_is_clear():
        move()


def go_bottom():
    """
    pre-condition:karel is top at pillar,facing East
    post-condition:karel is bottom at pillar,facing South
    """
    turn_right()
    while front_is_clear():
        move()
    turn_left()


def get_off_work():
    """
    pre-condition:karel at the bottom at final pillar,facing East
    post-condition:karel finishes at the bottom and finishes the final pillar facing West
    """
    fix()
    go_bottom()


def turn_right():
    for i in range(3):
        turn_left()












# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
