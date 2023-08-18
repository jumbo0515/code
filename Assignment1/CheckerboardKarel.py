"""
File: CheckerboardKarel.py
Name: Jumbo
----------------------------
When you finish writing it, CheckerboardKarel should draw
a checkerboard using beepers, as described in Assignment 1. 
You should make sure that your program works for all of the 
sample worlds provided in the starter folder.
"""

from karel.stanfordkarel import *


def main():
    """
    pre-condition:karel at (1,1),facing East
    post-condition:karel is finish put beeper job at anyway,facing East
    """
    if not front_is_clear():
        # for 8x1
        turn_left()
        fell_one_line()
        turn_right()
    else:
        while not on_beeper():
            fell_one_line()
            if not front_is_clear():
                next_line()
                if not on_beeper():
                    fell_second_line()
                    next_line()


def fell_one_line():
    """
    pre-condition:karel at the (1,1),facing East
    post-condition:karel is finish one line beeper job at pre-condition,facing East
    """
    put_beeper()
    while front_is_clear():
        if on_beeper():
            move()
        else:
            if front_is_clear():
                move()
                put_beeper()
    # Determine whether to reach the wall
    if not facing_north():
        turn_around()
        while front_is_clear():
            move()


def fell_second_line():
    """
    pre-condition:karel on the far left,facing East
    post-condition:karel is finish one line beeper job at pre-condition,facing East
    """
    while front_is_clear():
        if on_beeper():
            move()
        else:
            if front_is_clear():
                move()
                put_beeper()
    # Determine whether to reach the wall
    if not facing_north():
        turn_around()
        while front_is_clear():
            move()


def next_line():
    if not front_is_clear():
        turn_right()
        if facing_north():
            if front_is_clear():
                move()
                turn_right()


def turn_around():
    turn_left()
    turn_left()


def turn_right():
    for i in range(3):
        turn_left()











# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
